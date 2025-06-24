class Produto:
    def __init__(self, nome, valor):
        self.__nome = nome
        self.__valor = valor

    def __repr__(self):
        return f"nome:{self.__nome} valor:{self.__valor}"

    @property
    def nome(self):
        return self.__nome

    @property
    def valor(self):
        return self.__valor
