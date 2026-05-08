import math
import cmath

while True:
    try:
        a = float(input('Escreva um numeral diferente de zero, para o coeficiente a: '))
        if a == 0:
            print("Erro: o valor deve ser diferente de zero, para ser equação de segundo grau.")
            continue
        b = float(input('Escreva um numero para o coeficiente b: '))
        c = float(input('Escreva um numero para o coeficiente c: '))
        break
    except ValueError:
        print('Valor invalido')

discriminante = b**2 - 4 * a * c

print(f"O discriminante deu o valor: {discriminante}")
if discriminante == 0:
    raiz_real = -b/(2 * a)
    print(f"Raiz real única: {raiz_real: .2f}")
elif discriminante > 0:
    raiz_1 = (-b + math.sqrt(discriminante))/(2 * a)
    raiz_2 = (-b - math.sqrt(discriminante))/(2 * a)
    print(f'Raiz 1: {raiz_1: .2f} e Raiz 2: {raiz_2: .2f}')
elif discriminante < 0:
    raiz_1 = (-b + cmath.sqrt(discriminante))/(2 * a)
    raiz_2 = (-b - cmath.sqrt(discriminante))/(2 * a)
    print(f'Seus coeficientes geraram raizes complexas, Raiz 1: {raiz_1: .2f} e Raiz 2: {raiz_2: .2f}')



