import math
print("Calculo da Distancia entre dois pontos A(x1,y1) e B(x2,y2)")

px1 = int(input("Digite o valor do ponto x1 de A: "))
py1 = int(input("Digite o valor do ponto y1 de A: "))
px2 = int(input("Digite o valor do ponto x2 de B: "))
py2 = int(input("Digite o valor do ponto y2 de B: "))
distancia = math.sqrt ((px1-px2)**2+(py1-px2)**2)
print("Distancia entre dois pontos,", distancia)
