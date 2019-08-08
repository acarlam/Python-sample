#lista_menores.py

a = [1,1,2,3,5,8,13,21,34,55,89]

def lista_menores10(lista):
    # codigo
    for elemento in lista:
        if elemento < 10:
            print("Mostra", elemento)
        else:
            print("Não mostrar")


if __name__ == "__main__":
    lista_menores10(a)