def calcular_media(valor_1, valor_2, valor_3):
    media_aritmetica = (valor_1 + valor_2 + valor_3) / 3
    return media_aritmetica

nota_1 = float(input('Digite um valor para a primeira nota: ').strip())
nota_2 = float(input('Digite um valor para a segunda nota: ').strip())
nota_3 = float(input('Digite um valor para a terceira nota: ').strip())

media = calcular_media(nota_1, nota_2, nota_3)

print('O valor da média aritmética entre as notas:\n' \
      f'{nota_1}, {nota_2} e {nota_3}\n'
      f'foi: {media}')