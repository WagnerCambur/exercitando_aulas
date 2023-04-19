# Exercitando encapsulamento 
# Elementos privados

class Calculadora:
    def calcular(self,operacao,num1,num2):
        if operacao == "+":
            return self.__adicionar(num1,num2)
        elif operacao == "-":
            return self.__subtrair(num1,num2)
        else:
            print("Operação Iválida")
    def __adicionar(self,num1,num2):
        return num1 + num2
    def __subtrair(self, num1,num2):
        return num1 - num2