class Livro:
    def __init__(
        self,
        titulo: str,
        autor: str,
        ano: int
    ) ->  None:
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.disponivel = True

    def __str__(self) -> str:
        return (
            f"Título: {self.titulo}\n"
            f"Autor: {self.autor}\n"
            f"Ano: {self.ano}\n"
            f"Disponível: {self.disponivel}"
        )

    def emprestar(self) -> None:
        if not self.disponivel:
            raise ValueError("O livro já está emprestado.")
        self.disponivel = False

    def devolver(self) -> None:
        if self.disponivel:
            raise ValueError("O livro já está disponível.")

        self.disponivel = True