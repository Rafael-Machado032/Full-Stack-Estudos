import ModuloFuncao1 as M # Importa o módulo ModuloFuncao1 com o alias M
from ModuloFuncao2 import aluno # Importa apenas o dicionário aluno do módulo ModuloFuncao2

M.saudacao("Rafael") # Chama a função saudacao do módulo ModuloFuncao1

print(M.aluno["curso"])

print(aluno["idade"]) # Acessa a idade do aluno importado do ModuloFuncao2