lista = [1, 7, 14, 15, 19, 24, 32, 56]
def soma_lista(lista_dada, indice_inicial):
    
    if indice_inicial == len(lista_dada) - 1:
        return lista_dada[indice_inicial]
    
    return lista_dada[indice_inicial] + soma_lista(lista_dada, indice_inicial + 1)

resultado_soma = soma_lista(lista, 0)

print('A soma dos elementos da lista:\n' \
        f'{lista}\n' \
        f'é: {resultado_soma}' )