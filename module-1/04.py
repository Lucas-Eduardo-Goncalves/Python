# Módulos
# Python já vem com algumas bibliotecas instaladas, porém que não são importadas, alguns exemplos são:

# Math `math`
# Alguns exemplos:
# - ceil (arredondar para cima)
# - floor (arredondar para baixo)
# - trunc (remover numeros após a virgula)
# - pow (calcular potencia)
# - sqrt (calcular raiz quadrada)
# - factorial (calcular fatorial)

from math import sqrt
from random import random, randint
from emoji import emojize

number = int(input("Digite um numero: "))
square_root = sqrt(number)

random_float_number = random()
random_int_number = randint(1, 10)

print(square_root)
print(random_float_number)
print(random_int_number)
print(emojize(":thumbs_up:"))
