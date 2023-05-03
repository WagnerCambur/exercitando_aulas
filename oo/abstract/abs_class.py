from abc import ABC, abstractmethod
#Orientação a Objetos em Python - Métodos e Classes Abstratas

class AbstractClass(ABC):

    def __init__(self):
        self.atributo = 'Ola Mundo'
    def metodo (self , elemento: str) -> None:
        print(elemento)

    @abstractmethod
    def metodo_abstrato(self) -> None:
        pass