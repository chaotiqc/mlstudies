import math
# Exercicios 7.6:
## 1. Supondo que o dólar esteja em R$ 3.25, salve esse valor em uma variável e utilize-o para calcular quanto você teria ao cambiar R$65.00 para doláres

dolar = 3.25
valortdolar = 65.00*3.25
print(valortdolar)

## 2.

p1 = 8.66
p2 = 5.35
p3 = 5
p4 = 1

ma = (p1+p2+p3+p4)/4
print(f"{ma:.2f} é a media aritmetica")
mg =(p1*p2*p3*p4)**(1/4)
print(f"{mg:.2f} é a media geometrica")
mh = ((4)/((1/p1)+(1/p2)+(1/p3)+(1/p4)))
print(f"{mh:.2f} é a media harmonica")

# 3.
celular = 299.99
chaleira = 23.87
gnomo = 66.66
adesivost = 1.42*6
frete = 12.34

## a
valortdolar1 = celular+chaleira+gnomo+adesivost+frete

## b

valortreal = valortdolar1*dolar

## c