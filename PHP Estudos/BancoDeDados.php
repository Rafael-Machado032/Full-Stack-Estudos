<?php

/* Banco de Dados */

// Conexão e Manipulação de Banco de Dados (PDO)

//PADRÃO SINGLETON PARA CONEXÃO
//Abrir a porta do banco uma única vez e usar essa mesma porta em todo o seu site. 
// Se você der new PDO em dez arquivos diferentes, o servidor pode ficar lento ou travar.

//1. Classe de Conexão Profissional (Singleton)
// Criamos um atributo static para segurar a conexão e um método static para entregá-la.
//EX: Arquivo Conn.php

namespace App\Database;

use PDO;
use PDOException;
class Conn {
    private static $connect = null;

    public static function getConn() {
        // Se a conexão não existe, eu crio. Se já existe, eu só devolvo a mesma.
        if (self::$connect == null) {
            try {
                
                $dsn = "mysql:host=localhost;dbname=meu_banco;charset=utf8";
                //Você cria um objeto que representa a "ponte" entre o PHP e o Banco de Dados.
                //$pdo = new PDO("tipo:host=endereco;dbname=nome", "usuario", "senha");
                self::$connect = new PDO($dsn, "root", "");
                
                // Ativa o modo de erros para facilitar o estudo
                self::$connect->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
                //PDO::ATTR_ERRMODE: É a "chave" que controla como o PDO deve reagir a erros.
                //PDO::ERRMODE_EXCEPTION: É o "modo de erro" que diz ao PHP: "Se algo der errado no banco, lance uma Exceção (pare o código e mostre o erro detalhado)".
   
                //Define o "Modo de Organização" (Traz os dados limpos por nome da coluna)
                self::$connect->setAttribute(PDO::ATTR_DEFAULT_FETCH_MODE, PDO::FETCH_ASSOC);
                
            } catch (PDOException $e) {
                die("Erro crítico na conexão: " . $e->getMessage());
            }
        }
        return self::$connect;
    }
}

//2. Como usar no seu projeto?

use App\Database\Conn;

// Pega a conexão (ele cria ou reaproveita a existente)
$pdo = Conn::getConn();

$stmt = $pdo->query("SELECT * FROM usuarios");
$lista = $stmt->fetchAll();


//2. Prepared Statements (Segurança contra Invasão)
//Nunca coloque variáveis direto na sua frase SQL (isso evita o famoso SQL Injection). 
// Use "buracos" (parâmetros) e depois preencha-os. 
// --- PARTE 1: WHITELIST (Segurança da Estrutura/Coluna) ---
$colunaUsuario = $_GET['campo'] ?? 'nome'; // O que vem da URL
$permitidos = ['nome', 'email', 'cidade']; // Minha lista de confiança

// Se o que o usuário mandou não está na lista, travo no 'nome'
$colunaSegura = in_array($colunaUsuario, $permitidos) ? $colunaUsuario : 'nome';


// --- PARTE 2: PREPARED STATEMENT (Segurança do Dado/Valor) ---
$busca = $_GET['busca'] ?? ''; // O que o usuário quer procurar

// Monto a query usando a variável da Whitelist e o "buraco" (:) para o valor
$sql = "SELECT * FROM usuarios WHERE $colunaSegura LIKE :termo";

$stmt = $pdo->prepare($sql);

// O BindValue limpa o texto contra SQL Injection
$stmt->bindValue(':termo', "%$busca%"); 
$stmt->execute();

$resultados = $stmt->fetchAll();


//TRASAÇÕES NO PDO: Tudo ou Nada
// Elas garantem que um conjunto de comandos só seja gravado se todos derem certo. 
// Se um falhar, o PHP desfaz tudo o que foi feito antes (o famoso Rollback).

//1. Os 3 Comandos Mágicos
//$pdo->beginTransaction(): "Inicia o cronômetro". O banco para de gravar as alterações permanentemente e guarda numa "memória temporária".
//$pdo->commit(): "Confirma". Grava tudo o que foi feito de uma vez só no HD do banco.
//$pdo->rollBack(): "Cancela". Joga fora tudo o que foi feito desde o início da transação (volta ao estado original).

try {
    // 1. Inicia a transação
    $pdo->beginTransaction();

    // 2. Executa as operações (ex: Transferência)
    $pdo->exec("UPDATE contas SET saldo = saldo - 100 WHERE id = 1");
    $pdo->exec("UPDATE contas SET saldo = saldo + 100 WHERE id = 2");

    // 3. Se chegou aqui sem erro, GRAVA DEFINITIVO!
    $pdo->commit();
    echo "Transferência realizada com sucesso!";

} catch (Exception $e) {
    // 4. Deu erro? DESFAZ TUDO para não sumir dinheiro!
    $pdo->rollBack();
    echo "Erro na transação: " . $e->getMessage();
}

//ERROS PROFICIONAIS: Exibição vs. Log (Segurança)
//O erro comum é deixar o PHP mostrar o erro técnico (com nomes de pastas e senhas) na tela do site. 
// O profissional esconde o erro do usuário e o salva em um arquivo secreto no servidor para o programador ler depois.
//Desenvolvimento (Sua máquina): Você quer ver o erro completo para consertar.
//Produção (Site no ar): Você mostra uma mensagem educada e guarda o "erro feio" num arquivo .log.

try {
    $pdo = App\Database\Conn::getConn();
    $stmt = $pdo->query("SELECT * FROM tabela_que_nao_existe");

} catch (\PDOException $e) {
    // 1. SALVAR NO LOG (Arquivo secreto no servidor)
    // O 3 significa "salvar em um arquivo específico"
    $mensagem = "[" . date('Y-m-d H:i:s') . "] Erro: " . $e->getMessage() . " no arquivo " . $e->getFile() . PHP_EOL;
    error_log($mensagem, 3, "erros_banco.log");

    // 2. MOSTRAR AO USUÁRIO (Mensagem amigável)
    echo "Desculpe, tivemos um problema técnico. Nossa equipe já foi notificada.";
    
    // Opcional: Enviar e-mail para o admin aqui
}

