while True:
    try:
        valor = float(input("Digite um valor positivo, em metros: "))
        if valor < 0:
            print("Valor invalido")
            continue
        break
    except ValueError:
        print("Valor invalido")
        exit()
conversao = valor * 3.28
print(f'Seu valor em metros {valor}m, será convertido para pés utilizando 2 casas decimais.')
print(f'Seu valor em pés: {conversao: .2f}ft')

