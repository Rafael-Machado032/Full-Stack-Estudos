import urllib.request # Bibilioteca para fazer requisições WEB

url = "https://www.google.com/finance/quote/BTC-USD?sa=X&sqi=2&ved=2ahUKEwjfnLHftpuSAxVCqZUCHUW9KXQQ-fUHegQIDBAd"

requisicao = urllib.request.Request(url)
# Cria um objeto de requisição
requisicao.add_header('User-Agent', 'Mozilla/5.0')
# A sites bloqueia se não for acessado pelo navegador
# Então adicionamos um cabeçalho para simular um navegador do mozila
pagina = urllib.request.urlopen(requisicao)
# Abre a URL e pega o conteúdo da página

texto = pagina.read().decode("utf-8")
# Lê o conteúdo da página e decodifica para UTF-8

posicao_inicio = texto.find("YMlKec fxKbKc")
# Peguei a classe que contém o preço do bitcoin
# posicao_inicio recebe a posição do primeiro caractere
preco = texto[posicao_inicio+15:posicao_inicio+24]
# pega a posição inicial e final do preço

print(f"Preço do Bitcoin: {preco}")