from banco import MeuBanco

class Agencia(MeuBanco):
    def __init__(self, nome, endereco, numero):
        super().__init__(nome, endereco)
        self._numero = numero

    def __str__(self):
         return f'{self._nome}| {self._endereco} | nº {self._numero}'






