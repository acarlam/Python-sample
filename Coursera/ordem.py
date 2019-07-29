#ordem.py
rec1 = int(input("Recebe 1º: "))
rec2 = int(input("Recebe 2º: "))
rec3 = int(input("Recebe 3º: "))
if (rec1 < rec2) and (rec2 < rec3):
    print("Crescente !")
else:
    print("não está em ordem crescente")