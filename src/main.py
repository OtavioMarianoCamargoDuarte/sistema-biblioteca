from livro import Livro

livro = Livro("Dom Casmurro", "Machado de Assis", 1899)

print(livro)

try:
    livro.emprestar()
    print("Livro emprestado com sucesso!")

    livro.emprestar()
    print("Livro emprestado com sucesso!")

except ValueError as erro:
    print(f"Erro: {erro}")