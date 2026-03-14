<?php

/* Banco de Dados */

// Conexão e Manipulação de Banco de Dados (PDO)

//1. Conexão com PDO 
//Você cria um objeto que representa a "ponte" entre o PHP e o Banco de Dados.
//$pdo = new PDO("tipo:host=endereco;dbname=nome", "usuario", "senha");
try {
    $pdo = new PDO("mysql:host=localhost;dbname=meu_banco", "root", "");
    // Ativa o modo de erros para facilitar o estudo
    $pdo->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    //Define o "Modo de Organização" (Traz os dados limpos por nome da coluna)
    $pdo->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
    //PDO::ATTR_ERRMODE: É a "chave" que controla como o PDO deve reagir a erros.
    //PDO::ERRMODE_EXCEPTION: É o "modo de erro" que diz ao PHP: "Se algo der errado no banco, lance uma Exceção (pare o código e mostre o erro detalhado)".
} catch (PDOException $e) {
    echo "Erro na conexão: " . $e->getMessage();
}

//2. Prepared Statements (Segurança contra Invasão)
//Nunca coloque variáveis direto na sua frase SQL (isso evita o famoso SQL Injection). 
// Use "buracos" (parâmetros) e depois preencha-os. 
//Use : antes do nome do campo.

$sql = "INSERT INTO usuarios (nome, email) VALUES (:nome, :email)";
$stmt = $pdo->prepare($sql);//prepare()	Prepara a frase SQL com segurança (antes de enviar).

// "Vincula" os valores aos nomes
$stmt->bindValue(':nome', 'João Silva'); //bindValue()	Troca o :nome pelo valor real (protege o banco).
$stmt->bindValue(':email', 'joao@email.com');

$stmt->execute();//execute()	Manda o comando final para o banco de dados.

//3. Consultar Dados (SELECT)
//Para buscar informações, usamos o fetch (um por um) ou fetchAll (todos de uma vez).

$stmt = $pdo->query("SELECT * FROM usuarios");
$dados = $stmt->fetchAll(); // Retorna um array
//fetchAll() Pega todos os resultados da consulta de uma vez.
foreach($dados as $usuario) {
    echo $usuario['nome'] . "<br>";
}





