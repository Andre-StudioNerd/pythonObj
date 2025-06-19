class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria,capacidade,nota_avaliacao):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.capacidade = capacidade
        self.nota_avaliacao = nota_avaliacao
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} |{self.ativo} |{self.capacidade} |{self.nota_avaliacao}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome} | Categoria: {restaurante.categoria} | Situação: {restaurante.ativo} | Capacidade: {restaurante.capacidade} pessoas |Nota: {restaurante.nota_avaliacao}')

class Cliente:
    clientes=[]
    def __init__(self, nome, idade, email, telefone):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.telefone = telefone
        Cliente.clientes.append(self)

    def __str__(self):
        return f'{self.nome}|{self.idade}|{self.email}|{self.telefone}'

    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'Nome: {cliente.nome} | Idade: {cliente.idade} | Email: {cliente.email} | Telefone: {cliente.telefone}')

restaurante_praca = Restaurante('Sabor da Praça', 'Gourmet',100,10)
restaurante_pizza = Restaurante('Pizza Express', 'Italiana',50,8)
cliente1=Cliente('Alice',23,'Email@email.com','11111')
cliente2=Cliente('Pedro',31,'Email@email.com.br','11111222')

print("Listar Restaurantes")
Restaurante.listar_restaurantes()
print("Listar Clientes")
Cliente.listar_clientes()