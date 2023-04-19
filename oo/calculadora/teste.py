from calculadora import Calculadora
# Exercitando encapsulamento 
# Elementos privados

calculadora = Calculadora()
resultado_soma = calculadora.calcular("+", 8, 4)
resultado_subtrair = calculadora.calcular("-", 10, 5)
print(resultado_soma)
print(resultado_subtrair)