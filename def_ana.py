#primer def
def verCadena(cadena):
    for i in lista:
        print(i)
        cadena+=str(i)+coma
    return cadena

#segundo def
def listInversa(lista):
    lista.sort(reverse=True)
    lista2=lista
    return lista2

#tercer def
def menu(lista):
    menu = int(input("Selecciona \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu> 2:
        print('Digitar numero del 1 al 2 unicamente')
        menu = int(input("Selecciona \n 1. Para buscar en la lista \n 2. Para salir\n"))

    while menu == 1:
        letra = input("Introduce la palabra para buscar en lista: ")
        for i in lista:
            if i == letra:
                print('Es igual ')
            else:
                print('no es igual')
        menu = int(input("Selecciona \n 1. Para buscar en la lista \n 2. Para salir\n"))

    if menu == 2:
        print('Vuelve pronto')

#cuarto def
def contar(lista):
    letra = input("Introduce palabra que este dentro de lista para contar sus silabas: ")
    for i in lista:
        if i == letra:
            verd=len(i)
            print(f'{verd}')
        else:
            print(f"NULL")

#base
lista=['Ana','Maria','Abril','Echeverry','Daniel','Alejandro','Fierro','Espinosa','Basbuni','Gripa']
cadena=""
coma=","

print("\n El programa mostrara en una variable la lista \n")

cadena =verCadena(cadena)
print(f"{cadena}")

print("\n Se imprimira la lista en de manera desendente alfabeticamente \n")

lista2 =listInversa(lista)
print(f"{lista2}")

#La lista al buscarla queda ordenada de mayor a menor Z a A
print("\n El programa dirá si ese nombre esta dentro de la lista \n")

menu(lista)

print("\n El programa contará las silabas \n")

contar(lista)

print("Termino el programa")


 

