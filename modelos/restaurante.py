from modelos.avaliaca import Avaliacao
from modelos.cardapio.iten_cardapio import ItemCardapio

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = False
        self._cardapio = []
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome}|{self.categoria}'

    @property
    def ativo(self):
        return '⌧' if self._ativo else '☐'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {str(restaurante.media_avaliacoes).ljust(25)} | {restaurante.ativo}')

    def alternar_estado(self):
        self._ativo = not self._ativo


    def receber_avaliacao(self, cliente, nota):
        if 0 < nota <= 5:
          avaliacao = Avaliacao(cliente, nota)
          self._avaliacao.append(avaliacao)


    @property
    def media_avaliacoes(self):
        if not self._avaliacao:
         return '-'
        soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
        quantidade_de_notas = len(self._avaliacao)
        media = round(soma_das_notas / quantidade_de_notas, 1)
        return media

    def adicionar_no_cardapio(self,item):
        if isinstance(item, ItemCardapio):
            self._cardapio.append(item)

    def exibir_cardapio(self):

        print(f'\nCardapio do restaurante {self._nome}\n')
        for i,item in enumerate(self._cardapio,start=1):
            if hasattr(item, 'descricao') and not hasattr(item, 'tipo') and not hasattr(item, 'tamanho'):
                mensagem_prato = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao}'
                print(mensagem_prato)
            elif hasattr(item, 'descricao') and hasattr(item, 'tipo') and hasattr(item, 'tamanho'):
                  mensagem_sobremesa = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Descrição: {item.descricao} | Tipo {item.tipo} | Tamanho:{item.tamanho}\n'
                  print(mensagem_sobremesa)
            else:
                 mensagem_bebida = f'{i}. Nome: {item._nome} | Preço: R${item._preco} | Tamanho: {item.tamanho}'
                 print(mensagem_bebida)