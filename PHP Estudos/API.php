php<?php

//📚 Consumo de Dados: cURL e Web Services

//1. O que é cURL?

//É uma biblioteca que permite ao PHP enviar e receber dados de outros sites. 
// Ele funciona em 4 passos básicos: Iniciar, Configurar, Executar e Fechar.

$url = "https://viacep.com.br";

// 1. Inicia a conexão
$ch = curl_init($url);

// 2. Configura (Diz que quer o resultado como string, não exibir direto)
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true); // Resultado como string
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false); // Pula validacao SSL se der erro

// 3. Executa e guarda a resposta
$resposta = curl_exec($ch);

// 4. Fecha a conexão
curl_close($ch);

// Agora usa o que aprendeu de JSON:
$dados = json_decode($resposta, true);
echo "Logradouro: " . $dados['logradouro'];

// curl_init(): Abre o "telefone".
// curl_setopt(): Disca o número e define as regras (se quer retorno, se envia senha, etc).
// curl_exec(): Faz a ligação e ouve a resposta.
// curl_close(): Desliga o telefone (importante para não gastar memória).


//2. Web Services (REST vs SOAP)

// Existem dois tipos principais de "conversas" entre sistemas:
// REST (O Moderno): Usa JSON e os métodos HTTP (GET, POST, PUT, DELETE). É o que você usará em 99% dos casos hoje.
// SOAP (O Antigo/Bancário): Usa XML e é muito mais rígido e pesado. No PHP, usa-se a classe SoapClient.

// No cURL, você precisa dizer o que quer fazer no Web Service:
// Método	Ação	No cURL
// GET	Buscar dados (Padrão)	    CURLOPT_HTTPGET (Não precisa escrever pois ja intende o padrão)
// POST	Enviar/Criar dados	        CURLOPT_POST
// PUT	Atualizar dados	            CURLOPT_CUSTOMREQUEST, "PUT"
// DELETE	Apagar dados	        CURLOPT_CUSTOMREQUEST, "DELETE"

//📚 Enviando um POST com cURL

// 1. O que você quer enviar (Dados do "Formulário")
$dados = [
    "nome"  => "Marcos Silva",
    "email" => "marcos@email.com",
    "plano" => "Premium"
];

// 2. Inicia o cURL com a URL de destino
$ch = curl_init("https://api.meusistema.com");

// --- CONFIGURAÇÕES ESSENCIAIS ---

// Retorna o resultado como string (Não imprime na tela)
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

// Pula a verificação de SSL (Útil se estiver no Laragon/Localhost)
curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

// --- CONFIGURAÇÕES DE ENVIO (O POST) ---

// Ativa o modo POST (O "Verbo")
curl_setopt($ch, CURLOPT_POST, true);

// Envia os dados (A "Carga")
// Dica: http_build_query organiza o array para o formato que o PHP entende melhor
curl_setopt($ch, CURLOPT_POSTFIELDS, http_build_query($dados));

// 3. Executa a chamada e guarda a resposta
$resposta = curl_exec($ch);

// 4. Fecha a conexão (Opcional no PHP 8+)
curl_close($ch);

// 5. TRATANDO O RESULTADO
$resultado = json_decode($resposta, true);

if (isset($resultado['id'])) {
    echo "Sucesso! Cliente cadastrado com ID: " . $resultado['id'];
} else {
    echo "Erro ao cadastrar cliente.";
}

