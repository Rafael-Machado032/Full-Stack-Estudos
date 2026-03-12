<?php

/* IMPPRIMIR NA TALA */
echo "Ola mundo";

echo "<pre>";

/* VARIÁVEIS SUPERGLOBAIS DO PHP */

// Essas variáveis são arrays nativos que o PHP já traz prontos.
// Elas estão disponíveis em qualquer parte do seu código.

// $_GET: Dados que aparecem na URL (ex: ?id=10).
// $_POST: Dados "escondidos" enviados por formulários (ex: Senhas).
// $_FILES: Tudo sobre arquivos que o usuário faz Upload (fotos, PDFs).
// $_SESSION: Dados que não somem quando você muda de página (ex: "Usuário Logado").
// $_COOKIE: Dados guardados no navegador do cliente (ex: "Lembrar meu login").
// $_SERVER: Informações do "dono da casa" (IP do usuário, nome do servidor, pasta do arquivo).
// $_ENV: Variáveis de ambiente (usadas para guardar senhas do Banco de Dados com segurança).
// $_REQUEST: Uma "mistura" que contém GET, POST e COOKIE ao mesmo tempo (evite usar, é melhor ser específico).



// 1. $_GET: Captura dados enviados pela URL (após o ?)
// Exemplo de URL: localhost:8000/index.php?nome=Rafin&id=10
echo "Nome via GET: " . ($_GET['nome'] ?? 'Não enviado');

echo "<pre>";
// 2. $_POST: Captura dados enviados de forma oculta (Formulários)
// Exemplo: Usado em formulários de Login ou Cadastro (Senha nunca vai na URL)
echo "Senha via POST: " . ($_POST['senha'] ?? 'Não enviado');

echo "<pre>";
// 3. $_SESSION: Mantém dados salvos enquanto o usuário navega no site
// Exemplo: Armazenar se o usuário está logado ou itens no carrinho
session_start(); // Obrigatório para usar sessões
$_SESSION['usuario'] = "RAFAEL MACHADO";
echo "Usuario: ".($_SESSION["usuario"]);
echo "</pre>";

echo "<pre>";
// 4. $_COOKIE: Dados guardados no navegador do visitante (por dias/meses)
// Exemplo: Salvar a preferência de "Tema Escuro" do site
setcookie("tema", "dark", time() + 3600); // Salva por 1 hora
// LENDO o cookie (Pegando o que o navegador nos enviou)
echo "O tema escolhido é: " . $_COOKIE['tema'];
echo "</pre>";

echo "<pre>";
// 5. $_SERVER: Informações sobre o ambiente e o servidor
// Exemplo: Pegar o endereço IP do visitante ou o nome do arquivo atual
echo "Seu IP é: " . $_SERVER['REMOTE_ADDR'];
echo "<br/>";
echo "Arquivo atual: " . $_SERVER['PHP_SELF'];
echo "</pre>";

echo "<pre>";
// 6. $_FILES: Gerencia Uploads de arquivos
// Exemplo: Quando o usuário envia uma foto de perfil
echo "
<form method='POST' enctype='multipart/form-data'>
    <input type='file' name='foto'>
    <button type='submit'>Enviar Arquivo</button>
</form>
";
echo "Nome da foto: " . ($_FILES['foto']['name'] ?? 'Aguardando envio...');
echo "</pre>";

echo "<pre>";
// 7. $_ENV: Variáveis de ambiente do sistema
// Exemplo: Usado em nível profissional para esconder senhas do Banco de Dados. 
// Para ler criase o arquivo .env
// Nescessario instalar a bibioteca o camando "composer require vlucas/phpdotenv"
// instala e cria a pasta ventor
// No arquivo importa a biblioteca. Carrega o Autoload do Composer (Obrigatório!)
require 'vendor/autoload.php';

// Configura a biblioteca para ler a pasta atual (__DIR__)
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

// Agora a leitura funciona
echo "Banco de Dados: " . $_ENV['DB_HOST'];
echo "</pre>";

echo "<pre>";
// 8. $_REQUEST: Uma mistura de $_GET e $_POST (Evite usar no profissional)
// Exemplo: Ele tenta achar o dado em qualquer lugar, o que é menos seguro
echo "Request nome: " . ($_REQUEST['nome'] ?? 'Vazio');
echo "</pre>";

echo "<pre>";
// 9. $GLOBALS: Acesso a todas as variáveis globais do script
// Exemplo: Se você criar uma variável fora de uma função e quiser usar dentro
$x = 10;
echo $GLOBALS['x'];
echo "</pre>";

/* CRIANDO VARIÁVEIS NO PHP (REGRAS E BOAS PRÁTICAS) */

// 1. Strings (Textos) - Use aspas duplas para interpretar variáveis dentro
$nome_usuario = "Rafin"; 
$sobrenome = 'Dev'; // Aspas simples são levemente mais rápidas para texto puro

// 2. Integers (Números Inteiros)
$idade = 25;

// 3. Floats (Números Decimais) - Use PONTO, nunca vírgula
$preco_produto = 19.90;

// 4. Booleans (Verdadeiro ou Falso) - Muito usado em IFs
$esta_logado = true;
$tem_desconto = false;

// 5. Arrays (Listas de dados) - O jeito moderno
$cursos = ["PHP", "Next.js", "MySQL"];

// 6. Constantes - Valores que NÃO mudam (não usa $)
define("PI", 3.14);
define("URL_SITE", "http://localhost:8000");


/* Array */

//1. Lista Simples
$cursos = ["PHP", "Next.js", "MySQL"];

echo $cursos[0]; // Exibe: PHP
echo $cursos[1]; // Exibe: Next.js

//2. Associativo (Chave e Valor)
$usuario = [
    "nome" => "Rafael",
    "idade" => 37,
    "profissao" => "Desenvolvedor"
];
echo "<pre>";
echo $usuario["nome"]; // Exibe: Rafin
echo "</pre>";
echo "<pre>";
echo "Ele tem " . $usuario["idade"] . " anos.";
echo "</pre>";

echo "<pre>";
//3. Multidimensional (Lista de Listas)
$usuarios = [
    ["nome" => "Rafin", "email" => "rafin@email.com"],
    ["nome" => "João", "email" => "joao@email.com"]
];

echo $usuarios[0]["nome"]; // Acessa o nome do primeiro usuário (Rafin)
echo "</pre>";

echo "<pre>";
//Percorrer um Array (O comando foreach)
$frutas = ["Maçã", "Banana", "Uva"];

foreach ($frutas as $fruta) {
    echo "Fruta: $fruta <br>";
}
echo "</pre>";

/* Concatenação */

$nome = "Rafael";
$sobrenome = "Machado";
echo "<pre>";
//1. Simples
// Unindo as variáveis com um espaço no meio
echo "Nome completo: " . $nome . " " . $sobrenome; 
echo "</pre>";
echo "<pre>";
//2. Interpolação (Dentro de aspas duplas " ")
echo "Olá, $nome $sobrenome! Bem-vindo."; 
echo "</pre>";
echo "<pre>";
//3. Concatenação com Atribuição (.=)
$texto = "Eu estou aprendendo ";
$texto .= "PHP "; // Adiciona ao final da variável anterior
$texto .= "com foco profissional.";

echo $texto; // Resultado: Eu estou aprendendo PHP com foco profissional.
echo "</pre>";