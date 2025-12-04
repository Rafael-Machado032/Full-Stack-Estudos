| Camada            | Tecnologia            | Função                                |
|-------------------|-----------------------|---------------------------------------|
| Banco de Dados    | PostgreSQL            | Armazenamento de dados históricos     |
| Back-end          | Python + FastAPI      | Lógica, análise de dados e API REST   |
| Front-end         | React.js + JavaScript | Interface do usuário e interação      |
| Visualização      | Plotly.js             | Renderização dos gráficos interativos |

Etapa 1: Base de dados e API (MVP)
Foco principal: Coletar e disponibilizar dados para o front-end.
1.1. Configurar o back-end: Inicie o projeto Python usando o FastAPI. Instale as bibliotecas requests (para buscar dados) e pandas (para processá-los).
1.2. Integrar com a API de dados: Conecte-se a uma API pública como a CoinGecko API. Busque dados históricos do Bitcoin e informações em tempo real.
1.3. Criar o endpoint de dados: Desenvolva um endpoint na sua API que receba uma solicitação do front-end (ex: GET /api/bitcoin/data) e retorne os dados processados em formato JSON.
1.4. Iniciar o projeto front-end: Crie a estrutura do Next.js. Não se preocupe com o design agora. Use o App Router para criar a página de análise (app/analise/page.tsx).
1.5. Fazer a requisição no front-end: Utilize fetch para consumir o endpoint da sua API Python e exibir os dados brutos na tela (ex: em um console.log).
1.6. Entregar o MVP: Você terá uma aplicação que, ao ser acessada, busca dados do back-end e os exibe.
Etapa 2: Visualização e Dashboard
Foco principal: Apresentar os dados de forma clara e interativa.
2.1. Instalar a biblioteca de gráficos: Instale o Plotly.js no seu projeto Next.js.
2.2. Implementar os gráficos:
Crie um gráfico de velas (candlestick) para visualizar os preços de abertura, fechamento, máxima e mínima.
Crie um gráfico de linha para mostrar o volume de negociação.
2.3. Adicionar indicadores técnicos: No back-end, use a biblioteca TA para calcular indicadores como a Média Móvel (MA) e o Índice de Força Relativa (RSI). Inclua esses dados na resposta da sua API.
2.4. Renderizar os indicadores: No front-end, adicione as linhas dos indicadores aos seus gráficos usando o Plotly.js.
2.5. Ajustar a interface: Utilize um sistema de componentes como o Material UI ou estilize com Tailwind CSS para criar um dashboard visualmente atraente.
Etapa 3: Funcionalidades Adicionais
Foco principal: Adicionar mais valor e interatividade.
3.1. Roteamento dinâmico: Altere a rota de análise para /analise/[cripto], permitindo que o usuário visualize outras criptomoedas além do Bitcoin.
3.2. Análise on-chain: Adicione um novo endpoint no back-end para coletar dados on-chain (como número de transações e endereços ativos) usando uma API de blockchain.
3.3. Tabela de dados: Exiba uma tabela com as informações detalhadas da criptomoeda (preço atual, volume, capitalização de mercado) e com as métricas que você calculou no back-end.
3.4. Otimizar a performance: Implemente estratégias de cache no back-end para evitar requisições repetidas à API externa e otimize a forma como o Next.js carrega os dados.