linhas = int(input('Digite a quantidade de linhas da matriz: '))

colunas = int(input('Digite a quantidade de colunas da matriz: '))


matriz = list()
for c in range(1, linhas + 1):
    linha = list()
    for i in range(1, colunas + 1):
        while True:
            try:
                valor = int(input(f'Digite o {i}º elemento da {c}ª linha: '))
                break
            except:
                print('Valor INVÁLIDO! Digite apenas valores inteiros!')
        linha.append(valor)
    matriz.append(linha)

print(f'A matriz gerada foi: {matriz}')

matriz_id = [[0] * colunas for i in range(linhas)]
for i in range(linhas):
    for j in range(colunas):
        if i == j:
            matriz_id[i][j] = 1
e_identidade = False
if linhas == colunas:
    for i in range(linhas):
        for j in range(colunas):
            if matriz_id[i][j] != matriz[i][j]:
                e_identidade = False
            else:
                e_identidade = True
                break
if e_identidade == True:
    print(f'Sua matriz {matriz} é a matriz identidade.')
else:
    print(f'A matriz fornecida não é a matriz identidade para as dimensões {linhas}x{colunas}')