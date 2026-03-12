# 📂 Configuração do Ambiente PHP Profissional (2024/2025)

Este documento registra os passos para configurar um ambiente PHP moderno sem depender de instaladores "tudo-em-um" como o XAMPP.

## 1. Instalação do PHP (Manual)
- **Versão:** PHP 8.5 (Thread Safe)
- **Local:** `C:\PHP`
- **Configuração:**
  - Renomeia o arquivo `php.ini-development ` para `php.ini`.
  - **Path do Windows:** Adicionado `C:\PHP` às Variáveis de Ambiente do Sistema.

## 2. Ajustes no `php.ini` (O "Cérebro")
Ative as seguintes extensões (removendo o `;`):
- `extension_dir = "ext"` (Diretório de extensões)
- `extension=curl` (Requisições HTTP)
- `extension=mbstring` (Manipulação de texto)
- `extension=openssl` (Segurança/SSL)
- `extension=pdo_mysql` (Conexão com Banco de Dados)
- `extension=zip` (Descompactação de pacotes pelo Composer)

## 3. Gerenciador de Dependências (Composer)
- **Instalação:** Instale usando `Composer-Setup.exe` apontando para o binário em `C:\PHP\php.exe`.
- **Comando de Teste:** `composer --version`.
- **Função:** Permite instalar blibiotecas (ex: Carbon, Laravel).

## 4. Comando Execução
- **Via Console** `php nome-do-arquivo.php`
- **Via Navegador** Dentro da pasta execulta o comando `php -S localhost:8000`
