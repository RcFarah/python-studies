# Exercicio #042

# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

seg_a = int(input('Digite o valor do segmento a: '))
seg_b = int(input('Digite o valor do segmento b: '))
seg_c = int(input('Digite o valor do segmento c: '))

if seg_a < seg_b + seg_c and seg_b < seg_a + seg_c and seg_c < seg_a + seg_b:
    print('Esses segmentos podem formar um triângulo!')

    if seg_a == seg_b == seg_c:
        print('Esse é um triangulo EQUILÁTERO!')
    elif seg_a != seg_b != seg_c != seg_a:
        print('Esse é um triângulo ESCALENO!')
    else:
        print('Esse é um triângulo ISÓSCELES!')
else:
    print('Esses segmentos não podem formar um triângulo...')
