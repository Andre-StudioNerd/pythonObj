class Livro:
    livros=[]
    def __init__(self, titulo, autor, paginas):
        self._titulo = titulo
        self._autor = autor
        self.paginas = paginas
        Livro.livros.append(self)

    def __str__(self):
        return f'{self.titulo} | {self.autor} | {self.paginas} páginas'

    @property
    def titulo_autor(self):
        return f'{self.titulo} | {self.autor}'

    def aumentar_paginas(self, quantidade):

        self.paginas += quantidade

    @classmethod
    def listar_livros(cls):
        print(f'{'Nome do livro'.ljust(25)} | {'Autor'.ljust(25)} | {'Páginas'}')
        for livro in cls.livros:
            print(f'{livro._titulo.ljust(25)} | {livro._autor.ljust(25)} | {livro.paginas}')

if __name__=='__main__':

     livro_terror=Livro('Livro Terror','AutorA',100)
     livro_terror.aumentar_paginas(10)
     livro_futuro=Livro('Livro Futuro','AutorB',200)
     print("-"*80)
     print("Listando Livros: ")
     print("-"*80)
     Livro.listar_livros()
     print("-"*80)