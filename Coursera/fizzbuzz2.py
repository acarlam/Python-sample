#fizzbuzz2.py
num = int(input("Digite um número inteiro: "))
verifica1 = num % 3
verifica2 = num % 5
if (verifica1 == 0) and (verifica2 == 0):
    print("FizzBuzz")
else:
    print(num)