num_user = int(input('Digite um número inteiro e positivo: ').strip())
qntd_primos = 0

while num_user > 1:
    e_primo = True
    num_aux = num_user - 1    
    while num_aux > 1:
        if num_user % num_aux == 0:
            e_primo = False
            break
        num_aux -= 1
    if e_primo == True:
        qntd_primos += 1
    num_user -= 1
print(f'A sequência de números apresenta {qntd_primos} números primos, até o valor inserido pelo usuário.')