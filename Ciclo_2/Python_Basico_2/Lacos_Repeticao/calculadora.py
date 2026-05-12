while True:
    print('###########################\n' \
          '### Calculadora Simples ###\n' \
          '###########################\n' \
          '#a. Soma                  #\n' \
          '#b. Subtração             #\n' \
          '#c. Multiplicação         #\n' \
          '#d. Divisao               #\n' \
          '#e. Sair do Programa      #\n' \
          '###########################\n')
    escolha_usuario = str(input('Escolha uma opção (a~e): \n').lower().strip())
    if escolha_usuario == 'e':
        print('Encerrando o programa\n')
        break
    num_1 = float(input('Digite um número: \n'))
    num_2 = float(input('Digite um número: \n'))
    
    if escolha_usuario == 'a':
        resultado = num_1 + num_2
        print('Sua escolha de operação foi de soma\n' \
              f'{num_1} + {num_2} = {resultado}\n')
    
    elif escolha_usuario == 'b':
        resultado = num_1 - num_2
        print('Sua escolha de operação foi de subtração\n' \
              f'{num_1} - {num_2} = {resultado}\n')
    
    elif escolha_usuario == 'c':
        resultado = num_1 * num_2
        print('Sua escolha de operação foi de multiplicação\n' \
              f'{num_1} * {num_2} = {resultado}\n')
    
    elif escolha_usuario == 'd':
        if num_2 != 0:
            resultado = num_1 / num_2
            print('Sua escolha de operação foi de divisão\n' \
                f'{num_1} / {num_2} = {resultado}\n')
        else:
            print('ERRO: Divisão por zero\n')

