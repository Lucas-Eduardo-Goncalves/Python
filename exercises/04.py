v1 = input("Digite algo: ")

print("O tipo primitivo é", type(v1))
print("Apenas espaços?", v1.isspace())
print("É numérico?", v1.isnumeric())
print("Possui apenas letras?", v1.isalpha())
print("Possui letras ou numeros?", v1.isalnum())
print("Apenas letras maiusculas?", v1.isupper())
print("Apenas letras minusculas?", v1.islower())
print("Está capitalizado?", v1.istitle())