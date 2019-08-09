#teste_classe.py

class Veiculo:

    def __init__(self, nome, cor, valor):
        self.nome = nome
        self.cor = cor
        self.valor = valor
    

    def descricao(self):
        return f"Carro: {self.__class__}, Cor: {self.cor}, Valor: {self.valor}, Nome: {self.nome}"
    
class Bug(Veiculo):
    pass    
    
    
class Conversivel(Veiculo):
    pass   


if __name__ == '__main__':
    carro1 = Bug('Troller', '50mil', 'Azul')
    carro2 = Conversivel('Ferrari', '60mil', 'vermelho')
    print(carro1.descricao())
    print(carro2.descricao())    
