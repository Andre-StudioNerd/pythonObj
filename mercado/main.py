from produtos import Produto

produtos = [
    Produto("Arroz", 10.5, 100),
    Produto("Feijao", 6.5, 80),
    Produto("Refrigerante", 3.0, 120),
    Produto("Cafe", 5.45, 75),

]

def lista_estoque(produtos):
    print("Todos os produtos:")
    for produto in produtos:
        print(produto.impressao)
        print('*'* 80)


def pouco_estoque(produtos):
    poucas_qtd = []
    print("\nProdutos com pouco estoque:")
    print("-"*80)
    for produto in produtos:
        if(produto.quantidade < 80):
         poucas_qtd.append(produto)
    print (poucas_qtd)
    print("-"*80)

def adicionar_produto(produtos):
     for produto in produtos:
        if produto.valor < 10:
            valor_antigo = produto.valor
            produto.acrescentar_valor(produto.valor * 0.10)
            print(f"{produto.nome} | R$ {valor_antigo:.2f} | Novo Valor -> R$ {produto.valor:.2f}")


if __name__=='__main__':
    lista_estoque(produtos)
    pouco_estoque(produtos)
    adicionar_produto(produtos)
