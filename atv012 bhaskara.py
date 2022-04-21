from math import pow

a = float(input("Qual é o valor de a? "))
b = float(input("Qual é o valor de b? "))
c = float(input("Qual é o valor de c? "))

#print("A equação é: ({}) * x ** 2 + ({}) * x + ({})".format(a, b, c))

delta = b * b - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
elif delta == 0:
    raiz = (-b + pow(delta, 1 / 2)) / 2 * a
    print("a raiz desta equação é {}".format(raiz))
else:
    x = (-b + pow(delta, 1 / 2)) / 2 * a
    y = (-b - pow(delta, 1 / 2)) / 2 * a
    if x < y == y or y < x == x:
        print("as raízes da equação são {:.2f} e {:.2f}".format(x, y))