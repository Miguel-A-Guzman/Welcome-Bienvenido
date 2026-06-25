#Este programa crea un número aleatorio del 1 al 10 y hace que lo adivines. Tienes n intentos.
import random as rnd                                                                #Importamos random para crear números pseudo-aleatorios.

def game():
    secreto = rnd.randint(1, 10)                                                    #Definimos la variable. Cuando comience el juego cambiará de valor.
    n = 6                                                                           #Intentos máximos.
    intento = n
    intentos = 1
    print('Estoy pensando en un número del 1 al 10. Tienes', n, 'intentos.')
    while intento != 0:                                                             #Mientras el intento sea diferente de 0 el juego empieza.
        respuesta = int(input('¿Cuál crees que es el número?: '))                   #Empezamos añadiendo un número.
        if respuesta != secreto:                                                    #Si la respuesta es diferente del secreto, se resta 1 al intento.
            intento = intento - 1
            intentos = intentos + 1            
            print('Ese valor no era.', end = '\n')
            if intento == 0:                                                        #Si se terminan los intentos se rompe el bucle.
                print('Te quedaste sin intentos :(')
                break
            elif secreto < respuesta:                                               #Ayudas por si el número es menor o mayor al colocado.
                print('El número que estoy pensado es menor. Prueba de nuevo.')
            else:
                print('El número que estoy pensado es mayor. Prueba de nuevo.')
            if intento == 1:                                                        #Cuando queda 1 intento y aún no se adivina el número.
                print('Te queda', intento, 'intento')
            else:
                print('Te quedan', intento, 'intentos')
            continue
        elif intento == 1:                                                          #Cuando se acertó faltando 1 intento.
            print('¡Acertaste! Te quedaba', intento, 'intento')
            break
        if intento == n and intentos == 1:                                          #Cuando se acertó a la primera.
            print("¡Acertaste a la primera!")
            break
        else:                                                                       #Acertando con más intentos.
            print('¡Acertaste a los', intentos, 'intentos!')
            break              
    again = input('¿Quieres jugar de nuevo? ')                                      #Reiniciamos el juego según la entrada.
    if again in ('S', 's', 'Sí', 'Si',
                 'si', 'y', 'yes', 'YES',
                 'Yes','claro', 'clarin', 'clarinetes'):
        intento = n                                                                 #Se reestablece el intento y se corre la función de nuevo.
        game()
    else:
        print('Bye o/')                                                             #Cualquier otra cosa, termina el programa.
game()                                                                              #Inicio del programa.
