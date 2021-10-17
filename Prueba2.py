import random

cont = 0
opcion = None


def multiplicacion(a, b):
    return a * b


while opcion != 0:
    print(' - APRENDE A MULTIPLICAR HDTPM -'.center(100, '.'))
    try:
        print('1. Iniciar juego')
        print('0. Salir del juego')
        opcion = int(input('Selecciona tu respuesta: '))

        while opcion == 1:
            a = random.randint(1, 10)
            b = random.randint(1, 10)
            r = int(input(f'¿Cuánto es {a}*{b}?: '))
            if r == multiplicacion(a, b):
                print('Correcto. =D')
                cont += 1
            else:
                print('Correcton\'t. La respuesta era: ', multiplicacion(a, b))
                print(f'Tu puntuación fue de: {cont}')
                break

    except Exception as e:
        print(f'Ocurrió un error: {e}')
        print(f'Vuelve a ingresar un número correcto')
        opcion = None

else:
    print('\nSaliendo del juego....')
