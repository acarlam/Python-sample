#bhaskara.py Carla Alexandra Martins
import math
a = float(input("Entre acom A: "))
b = float(input("Entre acom B: "))
c = float(input("Entre acom C: "))

# 1° Calcular o delta 
delta = float((b**2) - 4 * a * c)

if delta > 0:
    x1 = float((-b + math.sqrt(delta))/(2 * a))
    x2 = float((-b - math.sqrt(delta))/(2 * a))
    print("Raiz X1",x1," e raiz x2 é ",x2) 
elif delta == 0: 
    x1 = float((-b / (2 * a)))
    print("Raiz x1 = x2",x1)
else: 
    print("Não possui raizes reais!")