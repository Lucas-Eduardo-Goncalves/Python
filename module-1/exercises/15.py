n1 = float(input("Quantos dias o carro foi alugado? "))
n2 = float(input("Quantos kilometros foram rodados? "))

calc = n1 * 60 + n2 * 0.15

print("O valor a ser pago é de R${:.2f}".format(calc))