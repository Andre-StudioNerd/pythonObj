class Carro:
    carros=[]
    def __init__(self,modelo,cor, ano):
        self.modelo=modelo
        self.cor=cor
        self.ano=ano
        Carro.carros.append(self)


    def __str__(self):
        return f'{self.modelo} |{self.cor} |{self.ano}'

    def listar_carros():
       for carro in Carro.carros:
           print(f'{carro.modelo} | {carro.cor} |{carro.ano}')

if __name__=='__main__':

     carro_hilux=Carro('Hilux','Prata',2009)
     carro_onix=Carro('Onix','Branco',2014)
     print("-"*30)
     print("Listando Carros: ")
     print("-"*30)
     Carro.listar_carros()
     print("-"*30)
