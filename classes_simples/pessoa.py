class Pessoa:
    pessoas=[]
    def __init__(self, nome, idade, profissao=None):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
        Pessoa.pessoas.append(self)

    def __str__(self):
        return f'{self.nome}, {self.idade} anos, {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome} e trabalho como {self.profissao}.\nEu tenho {self.idade} anos.'

        else:
            return f'Olá, sou {self.nome} e não trabalho aqui.'
    @property
    def aniversario(self):
        self.idade += 1
        return f'Eu faço {self.idade} anos no próximo mês.'



if __name__=='__main__':

   pessoa_nova = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
   pessoa_antiga = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedora')
   pessoa_desconhecida = Pessoa(nome='Luiz', idade=22)

   print('-----------------INICIO DO PROGRAMA------------- ')
   print('Lista da empresa')
   print("-"*80)
   print(pessoa_nova.saudacao)
   print(pessoa_nova.aniversario)
   print("-"*80)
   print(pessoa_antiga.saudacao)
   print("-"*80)
   print(pessoa_desconhecida.saudacao)
   print("-"*80)
   print('--------------FIM DO PROGRAMA !-------------------')
