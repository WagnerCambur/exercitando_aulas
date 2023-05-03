from produtos import Produto
from carrinho import CarrinhoDeCompras

#Orientação a Objetos em Python - Agregação de Classes
#Testando

car = CarrinhoDeCompras()
monitor = Produto('Monitor', 1000)
cerveja = Produto('Cerveja', 6)
mouse = Produto('Mouse', 80)
car.adicionar_produtos(monitor)
car.adicionar_produtos(cerveja)
car.adicionar_produtos(mouse)
car.finalizar_compra()
