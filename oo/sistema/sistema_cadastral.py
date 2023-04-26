class SistemaCadastral:

    def __cadastrar(self,nome: str, idade:int) -> bool:
        if self.__vericar_dados(nome,idade):
            self.__armazenar_dados(nome,idade)
        else:
            self.__indicar_erro()
    def __verificar_dados(self, nome: str, idade: int) -> bool:
        if isinstance(nome, str) and isinstance(idade, int):
            return True
        else:
            return False

    def __armazenar_dados(self, nome: str, idade:int) -> None:
        print('acessando o banco de dados...')
        print('Cadastrar o Usuario {}, Idade{}'.format(nome,idade))
        
    def __indicar_erro(self) ->None:
        print('dados inválidos')


#teste
sis = SistemaCadastral()
sis.cadastrar('wagner', 18)