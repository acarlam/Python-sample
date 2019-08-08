#Circulo.py
from math import pi

class Circulo:
    def __init__(self, raio):
        self.raio = raio


    def area(self):
        Total_Area = ((self.raio**2) * pi)
        return Total_Area

    def perimetro(self):
        p = 2 * pi * self.raio
        return p


if __name__ == '__main__':
    circulo = Circulo(4)
    area = circulo.area()
    perimetro = circulo.perimetro()
    print(f"Area",round (area,2))
    print(f"Perimetro",round(perimetro,2))