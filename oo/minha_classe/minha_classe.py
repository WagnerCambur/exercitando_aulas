#variaveis e metodos de classe

class Loja:
    tarifa = 1.10
    def __init__(self,endereco) ->None:
        self.__endereco = endereco
    def apresentar_endereco(self) -> None:
        print(self.__endereco)
    @classmethod
    def vender(cls) ->int:
        return 40 *cls.tarifa
    @classmethod
    def alterar_tarifa(cls, nova_tarifa: int) ->None:
        cls.tarifa = nova_tarifa

#testando 

loja_praia = Loja('PRAIA')
loja_centro = Loja('CENTRO')

loja_praia.apresentar_endereco()

print(loja_praia.vender())
print(loja_centro.vender())

loja_centro.apresentar_endereco()
loja_centro.alterar_tarifa(1.80)

print(loja_praia.vender())
print(loja_centro.vender())




