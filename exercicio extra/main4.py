import math

print("Informe tres valores numericos")
a=int(input("Digite o primeiro valor: "))
b=int(input("Digite o segundo valor: "))
c=int(input("Digite o terceiro valor: "))

if a>b>c :
    print("O maior numero e: ",a, "O menor numero e",c)

if b>a>c :
    print("O maior numero e: ",b, "O menor numero e",c)

if c>b>a :
    print("O maior numero e: ", c, "O menor numero e", a)

if a>c>b :
    print("O maior numero e: ", a, "O menor numero e", b)

if b>c>a :
    print("O maior numero e: ", b, "O menor numero e", a)

if c>a>b :
    print("O maior numero e: ", c, "O menor numero e", b)
