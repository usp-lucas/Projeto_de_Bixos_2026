num_user = int(input('Escreva um número inteiro positivo: ').strip())
num_menor = 0
while True:
    if num_menor < num_user:
        print(num_menor)
        num_menor += 1
    if num_menor == num_user:
        print(num_menor)
        break