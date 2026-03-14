<?php
/* Programação Orientada a Objetos*/

//1. Basico
//Sintax de orientação objeto
class NomeDaClasse {
    public $atributo; // Característica

    public function metodo() { // Ação
        // código aqui
    }
}

//Ex:

class Carro {
    public $cor;
    public $modelo;

    public function buzinar() {
        return "Beep Beep!";
    }
}

// Criando um Objeto (Instanciar)
$meuCarro = new Carro();
$meuCarro->cor = "Vermelho";
$meuCarro->modelo = "Ferrari";

echo $meuCarro->buzinar(); // Saída: Beep Beep!

//2. Construction

// Ele roda automaticamente assim que você cria o objeto (new). 
// Serve para já "nascer" com dados.
class Usuario {
    public $nome;

    // O construtor recebe o nome na hora do 'new'
    public function __construct($nomeDigitado) {
        $this->nome = $nomeDigitado;
    }
}

$user = new Usuario("João"); 
echo $user->nome; // Já exibe "João"


//Termo 	O que é?
// class	Define o molde.
// new	    Cria o objeto real.
// ->	    Acessa um atributo ou método do objeto.
// $this    Referece a ao mesmo objeto
// public	É o padrão. Qualquer um pode acessar ou alterar o atributo/método de fora da classe..
// private  Segurança Máxima. Só a própria classe
/* static   Ele pertence à Classe e não ao Objeto. Você não precisa usar o new para usá-lo
    Sintaxe: public static $contador;
    Acesso: Usa-se NomeDaClasse::metodo() (os dois pontos duplos ::).*/

//3. Modificadores de Acesso e Restrição de Classes

// HERANÇA
// Permite que uma classe (Filha) herde todas as características e comportamentos de outra (Pai). 
// Evita repetir código.
// class Filha extends Pai { ... }

class Animal {
    public function comer() { return "Comendo..."; }
}

class Cachorro extends Animal {
    public function latir() { return "Au Au!"; }
}

$toto = new Cachorro();
echo $toto->comer(); // Herdado do Pai
echo $toto->latir(); // Próprio da Filha

// PROTECTED (Protegido)
// Ninguém de fora vê, mas os filhos conseguem ver.
// protected $nome;
 class Pai {
    protected $sobrenome = "Silva";
}
class Filho extends Pai {
    public function dizerNome() {
        return "João " . $this->sobrenome; // Funciona! (é herdeiro)
    }
}
$f = new Filho();
// echo $f->sobrenome; // ERRO! (Acesso externo proibido)

//FINAL
// A palavra final serve para "travar" uma classe ou um método. 
// Se uma classe é final, ela não pode ter filhos (não pode ser estendida).
// final class Nome { ... }
final class Seguranca {
    // Ninguém pode dar "extends" nesta classe
}
// class Hacker extends Seguranca { } // ERRO FATAL!

// ABSTRAÇÃO, REFERÊNCIA E MEMBROS DE CLASES
//1. Classes e Métodos Abstratos (abstract)
// Uma classe abstrata é um "rascunho" que não pode ser instanciado (você não pode dar new nela). 
// Ela serve apenas para ser herdada.
// abstract class Nome { ... }
abstract class Conta {
    public $saldo;
    // Todo mundo que herdar "Conta" É OBRIGADO a ter o método sacar
    abstract public function sacar($valor); 
}
class ContaCorrente extends Conta {
    public function sacar($valor) {
        $this->saldo -= $valor + 2; // Regra específica aqui
    }
}

//2. self:: vs $this->
// Enquanto o $this aponta para o objeto (o carro específico), o self aponta para a classe (o molde)
// $this->  Usa para atributos e métodos normais.
// self::   Usa para atributos e métodos estáticos (static) ou constantes.
class Contador {
    public static $total = 0;
    public function __construct() {
        self::$total++; // Mexe na variável da CLASSE, não do objeto
    }
}
//3. Constantes de Classe (const)
//Diferente de variáveis, constantes não mudam de valor e são sempre acessadas como se fossem estáticas (com ::).
class Config {
    const BANCO = "MySQL";
}
echo Config::BANCO; // Acesso direto sem 'new'

//4. Parent (parent::)
//Usado quando o "filho" quer chamar um método do "pai" que ele mesmo acabou de sobrescrever.
class Pai1 {
    public function oi() { return "Olá!"; }
}
class Filho1 extends Pai1 {
    public function oi() {
        return parent::oi() . " Tudo bem?"; // Pega o do pai e aumenta
    }
}

//INTERFACES O Contrato de Comportamento

//1. Interface (interface)
//É um molde 100% abstrato. 
// Ela só contém a assinatura dos métodos (o nome e os parâmetros), sem código dentro.
//interface NomeDaInterface { ... }
interface Notificacao {
    public function enviar($mensagem); // Sem as chaves { }
}

//2. Implementação (implements)
//É a palavra-chave que você usa na classe para dizer que ela vai seguir as regras daquela interface.
//class MinhaClasse implements NomeDaInterface { ... }
// O "Contrato"
interface Animal1 {
    public function fazerSom();
}
// A Classe que "Assina o Contrato"
class Cachorro1 implements Animal1 {
    public function fazerSom() {
        return "Au Au!";
    }
}
class Gato implements Animal1 {
    public function fazerSom() {
        return "Miau!";
    }
}

//NAMESPACE: As Pastas Virtuais do Código
// O Namespace resolve o problema de nomes repetidos. 
// Imagine que você tem duas classes chamadas Cliente: uma para o Banco de Dados e outra para a API externa.
// obs: Arquivos separados pois o php não permite 
// Sem o Namespace, o PHP daria erro. Com ele, você as separa em "caixas" diferentes.

//1. Namespace (namespace)
//Define em qual "pasta virtual" aquela classe está. 
//Deve ser sempre a primeira linha do arquivo PHP.
//obs:"O seu Namespace deve espelhar as suas Pastas Reais."
//namespace NomeDaPasta;
namespace App\Model; // "Pasta" virtual

class Usuario {
    public $nome = "João";
}
//segundo arquivo
namespace app\Service;
class Usuario {
    public $nome = "Maria";
}

//2. Use (use)
//Serve para "importar" ou chamar uma classe que está em outro Namespace para o arquivo atual. 
// É como dar um "atalho".
//use NomeDaPasta\Classe;
namespace App;

use App\Model\Usuario; // Importa a classe específica

$u = new Usuario();
echo $u->nome;

//3. Apelidos (as)
//Se você precisar usar duas classes com o mesmo nome no mesmo arquivo, você dá um "apelido" para uma delas.

use app\Service\Usuario as UsuarioExterno; // Apelidou para não dar conflito

$u1 = new Usuario();
$u2 = new UsuarioExterno();

//4. A Barra Invertida Global (\)
//Se você estiver dentro de um Namespace e quiser usar uma função nativa do PHP (como a classe DateTime), 
// às vezes é bom usar a \ na frente para o PHP saber que ela está na "raiz" (fora de qualquer pasta).
$data = new \DateTime();


