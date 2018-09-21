import math

n1 = input("Digite o 1° numero: ")
n2 = input("Digite o 2° numero: ")
n3 = input("Digite o 3° numero: ")

def maior():
    if n1 > n2 > n3:
        print("O maior numero e: ", n1, "O menor numero e", n3)
    elif n2 > n1 > n3:
        print (n2,"é o maior numero!!")
    elif n3 > n1 > n2:
        print n3 ("é o maior numero!!")

    #Se alguns numeros forem iguais

    elif n1 == n2 and n1 and n2 > n3:
        print (n1,"e o maior")
    elif n1 == n3 and n1 and n3 > n2:
        print(n1,"é o maior!!")
    elif n2 == n3 and n2 and n3 > n1:
        print (n2,"é o maior!!")
    #todos os numeros iguais
    elif n1 == n2 and n3:
        print ("todos o numeros são iguais")
