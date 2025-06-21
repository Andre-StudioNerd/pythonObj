class Musica:
    musicas=[]
    def __init__(self,nome,artista,duracao):
        self.nome=nome
        self.artista=artista
        self.duracao=duracao
        Musica.musicas.append(self)

    def __str__(self):
        return f'{self.nome} | {self.artista} |{self.duracao}'

    def listar_musicas():
        for musica in Musica.musicas:
            print(f'{musica.nome} | {musica.artista} | {musica.duracao}')

if __name__=='__main__':

    musica_nova=Musica('Nova','Cantor',4)
    musica_outra=Musica('Outra','Cantora',3)
    print("-"*80)
    print("Listando Músicas:")
    print("-"*80)
    Musica.listar_musicas()
    print("-"*80)

