from livro import Livro

livro = Livro("Dom Casmurro", "Machado de Assis", 1899)

print(f'Titulo: {livro.titulo}')
print(f'Autor: {livro.autor}')
print(f'Ano: {livro.ano}')
print(f'Disponível: {livro.disponivel}')

livro.emprestar()
print(livro.disponivel)

livro.devolver()
print(livro.disponivel)