#lista_print.py

a = [1,1,2,3,5,8,13,21,34,55,89]

def lista_menores10(lista):
    lista_menores10 = []
    for elemento in lista:
        if elemento < 10:
            lista_menores10.append(elemento)
    print("Mostra", lista_menores10)
        
if __name__ == "__main__":
    lista_menores10(a)