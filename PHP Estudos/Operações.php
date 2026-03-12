<?php
/* Calculos */

//1. Basico
$a = 10;
$b = 3;

echo $a + $b;  // Soma: 13
echo "<br>";
echo $a - $b;  // Subtração: 7
echo "<br>";
echo $a * $b;  // Multiplicação: 30
echo "<br>";
echo $a / $b;  // Divisão: 3.333...
echo "<br>";
echo $a % $b;  // Módulo (Resto da divisão): 1
echo "<br>";
echo $a ** $b; // Exponenciação (10 elevado a 3): 1000
echo "<br>";

//2. Atribuição
$total = 100;
$total += 20; // $total agora é 120 (Soma e guarda)
$total -= 10; // $total agora é 110 (Subtrai e guarda)
$total *= 2;  // $total agora é 220 (Dobro)

//3. Fuçõens Nativas
// round(): Arredonda para o mais próximo.
// ceil(): Arredonda sempre para cima (teto).
// floor(): Arredonda sempre para baixo (chão).
// number_format(): A mais importante! Formata dinheiro.

$valor = 10.4;
$preco = 1250.758;

// 1. ROUND: O "equilibrado" (0.5 pra cima vira 11, abaixo disso vira 10)
echo "Round (10.4): " . round($valor); // Resultado: 10
echo "<br>";
echo "Round (10.6): " . round(10.6);   // Resultado: 11

echo "<br>";
// 2. CEIL: O "teto" (não importa o decimal, ele joga pra cima)
// Muito usado para calcular páginas: "Tenho 11 itens, cabem 10 por página, preciso de 2 páginas"
echo "Ceil (10.1): " . ceil(10.1);     // Resultado: 11

echo "<br>";
// 3. FLOOR: O "chão" (ignora o decimal e mantém o inteiro)
// Útil para calcular idades ou descontos onde você não quer arredondar pra cima
echo "Floor (10.9): " . floor(10.9);   // Resultado: 10

echo "<br>";
// 4. NUMBER_FORMAT: O "Rei do E-commerce" (Transforma número em dinheiro)
// Estrutura: number_format(valor, casas_decimais, 'separador_decimal', 'separador_milhar')
$total_venda = 5432.10;
echo "R$ " . number_format($total_venda, 2, ',', '.'); 
// Resultado: R$ 5.432,10

/* Operadores */
// 1. Comparação (Testes lógicos)

// Usados dentro do if para testar condições.
// ==   -> Igual a (valor)
// ===  -> Idêntico a (valor e tipo - Use sempre este!)
// !=   -> Diferente de
// !==  -> Não idêntico a
// >    -> Maior que / < : Menor que
// >=   -> Maior ou igual / <= : Menor ou igual

// 2. Lógicos (Combinar condições)

// Usados para unir dois ou mais testes no mesmo IF.
// && (AND) -> Só é verdadeiro se TUDO for verdade.
// || (OR)  -> É verdadeiro se PELO MENOS UM for verdade.
// ! (NOT)  -> Inverte o valor (se era true, vira false).

// 3. Especiais (Nível Sênior)
// ??  -> Coalescência Nula (Define um valor padrão se a variável não existir).
// ? : -> Ternário (Um if/else curto de uma linha só).

echo "<br>";
/* Condição */

//1. IF e IF ELSE
$hora = 14;

if ($hora < 12) {
    echo "Bom dia!";
} elseif ($hora < 18) {
    echo "Boa tarde!"; // Este será o resultado
} else {
    echo "Boa noite!";
}

echo "<br>";
//2. Ternario
$status = "pago";
echo ($status == "pago") ? "✅ Acesso Liberado" : "❌ Bloqueado";

echo "<br>";
//3. SWITCH
$corFavorita = "azul";

switch ($corFavorita) {
    case "vermelho":
        echo "Você escolheu vermelho.";
        break;
    case "azul":
        echo "Você escolheu azul.";
        break;
    default:
        echo "Cor não encontrada.";
}

/* Looping */

//1. FOR
for ($i = 1; $i <= 5; $i++) {
    echo "Contagem: $i <br>";
}

//2. FOREACH
$tecnologias = ["PHP", "Next.js", "Docker", "MySQL"];

foreach ($tecnologias as $item) {
    echo "Estudando: $item <br>";
}

//3. WHILE
$contador = 1;
while ($contador <= 3) {
    echo "Tentativa $contador <br>";
    $contador++; // Cuidado: se esquecer isso, o PC trava (loop infinito)!
}

//4. DO WHILE
$i = 10;
do {
    echo "Isso vai aparecer uma vez, mesmo 10 não sendo menor que 5.";
    $i++;
} while ($i < 5);

//5. Controles de loop
//break: Para o loop imediatamente (ex: "Achei o que queria, pode parar").
$nomes = ["Rafin", "João", "Ana", "Bia", "Carlos"];
$procurar = "Ana";

foreach ($nomes as $nome) {
    echo "Verificando: $nome <br>";

    if ($nome === $procurar) {
        echo "✅ Achei a $procurar! Parando a busca... <br>";
        break; // O PHP sai do loop IMEDIATAMENTE aqui
    }
}
echo "Fim da execução.";

//continue: Pula para a próxima repetição, ignorando o que vem abaixo dele no momento
for ($i = 1; $i <= 10; $i++) {
    // Se o número for 5, eu quero pular ele
    if ($i === 5) {
        echo "⚠️ Número 5 detectado! Pulando para o próximo... <br>";
        continue; // Ignora o 'echo' abaixo e volta para o topo do loop (pro 6)
    }

    echo "Número atual: $i <br>";
}
