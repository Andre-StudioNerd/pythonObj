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

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedora')
pessoa3 = Pessoa(nome='Luiz', idade=22)

print('-----------------INICIO DO PROGRAMA------------- ')
print('Lista da empresa')
print('-------------------------------------------------')
print(pessoa1.saudacao)
print(pessoa1.aniversario)
print('-------------------------------------------------')
print(pessoa2.saudacao)
print('-------------------------------------------------')
print(pessoa3.saudacao)
print('-------------------------------------------------')
print('--------------FIM DO PROGRAMA--------------------')
