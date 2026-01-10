## Instalação

    https://dev.mysql.com/downloads/installer/ -> Instalação do servidor
    Recomenda-se a versão completa (offline) de aproximadamente 550 MB.

    https://dev.mysql.com/downloads/workbench/ -> Intalação do gerenciador do Banco de Dados

    Para verificar se esta rodando no CMD execulte:

    ```bash
        net start | findstr /i "mysql"
    ```
    Se aparecer, o servidor esta ativo.
    obs: Nomei o servidor para MySQL_Estudos
    
    **Execultar comandos no CMD**

    Para que o Windows reconheça os comandos do MySQL em qualquer pasta, faça o seguinte: 
    No menu Iniciar, digite "Variáveis de Ambiente" e selecione "Editar as variáveis de ambiente do sistema".
    Clique no botão Variáveis de Ambiente.
    Em "Variáveis do Sistema", localize a variável Path e clique em Editar.
    Clique em Novo e cole o caminho da sua pasta bin (Ex: C:\Program Files\MySQL\MySQL Server 8.0\bin).
    Clique em OK em todas as janelas.
    Importante: Feche o CMD atual e abra um novo para que a alteração funcione.

    **Ativar Servidor**

    No CMD em modo administrador

    ```bash
        net start MySQL_Estudos
    ```
    Não pediu senha

    **Desativar Servidor**

    ```bash
        mysqladmin -u root -p shutdown
    ```
    E depois insira a senha


## Observação Geral

    SQLite É um banco de dados leve, usado para aplicaçoes locais so suporta uma conexao por vez
    MySQL É um banco de dados mais robusto, usado para aplicaçoes web que suportam moitas conexoes simultaneas
    Arquivo com extensão .sql é um arquivo de script SQL
    Arquivo com extensão .db é um arquivo de banco de dados SQLite

    **Criação de tabelas e atributos**

(tipo de dado) _ (nome do campo) _ (nome da tabela)

    tb -> Nome da tabela ex: tb_contato
    n -> Campos numerico ex: n_telefone