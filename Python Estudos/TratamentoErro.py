try:
    # Código que pode gerar uma exceção
    pass
except Exception as e:
    # Tratamento da exceção
    print(f"Erro: {e}")
except ValueError as ve:
    # Tratamento específico para ValueError
    print(f"Valor inválido: {ve}")
else:
    # Código que será executado se não ocorrer nenhuma exceção
    print("Código executado com sucesso.")
finally:
    # Código que será executado independentemente de ocorrer uma exceção ou não
    print("Execução finalizada.")

num = -10
if num < 0:
    raise ValueError("O número não pode ser negativo.")
# raise causa a interrupção do programa, então o código abaixo não será executado