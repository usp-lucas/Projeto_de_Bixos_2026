numeral_a = float(input('Digite um número: ').strip())
numeral_b = float(input('Digite outro número: ').strip())

if numeral_a > numeral_b:
    print(f'O primeiro número é maior que o segundo: \n {numeral_a} > {numeral_b}')
elif numeral_b > numeral_a:
    print(f'O segundo número é maior que o primeiro: \n {numeral_b} > {numeral_a}')
else:
    print(f'Os dois números são iguais: \n {numeral_a} = {numeral_b}')
