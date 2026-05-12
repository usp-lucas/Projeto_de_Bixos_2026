nomes_alunos = {
    'João' : 5.0, 
    'Paulo': 3.0, 
    'Pedro': 2.2, 
    'Marcos': 4.5, 
    'Lucas': 10.0, 
    'Maria': 6.2, 
    'Ana': 9.3, 
    'Júlia': 1.5, 
    'Bruna': 4.5, 
    'Bruno': 8.2,
    'Gustavo' : 5.0, 
    'Hugo': 3.0, 
    'Clara': 2.4, 
    'Jefferson': 4.5, 
    'Vitória': 5.0, 
    'Cláudia': 6.8, 
    'Matheus': 9.1, 
    'Vânia': 1.2, 
    'Sérgio': 4.3, 
    'Regina': 8.1,
    }
nome = input('VERIFICAÇÃO DE NOTAS DA P1 DE CÁLCULO\n' \
             'Digite um nome válido, com acento: ').capitalize().strip()
if nome in nomes_alunos:
    nota = nomes_alunos[nome]
    print(f'A nota do(a) aluno(a) {nome} foi: {nota}')
else:
    print('Nome não está no banco de dados, verifique acentuação.')