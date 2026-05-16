LADOS_LARGURA = LADOS_ALTURA = 2
class Retangulo:

    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        print(self.largura * self.altura)
        return self
    def calcular_perimetro(self):
        print(self.largura * LADOS_LARGURA + self.altura * LADOS_ALTURA)
        return self
    
retangulo_1 = Retangulo(2, 3)
retangulo_2 = Retangulo(3, 4)
retangulo_1.calcular_area().calcular_perimetro()
retangulo_2.calcular_area().calcular_perimetro()