def entrada_de_respostas(tamanho_valido):
    while True:
        entrada_aluno = input('\nEntre apenas com 10 respostas, separadas por espaço cada uma: ').split()        
        if len(entrada_aluno) != tamanho_valido:
            print(f'Você entrou com {len(entrada_aluno)} respostas, são esperadas {len(tamanho_valido)} respostas.')
            continue
        return entrada_aluno

gabarito = ['A', 'B','C','D','A','D','D','B','C','A']

entrada_de_respostas_aluno = entrada_de_respostas(len(gabarito))

acertos = 0


for g in range(len(gabarito)):
    if gabarito[g] == entrada_de_respostas_aluno[g]:
        acertos += 1

print(f'\nVocê obteve {acertos} acertos.\n')
