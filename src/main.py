from livro import Livro

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("O Hobbit", "J. R. R. Tolkien", 1937)
livro4 = Livro("Harry Potter", "J. K. Rowling", 1997)

biblioteca = [
    livro1,
    livro2,
    livro3,
    livro4
]

programa_ligado = True

while programa_ligado:

    print("\n####### MENU #######")
    print("[1] - Listar livros")
    print("[2] - Procurar livro")
    print("[3] - Emprestar livro")
    print("[4] - Sair")
    print("####################")

    opcao = input("Opção: ")

    if opcao == "1":

        print("\n=== CATÁLOGO ===\n")

        for livro in biblioteca:
            print(livro)
            print()

    elif opcao == "2":

        titulo_procurado = input(
            "\nDigite o título do livro: "
        )

        livro_encontrado = False

        for livro in biblioteca:

            if (
                livro.titulo.lower().strip()
                ==
                titulo_procurado.lower().strip()
            ):

                livro_encontrado = True

                print("\nLivro encontrado!\n")
                print(livro)

                break

        if not livro_encontrado:
            print("\nLivro não encontrado.")

    elif opcao == "3":

        titulo_procurado = input(
            "\nDigite o título do livro: "
        )

        livro_encontrado = False

        for livro in biblioteca:

            if (
                livro.titulo.lower().strip()
                ==
                titulo_procurado.lower().strip()
            ):

                livro_encontrado = True

                try:
                    livro.emprestar()
                    print("\nLivro emprestado com sucesso!")

                except ValueError as erro:
                    print(f"\nErro: {erro}")

                break

        if not livro_encontrado:
            print("\nLivro não encontrado.")

    elif opcao == "4":

        programa_ligado = False
        print("\nPrograma finalizado.")

    else:

        print("\nOpção inválida.")