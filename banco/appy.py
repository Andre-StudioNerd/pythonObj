from agencia import Agencia
from banco import MeuBanco


banco_A=MeuBanco("Banco A","Rua Nova")
agencia_B=Agencia("Agência B","Rua Velha",11)

def main():
    print(banco_A)
    print(agencia_B)

if __name__ == '__main__':
    main()