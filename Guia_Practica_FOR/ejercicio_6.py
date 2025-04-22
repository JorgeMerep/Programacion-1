#6.Imprimir los números múltiplos de 3 entre el 1 y el 10.


for multiplos_de_tres in range (1, 11):
    if multiplos_de_tres % 3 == 0:
        print(f'{multiplos_de_tres} es multiplo de 3, ', end="")
