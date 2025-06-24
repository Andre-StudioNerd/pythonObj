class Produto():
  def __init__(self, nome, valor, quantidade):
   self.__nome = nome
   self.__valor = valor
   self.__quantidade = quantidade

  def __repr__(self):
   return self.__nome

  @property
  def nome(self):
    return self.__nome

  @property
  def valor(self):
   return self.__valor

  @property
  def quantidade(self):
   return self.__quantidade

  def acrescentar_valor(self, acrescimo):
        self.__valor += acrescimo

  @property
  def impressao(self):
    return f"nome: {self.__nome} | valor: {self.__valor} | quantidade: {self.__quantidade}"