print('Vetor 1:')
vetor_1 = [float(elem) for elem in input('Escreva valores numéricos separados por espaço: ').split()]
print('Vetor 2:')
vetor_2 = [float(elem) for elem in input('Escreva valores numéricos separados por espaço: ').split()]
op_desejada = input('Qual operação deseja realizar? (s/m) ').lower().strip()

if op_desejada == 's':
    vetor_soma = [vetor_1[i] + vetor_2[i] for i in range(len(vetor_1))]
    print(f'A soma {vetor_1} + {vetor_2}, tem como resultado:\n'
          f'{vetor_soma}')
    
elif op_desejada == 'm':
    escalar = float(input('Digite um valor escalar: ').strip())
    vetor_1_escalado = [escalar * vetor_1[i] for i in range(len(vetor_1))]
    vetor_2_escalado = [escalar * vetor_2[i] for i in range(len(vetor_2))]
    print('As multiplicações escalares resultaram:\n' \
          f'{escalar} * {vetor_1} = {vetor_1_escalado}\n'
          f'{escalar} * {vetor_2} = {vetor_2_escalado}\n')
        
