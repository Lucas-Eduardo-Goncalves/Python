from math import sqrt, pow

ca = float(input("Informe o cateto adjacente: "))
co = float(input("Informe o cateto oposto: "))

res = sqrt((pow(ca, 2) + pow(co, 2)))

print("O valor da hipotenusa é {}".format(res))
