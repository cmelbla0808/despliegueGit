nombre = input("Introduce tu nombre: ")
valor = 8

'''
    Comentar de conflicto yo que sé
'''

#Comentario de una linea
def hola(nombre_recibido) :
    if valor < 4:
        print("Hola")
    elif  valor >= 4 and valor < 9:
        print("Adios")
    else:
        print("Buenos días")

    print("Hola mundo " + nombre_recibido)
    return 1

hola(nombre)