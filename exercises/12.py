n1 = int(input("Informe o valor inicial do produto: "))

valordedesconto = n1 * 5 / 100
valorcomdesconto = n1 - valordedesconto

print("O valor inicial foi de {}, o valor a ser descontado será de {}, e o valor final foi de {}".format(
    n1, str(valordedesconto), str(valorcomdesconto)))
