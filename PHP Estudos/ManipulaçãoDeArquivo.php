php<?php
/*📚 Gerenciamento de Sistema de Arquivos (Filesystem) */

//1. Pastas (Diretórios)

//mkdir("nome", permissao); – Cria uma pasta.
//is_dir("nome");           – Verifica se a pasta existe.
//rmdir("nome");            – Remove uma pasta (precisa estar vazia).

$pasta = "uploads";

if (!is_dir($pasta)) {
    mkdir($pasta, 0777); // Cria com permissão total de leitura/escrita
    echo "Pasta criada!";
}

//Permissões de Sistema (Octal).
// 1º número (7): O que o Dono (você/script) pode fazer.
// 2º número (7): O que o Grupo (outros scripts do servidor) pode fazer.
// 3º número (7): O que o Público (qualquer visitante do site) pode fazer.

// O número é a soma de três ações básicas:
// 4 = Ler (Read)
// 2 = Escrever (Write)
// 1 = Executar (Execute)
// Soma (4+2+1) = 7 (Pode tudo!)

// As Permissões mais comuns:
// Código	O que significa?	Quando usar?
// 0777	Acesso Total: Todo mundo lê, escreve e apaga.	Testes ou pastas de Upload temporárias.
// 0755	Padrão Seguro: Você faz tudo, o resto só lê.	Na maioria das pastas do seu site.
// 0644	Apenas Leitura: Ninguém (além de você) escreve.	Arquivos de configuração e imagens.

//Obs: Obrigatorio 0 na frente


//2. Arquivos: O Jeito Moderno e Rápido

//file_put_contents("arquivo.txt", "texto"); – Cria e escreve no arquivo.
//file_get_contents("arquivo.txt");          – Lê todo o conteúdo do arquivo.

$conteudo = "Novo acesso em: " . date("H:i:s");

// O FILE_APPEND serve para não apagar o que já existia (adiciona no fim)
// PHP_EOL Quebra de linha correta
file_put_contents("log.txt", $conteudo . PHP_EOL, FILE_APPEND);

echo file_get_contents("log.txt");

//3. Arquivos: O Jeito Clássico (Controle Total)

// $f = fopen("nome_do_arquivo", "modo") – Abre o arquivo.
// fwrite($f, "texto"); – Escreve.
// fgets($f); – Lê uma linha.
// fclose($f); – Obrigatório fechar para liberar o arquivo.

// Modos Principais (fopen):
// 'w': Escreve (apaga o que tinha antes).
// 'a': Adiciona no final.
// 'r': Só leitura. 

// 4. Outras Funções Úteis

// unlink("arquivo.txt"); – Deleta um arquivo.
// rename("antigo.txt", "novo.txt"); – Renomeia ou Move um arquivo.
// file_exists("arquivo.txt"); – Verifica se o arquivo existe. 

/*📚 Manipulação de Dados: JSON e XML*/

//1. JSON (JavaScript Object Notation)

//O PHP transforma Arrays/Objetos em texto JSON e vice-versa com apenas duas funções.

// json_encode($dados)          – Transforma Array em Texto.
// json_decode($texto, true)    – Transforma Texto em Array.

$usuario = ["nome" => "João", "idade" => 25];

// 1. Gerar JSON (Escrita)
$jsonTexto = json_encode($usuario);
file_put_contents("usuario.json", $jsonTexto);

// 2. Ler JSON (Leitura)
$jsonLido = file_get_contents("usuario.json");
$dados = json_decode($jsonLido, true); // O 'true' transforma em Array

echo $dados['nome']; // Saída: João

//2. XML (SimpleXML)

//O PHP usa a classe SimpleXMLElement para ler e criar arquivos XML de forma fácil.

// new SimpleXMLElement($xml) – Cria um objeto XML.
// $xml->asXML("arquivo.xml") – Salva o arquivo.

// 1. Criar XML (Escrita)
$xml = new SimpleXMLElement('<cliente></cliente>');
$xml->addChild('nome', 'Maria');
$xml->addChild('cidade', 'São Paulo');
$xml->asXML('cliente.xml');

// 2. Ler XML (Leitura)
$xmlLido = simplexml_load_file('cliente.xml');
echo $xmlLido->nome; // Saída: Maria

//Diferença

// JSON	{"nome": "João"}	-APIs, Mobile, Web.
// XML	<nome>João</nome>	-Notas Fiscais (NF-e), Bancos.