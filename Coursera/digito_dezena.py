#digito_dezena.py
numero = input("Digite um número inteiro: ")
unidade = int(numero) % 10
resulta = (int(numero) - int(unidade)) // 10
dezena = int(resulta) % 10  
if dezena != 0:
    print("O dígito das dezenas é ",dezena)
else:
    print("O dígito das dezenas é 0")