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