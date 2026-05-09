print('Quantas pernas tem uma aranha?' \
      '\na. 8 Pernas' \
      '\nb. 6 Pernas' \
      '\nc. 1 googol de pernas' \
      '\nd. Nenhuma perna')

resposta_usuario = input('Digite uma das alternativas como resposta: ').lower().strip()

if resposta_usuario == 'a':
    print('Parabéns! Sua resposta está correta.')
else:
    if resposta_usuario == 'c':
        print('Mermão... Complicado, viu!')
    else:
        print('Resposta incorreta!')