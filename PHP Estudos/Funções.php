<?php
/* CONTROLE DE EXECUÇÃO */

// die(): Mata a execução do script na hora.
// sleep(n): Pausa a execução por n segundos.

//1. DIE
// O die() para o PHP na mesma hora. Nada que estiver abaixo dele será executado. 
// É muito usado em verificações de segurança ou para debugar o código.

$usuario_logado = false;

if (!$usuario_logado) {
    // Para o site e mostra uma mensagem
    die("❌ ERRO: Você precisa estar logado para ver esta página.");
}

// Isso nunca será lido se o die() for executado
echo "Bem-vindo à área restrita!";

//2. SLEEP
// O sleep() faz o PHP "dormir" por alguns segundos antes de continuar. 
// No desenvolvimento profissional, usamos isso para evitar ataques de força bruta ou esperar uma resposta de uma API externa.

echo "Iniciando o processo... <br>";

// Espera 3 segundos antes de continuar
sleep(3);

echo "Processo finalizado após 3 segundos! ✅";

/* FUNÇÃO */

//1. Basico
//Apenas executa uma tarefa, como imprimir um HTML repetitivo.
function saudacao($nome) {
    echo "<h2>Olá, $nome! Bem-vindo ao sistema. ✅</h2>";
}

saudacao("Rafin"); // Chama a função passando o nome
saudacao("João");

//.2 Retorno
//Ela processa o dado e "devolve" o resultado para você guardar em uma variável.
function calcularDesconto($valor, $porcentagem) {
    $desconto = ($valor * $porcentagem) / 100;
    return $valor - $desconto;
}

$precoFinal = calcularDesconto(100, 15); // Devolve 85
echo "O preço com desconto é: R$ " . number_format($precoFinal, 2, ',', '.');

//3. Valor Padrão
//Você pode definir um valor que a função usa se você não mandar nada.
function configurarTema($tema = "claro") {
    echo "O tema do site agora é: $tema";
}

configurarTema(); // Usa "claro"
configurarTema("escuro"); // Usa "escuro"

/* Funções Nativa */

//1. DATE
//A função date() é a ferramenta nativa do PHP para trabalhar com tempo.

// d: Dia (01 a 31)
// m: Mês (01 a 12)
// Y: Ano com 4 dígitos (2026)
// H: Hora (00 a 23)
// i: Minutos (00 a 59)
// s: Segundos (00 a 59)

// Exibe: 12/03/2026
echo "Data de hoje: " . date("d/m/Y"); 
echo "<br>";
// Exibe: 16:44:05 (Hora:Minuto:Segundo)
echo "Hora atual: " . date("H:i:s"); 

//Fuso horario
date_default_timezone_set('America/Sao_Paulo');
echo "Hora certa no Brasil: " . date("H:i");

//Passado e Futuro
// "+1 day" (Amanhã)
// "+1 week" (Daqui a 7 dias)
// "+1 month" (Mês que vem)
// "+2 hours" (Daqui a 2 horas)
// "next Thursday" (Próxima quinta-feira)
// "last Monday" (Segunda passada)

// Amanhã
$amanha = strtotime("+1 day");
echo "Amanhã será: " . date("d/m/Y", $amanha);

// Daqui a 1 semana
$proximaSemana = strtotime("+1 week");
echo "Daqui a 7 dias: " . date("d/m/Y", $proximaSemana);

//2. INCLUDE

// O include é a ferramenta que os profissionais usam para não precisar repetir código em várias páginas. 
// Com ele, você "chama" o conteúdo de um arquivo para dentro de outro.
// No PHP profissional, usamos isso para separar o Header (topo), o Footer (rodapé) e as Configurações do site.

include 'topo.php';
echo "<p>Bem-vindo à página inicial!</p>";
include 'rodape.php';

// include 'arquivo.php';
// Tenta carregar o arquivo. Se o arquivo não existir, o PHP dá um aviso (Warning), mas o resto do site continua funcionando.

// require 'arquivo.php';
// Obrigatório. Se o arquivo não existir, o PHP dá um erro fatal e para tudo. Use para conexões de banco de dados ou senhas.

// include_once / require_once
// Garante que o arquivo seja carregado apenas uma vez. 
// Se você tentar incluir o mesmo topo duas vezes por erro, o PHP ignora a segunda. É o mais usado em sistemas grandes.

require_once 'vendor/autoload.php'; // Carrega o motor do Composer uma única vez
require_once 'config.php';          // Carrega suas configurações

//3. MANIPULAÇÃO DE STRING

//strtoupper()                              Tudo Maiuscula
//strtolower()                              Tudo Minuscula
//ucwords()                                 Primeira letra de cada palavra maiuscula
//trim()                                    Remove espaço
//str_replace(troca_esse, por_esse, texto)  Substitui o conteudo
//strlen()                                  Conta quantas strigs tem
//substr(texto, inicio, fim)                Corta o texto
//explode(onde_cortar,texto)                Transfoma o texto em array
//implode(intervalo_array, texto)           Transforma o array em texto

//Alterando Case

$nome = "rafin dev";

echo strtoupper($nome); // RAFIN DEV (Tudo grande)
echo "<br>";
echo strtolower("SITE EM MAIÚSCULO"); // site em maiúsculo (Tudo pequeno)
echo "<br>";
echo ucwords($nome); // Rafin Dev (Primeira letra de cada palavra em maiúscula)

//Limpeza de dados

$email_sujo = "  contato@email.com  ";
$email_limpo = trim($email_sujo); // Remove espaços do início e do fim

echo "E-mail: " . $email_limpo;

//Substituição e Busca

$texto = "O PHP é ultrapassado.";

// Substitui uma palavra por outra
$novo_texto = str_replace("ultrapassado", "incrível", $texto);
echo $novo_texto; // O PHP é incrível.

// Conta quantos caracteres tem o texto
echo strlen($texto); // Retorna o tamanho da frase

//Pedaço de texto

$post = "Este é um artigo muito longo sobre programação PHP moderna...";
echo substr($post, 0, 20) . "..."; // Pega do caractere 0 até o 20 e concatena com 3 pontinhos

//Transforma texto em array

$nomeCompleto = "Rafael Ferreira Silva";
// O primeiro parâmetro " " é onde o PHP deve "cortar"
$partes = explode(" ", $nomeCompleto);

echo "O primeiro nome é: " . $partes[0]; // Resultado: Rafael
echo "<br>O sobrenome é: " . $partes[1]; // Resultado: Ferreira

//Transforma array em texto

$habilidades = ["PHP", "MySQL", "Next.js", "Docker"];
// O primeiro parâmetro ", " é o que vai ficar entre os itens
$textoParaBanco = implode(", ", $habilidades);
echo "Habilidades do candidato: " . $textoParaBanco;
// Resultado: PHP, MySQL, Next.js, Docker

//4. MANIPULAÇÃO DE ARRAY

//array_push()                  Adiciona um ou mais elementos no final de um array que já existe.
//array_merge()                 Une dois ou mais arrays em um só. Muito útil para combinar dados de diferentes tabelas.
//in_array()                    Verifica se um valor específico existe dentro da lista. Retorna true ou false.
//array_keys()                  Separa as "chaves" do array. Essencial para criar relatórios automáticos.
//array_values()                Separa os valores da chave do array
//count()                       Diz quantos itens existem na lista.
//sort()                        Coloca o array em ordem alfabética ou numérica.
//asort()                       Coloca em ordem, mas mantém a conexão "Chave => Valor" (importante para arrays associativos).
//array_filter(array,teste)     Remove itens vazios null ou false ou opcional um teste que não passa (ex: filtrar só produtos caros).
//array_intersect_key()         Mantem apenas os itens cujas chaves existam em todos eles.
//array_map(função, array)      Tranforma ou limpa os elemento do array

//Adiciona no fim
$carrinho = ["Mouse", "Teclado"];
array_push($carrinho, "Monitor", "Fone"); // Adicionou dois itens
// Jeito simplificado (mais usado por profissionais):
$carrinho[] = "Webcam"; 
print_r($carrinho);
// Resultado: ["Mouse", "Teclado", "Monitor", "Fone", "Webcam"]

//Junta dois ou mais arrays
$lista1 = ["PHP", "MySQL"];
$lista2 = ["Laravel", "Docker"];
$mapa_estudos = array_merge($lista1, $lista2);
// Resultado: ["PHP", "MySQL", "Laravel", "Docker"]

//Verifica se tem o conteudo no array retorna true ou false
$usuarios = ["rafin", "admin", "visitante"];
if (in_array("admin", $usuarios)) {
    echo "✅ Acesso de administrador confirmado!";
}

//Retorna Chaves e valores das chaves
$usuario = ["nome" => "Rafin", "nivel" => "Sênior", "status" => "Ativo"];
$colunas = array_keys($usuario); // ["nome", "nivel", "status"]
$dados   = array_values($usuario); // ["Rafin", "Sênior", "Ativo"]

//Conta itens do array
echo "Você tem " . count($carrinho) . " itens no carrinho.";


$frutas = ["d" => "Limão", "a" => "Abacaxi", "b" => "Melancia"];

//Substitui as chaves por numero e coloca em ordem Alfabetica
$copia1 = $frutas;
sort($copia1); 
// Resultado: [0 => Abacaxi, 1 => Limão, 2 => Melancia] -> Perdeu as letras d, a, b

//Coloco em ordem Alfabetica
$copia2 = $frutas;
asort($copia2); 
// Resultado: ["a" => Abacaxi, "d" => Limão, "b" => Melancia] -> Manteve as letras!

//Fitro com 1 parametro
$dados_sujos = ["Rafin", "", "Dev", null, "PHP", false];
$dados_limpos = array_filter($dados_sujos); //Remove "", null e false

// Resultado: ["Rafin", "Dev", "PHP"]
print_r($dados_limpos);

//Filtro com 2 parametro
$produtos = [
    ["nome" => "Mouse", "preco" => 50],
    ["nome" => "Teclado", "preco" => 150],
    ["nome" => "Monitor", "preco" => 800],
    ["nome" => "Cabo USB", "preco" => 15]
];

// Filtrar apenas produtos que custam MAIS de 100 reais
$caros = array_filter($produtos, function($item) { //função que faz um teste e retorna true ou false
    return $item['preco'] > 100; //Se for false o filter exclui o array
});

echo "<h3>Produtos Premium:</h3>";
foreach ($caros as $p) {
    echo $p['nome'] . " - R$ " . $p['preco'] . "<br>";
}

// Retorna so as chaves iguais
// 1. Dados que vieram do Banco de Dados (Muitas informações)
$usuarioBanco = [
    "id" => 1,
    "nome" => "Rafin",
    "email" => "rafin@dev.com",
    "senha" => "123456", // Dado sensível!
    "token" => "abcde",  // Dado sensível!
    "criado_em" => "2024-01-01"
];
// 2. O "Filtro" (Quais chaves eu REALMENTE quero mostrar)
$camposPermitidos = [
    "nome" => null, 
    "email" => null
];
// 3. A Mágica: Mantém apenas o que bater com as chaves do filtro
$usuarioSeguro = array_intersect_key($usuarioBanco, $camposPermitidos);
// Resultado: 
// Array (
//     [nome] => Rafin
//     [email] => rafin@dev.com
// )

// Transforma ou limpa o array
$nomesNoBanco = ["  rafin ", " ANA", " joão  "];
// O array_map aplica uma função (como o trim ou strtoupper) em cada item
$nomesLimpos = array_map('trim', $nomesNoBanco);
$nomesFormatados = array_map('ucwords', $nomesLimpos);
/* 
Resultado: 
Array (
    [0] => Rafin
    [1] => Ana
    [2] => João
)
*/