import urllib.request # Bibilioteca para fazer requisições WEB
import sys # Biblioteca para manipulação do sistema
import io # Biblioteca para manipulação de fluxos de entrada e saída

url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

requisicao = urllib.request.Request(url)
# Cria um objeto de requisição
requisicao.add_header('User-Agent', 'Mozilla/5.0')
# A wikipedia bloqueia se não for acessado pelo navegador
# Então adicionamos um cabeçalho para simular um navegador do mozila
pagina = urllib.request.urlopen(requisicao)
# Abre a URL e pega o conteúdo da página

texto = pagina.read().decode("utf-8")
# Lê o conteúdo da página e decodifica para UTF-8

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# Configura a saída padrão para UTF-8 (para evitar erros com caracteres especiais)

posicao_inicio = texto.find("Brazil")
# Divide o texto em linhas

print(posicao_inicio)