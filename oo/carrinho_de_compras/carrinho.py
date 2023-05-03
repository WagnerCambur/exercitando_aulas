from produtos import Produto
from typing import Type
#Orientação a Objetos em Python - Agregação de Classes
class CarrinhoDeCompras:
    def __init__(self) -> None:
        self.__produtos = []

    def adicionar_produtos(self, produto: Type[Produto]) ->None:
        self.__produtos.append(produto)

    def finalizar_compra(self) ->None:
        print ('Compras Finalizadas!')

        for produto in self.__produtos:
            produto.informacoes_produto()