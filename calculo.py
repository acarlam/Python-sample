#calculo.py
class Retangulo:
    def __init__(self, altura , largura):
        self.altura = altura
        self.largura = largura


    def calculo(self):
        resultado = (self.altura * self.largura)
        return resultado

