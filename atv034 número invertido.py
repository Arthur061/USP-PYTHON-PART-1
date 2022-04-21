sequencia = []

while True:
    n = int(input('Digite um número: '))

    if n == 0:
        break

    sequencia.append(n)

for i in reversed(sequencia):
    print(i)