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

musica_nova=Musica('Nova','Cantor',4)
musica_outra=Musica('Outra','Cantora',3)

Musica.listar_musicas()

