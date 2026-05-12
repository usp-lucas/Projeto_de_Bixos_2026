while True:
    try:
        valor_celsius = float(input('Digite um valor em graus Celsius: '))
        break
    except ValueError:
        print('Valor inválido')
        continue

valor_kelvin = valor_celsius + 273.15
valor_fahrenheit = (valor_celsius * (9/5)) + 32

print(f'Seu valor, {valor_celsius: .2f}ºC, será convertido para kelvin e para fahrenheit.')
print(f'Valor em kelvin: {valor_kelvin:.2f}K;'
      f'\nValor em fahrenheit: {valor_fahrenheit: .2f}°F.')