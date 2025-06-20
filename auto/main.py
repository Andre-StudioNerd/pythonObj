from classes.carro import Carro

carro_ford = Carro(marca="Ford", modelo="Focus", cor="Preto")
carro_chevrolet = Carro(marca="Chevrolet", modelo="Cruze", cor="Prata")
carro_honda = Carro(marca="Honda", modelo="Civic", cor="Vermelho")


def main():
    print(f"Carro 1: {carro_ford.marca} {carro_ford.modelo}, Cor: {carro_ford.cor}")
    print(f"Carro 2: {carro_chevrolet.marca} {carro_chevrolet.modelo}, Cor: {carro_chevrolet.cor}")
    print(f"Carro 3: {carro_honda.marca} {carro_honda.modelo}, Cor: {carro_honda.cor}")
    carro_honda.ligar()

if __name__=="__main__":
    main()



