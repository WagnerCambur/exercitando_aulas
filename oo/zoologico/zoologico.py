
from typing import Type

# SOLID (L) - Princípio da Substituição de Liskov
class Animal:
    def comer(sef):
        print('O animal esta Comendo')

    def dormir(sef):
        print('O animal esta Dormindo')

    def andar(sef):
        print('O animal esta anadando na Jaula')

class Aves(Animal):
    def __init__(self):
        super().__init__()
    def cantar(sef):
        print('O ave esta cantando')

class Pinguim(Aves):
    def __init__(self):
        super().__init__()
    def escorregar(sef):
        print('O Pinguim esta escorregando no gelo')
    
class Pessoa:
    def observar(sef, animal :Type[Animal]):
        animal.comer()
#teste
wagner = Pessoa()
pinguim = Animal()
pinguim2 = Aves()
wagner.observar(pinguim)
wagner.observar(pinguim2)