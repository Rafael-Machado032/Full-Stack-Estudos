<?php
// Exibindo o formulário via PHP (usando aspas simples para o HTML interno)
echo "
<h3>Teste de Formulário Profissional</h3>
<form method='POST' action=''>
    <label>Nome:</label><br>
    <input type='text' name='usuario' placeholder='Digite seu nome'><br><br>
    
    <label>Senha (Invisível no POST):</label><br>
    <input type='password' name='senha'><br><br>
    
    <button type='submit'>Enviar via POST</button>
    <a href='?acao=limpar' style='margin-left:10px;'>Limpar via GET</a>
</form>
<hr>
";

// 1. Lógica do POST (Geralmente usada para Cadastros/Login)
if ($_SERVER['REQUEST_METHOD'] === 'POST') { //Testa o method enviado
    $usuario = trim($_POST['usuario'] ?? ''); //Se não vier nada assume string vazia
    $senha = $_POST['senha'] ?? '';

    if (!empty($usuario) && !empty($senha)) {// os dois tem que ser diferente que vazio
        echo "✅ Dados recebidos via POST! Usuário: <strong>$usuario</strong>";
        // No profissional, aqui você salvaria no Banco de Dados (MySQL)
    } else {
        echo "❌ Preencha todos os campos.";
    }
}

// 2. Lógica do GET (Geralmente usada para buscas ou links)
if (isset($_GET['acao']) && $_GET['acao'] === 'limpar') { //isset() verifica se existe a chave no url
    echo "♻️ Você clicou em um link GET. O sistema foi 'limpado'.";
}

/* Cookies e Sessões */

//1. Cookies
// Os cookies são pequenos arquivos de texto armazenados no computador do usuário (navegador). 
// Eles são úteis para guardar preferências (como tema escuro/claro) que duram mesmo após o navegador ser fechado.

//setcookie(nome, valor, expiração, caminho);

// Criar um cookie chamado "usuario" que vale por 1 hora (3600 segundos)
setcookie("usuario", "João", time() + 3600, "/");

// Ler o cookie
if(isset($_COOKIE["usuario"])) {
    echo "Bem-vindo, " . $_COOKIE["usuario"];
}

//2. Sessões (Sessions)
// As sessões armazenam dados no servidor. 
// São mais seguras que cookies e muito usadas para sistemas de login, 
// pois os dados somem quando o usuário fecha o navegador (ou após um tempo de inatividade).

// session_start(); (Deve ser a primeira coisa no código, antes de qualquer HTML)
// $_SESSION["chave"] = "valor";

// Iniciar a sessão
session_start();

// Gravar dados
$_SESSION["usuario_id"] = 123;
$_SESSION["perfil"] = "admin";

// Ler dados em outra página
echo "ID do usuário logado: " . $_SESSION["usuario_id"];

//Ex avançado:

session_start(); // Sempre inicie para poder manipular

// 1. Limpa as variáveis na memória
session_unset();

// 2. Destrói a sessão no servidor
session_destroy();

// 3. Opcional: Apaga o cookie de sessão no navegador (Garante 100%)
if (ini_get("session.use_cookies")) {
    $params = session_get_cookie_params();
    setcookie(session_name(), '', time() - 42000,
        $params["path"], $params["domain"],
        $params["secure"], $params["httponly"]
    );
}

// 4. Redireciona para o login
header("Location: login.php");
exit();
?>

