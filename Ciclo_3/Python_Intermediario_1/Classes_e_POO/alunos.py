class Alunos:
    def __init__(self, nome, nota1, nota2):
        self.nome = nome
        self.nota1 = nota1
        self.nota2 = nota2
    def calcular_media(self):
        return (self.nota1 + self.nota2) / 2
    def verificar_aprovacao(self):
        media = self.calcular_media()
        return print('Reprovado!') if media < 6 else print('Aprovado!')

joaozinho = Alunos('João', 6, 6)
josezinho = Alunos('José', 4, 2)
joaozinho.verificar_aprovacao()
josezinho.verificar_aprovacao()