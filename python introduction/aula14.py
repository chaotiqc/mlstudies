# Funcao lambda e map
## forma simplificada de escrever funcoes

def area_quadrado(L):
    area = L**2
    print(area)
area_quadrado(4)

area_quadrado2 = lambda x:print(x**2) ## função de uma forma mais simplificada
area_quadrado2(7)

area_retangulo = lambda b,h: print(b*h)
area_retangulo(4,7)

## Juntando lambda com map temos:
L = [4,5,6,7,11,9,10]
areas = list(map(lambda x:x**2, L))
print(areas)