cateto_a = float(input('Digite a medida do cateto a: ').strip())
cateto_b = float(input('Digite a medida do cateto b: ').strip())
cateto_c = float(input('Digite a medida do cateto c: ').strip())

if cateto_a < cateto_b + cateto_c and cateto_b < cateto_a + cateto_c and cateto_c < cateto_a + cateto_b:
    if cateto_a == cateto_b == cateto_c:
        print('Seu triângulo é equilatero.')
    elif cateto_a == cateto_b != cateto_c or cateto_b == cateto_c != cateto_a or cateto_a == cateto_c != cateto_b:
        print('Seu triângulo é isósceles.')
    elif cateto_a != cateto_b != cateto_c:
        print('Seu triângulo é escaleno.')
else:
    print('Os valores não formam um triângulo válido.')
    
  