
from typing import Type

# # SOLID (L) - Princípio da Substituição de Liskov

class PessoaA:
    def se_apresentar(self):
        print('Ola, sou a pessao A')

class PessoaB(PessoaA):

    def __init__(self):
        super().__init__()

    def se_apresentar(self):
        print('Estou alterando esse metodo')

#teste1
pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()



# class Animal:
#     def comer(sef):
#         print('O animal esta Comendo')

#     def dormir(sef):
#         print('O animal esta Dormindo')

#     def andar(sef):
#         print('O animal esta anadando na Jaula')

# class Aves(Animal):
#     def __init__(self):
#         super().__init__()
#     def cantar(sef):
#         print('O ave esta cantando')

# class Pinguim(Aves):
#     def __init__(self):
#         super().__init__()
#     def escorregar(sef):
#         print('O Pinguim esta escorregando no gelo')
    
# class Pessoa:
#     def observar(sef, animal :Type[Animal]):
#         animal.comer()
# #teste2
# wagner = Pessoa()
# pinguim = Animal()
# pinguim2 = Aves()
# wagner.observar(pinguim)
# wagner.observar(pinguim2)