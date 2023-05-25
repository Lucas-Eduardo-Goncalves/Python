# Operadores aritméticos
# Adição           +
# Subtração        -
# Multiplicação    *
# Divisão          /
# Potência         **, pow()
# Divisão inteira  //
# Resto da divisão %
# Raiz Quadrada ** (1/2)

# Ordem de precedência
# 1 - Parentes: ()
# 2 - Exponenciação: **
# 3 - Multiplicação, Divisão, Divisão inteira, Resto da divisão: *, /, //, %
# 4 - Soma, Subtração: +, -

val1 = 5
val2 = 2

print(val1 + val2)
print(val1 - val2)
print(val1 * val2)
print(val1 / val2)
print(val1 ** val2)
print(val1 // val2)
print(val1 % val2)

# Utilidades
print(81**(1/2))
print("="*20)

# Curiosidades
name = input("Digite seu nome: ")
print("Hello word, {:^20}!".format(name))
print("Hello word, {:>20}!".format(name))
print("Hello word, {:<20}!".format(name))

# Formatação
n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))

s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A soma é {}, \n o produto é {} e a divisão é {:.3f}".format(s, m, d), end=" >>> ")
print("Divisão inteira {} e potência {}".format(di, e))
