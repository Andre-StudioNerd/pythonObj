from produtos import Produto

produtos = [
    Produto("chocolate", 3.45),
    Produto("biscoito", 2.49),
    Produto("cafe", 3.45),
    Produto("suco", 4.30),
    Produto("feijao", 10.00),
    Produto("arroz", 8.50)
]



def lista_produtos():
  for produto in sorted(produtos, key=lambda produto: produto.nome,reverse=True):
   print(produto.nome, produto.valor)

if __name__=='__main__':
     lista_produtos()
