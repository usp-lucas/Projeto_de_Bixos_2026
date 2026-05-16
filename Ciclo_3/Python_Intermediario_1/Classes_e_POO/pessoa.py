class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def apresentar(self):
        return print(f'Olá meu nome é {self.nome} e tenho {self.idade} anos de idade.')

lucas = Pessoa('Lucas', 19)
lucas.apresentar()
julia = Pessoa('Júlia', 27)
julia.apresentar()