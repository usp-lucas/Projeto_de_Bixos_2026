vetor = []
print('##########################################################################\n' \
      '############# Inserção dos valores das coordenadas de um vetor ###########\n' \
      '##########################################################################\n')
entrada_usuario = input('\nInsira valores númericos, separados por espaço cada um: ').split()
escalar = float(input('Escreva um número para a multiplicação escalar: '))
vetor_escalado = []
for i in range(len(entrada_usuario)):
    entrada_usuario[i] = int(entrada_usuario[i])
    vetor.append(entrada_usuario[i])
    coord_escalada = escalar * vetor[i]
    vetor_escalado.append(coord_escalada)
print('Multiplicação por escalar:           \n' \
      f'{escalar} * {vetor} = {vetor_escalado}')