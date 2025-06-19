from agencia import Agencia
from banco import MeuBanco


banco1=MeuBanco("Banco A","Rua Nova")
agencia1=Agencia("Agenc B","Rua Velha",11)

def main():
    print(banco1)
    print(agencia1)

if __name__ == '__main__':
    main()