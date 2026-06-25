#Este programa recrea el juego PIEDRA, PAPEL O TIJERAS.
def main():                                                                 #Definimos la función.
    import random as rnd                                                    #Importamos random y sys.
    import sys
    v, p, e = 0, 0, 0                                                       #Definimos las variables v,p,e.
    print('\t\tPIEDRA, PAPEL O TIJERAS')                                    #Título del juego.
    while True:                                                             #Bucle para que siempre sea Verdadero. 
        cpu = rnd.randint(1,3)                                              #Definimos la variable cpu con números pseudo-random.
        print(f'\tVictorias = {v}, Perdidas = {p}, Empates = {e} ')         #Marcador dinámico.
        usuario = input('\tElige (P)IEDRA, P(A)PEL, (T)IJERAS O SALIR\n>')  #Se le pide al usuario qué colocar y se da valor a cada entrada.
        if usuario in ('P','p','piedra', 'PIEDRA'):
            usuario = 1
            print('\tPIEDRA VS...',end = ' ')
        elif usuario in ('A', 'a', 'papel', 'PAPEL'):
            usuario = 2
            print('\tPAPEL VS...',end = ' ')
        elif usuario in ('T', 't', 'TIJERAS', 'tijeras'):
            usuario = 3
            print('\tTIJERAS VS...',end = ' ')
        else:                                                               #Cualquier entrada no reconocida, cerrará el programa.
            print('Bye o/')
            sys.exit()
        if cpu == 1:                                                        #Si se colocó una entrada válida, se da a conocer el valor dado a cpu. 
            print('PIEDRA')
        elif cpu == 2:
            print('PAPEL')
        else:
            print('TIJERAS')

        if usuario == cpu:                                                  #Condicionales. Si el valor ingresado es igual a cpu, empate.
            print('\t¡Empate!')
            e = e + 1
            continue
        elif usuario == 1 and cpu == 3:                                     #Piedra gana a tijeras, tijeras gana a papel y papel gana a piedra.
            print('\t¡Ganaste!')
            v = v + 1
            continue
        elif usuario == 2 and cpu == 1:
            print('\t¡Ganaste!')
            v = v + 1
            continue
        elif usuario == 3 and cpu == 2:
            print('\t¡Ganaste!')
            v = v + 1
            continue
        else:
            print('\tPerdiste :(')                                          #Si es distinto, se pierde.
            p = p + 1
            continue
main()                                                                      #Inicio del programa.
