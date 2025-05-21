import math
# Exercícios 6.2

# 1. Calcule o resto da divisão de 10 por 3

print(f"o resto de 10/3 é {10%3}")

# 2. Calcule a tabuada do 3

for i in range(1,11):
    print(i*13)

# 3. Calcule quantas aulas Davinir pode faltar sabendo que ele tem 2 aulas por semana durante 4 meses e tendo que comparecer a 75%

aulas_por_semana = 2
semana_por_quatro_meses = 4*4

aulas_total = semana_por_quatro_meses*aulas_por_semana
porcentagem = (75/100)
porcentagem2 = aulas_total*porcentagem
#print(porcentagem)
#print(porcentagem2)
faltas = aulas_total - porcentagem2
print(f"ele tem até {faltas} faltas")

#Calculo de área de um círculo e raio r = 2
r = 2
Ac = math.pi * (r**2)
print(f"O raio é de {Ac:.2f}")

## Expressões numéricas
# 1. Quantos segundos há em 3h, 23min, 17segs?

treshsegs = (60*3)*60
minuto = 60*23
segs = 17
segstotal = treshsegs+minuto+segs

print(segstotal)

# velocidade media (m/s) de 65km em 3h, 23min, 17segs

## convertendo km para m

km = 65
m = 65*1000

## utilizando o código acima, podemos já resolver essa questão:

vm = m/segstotal
print(f"A velocidade média é igual a {vm:.2f} m/s")

# 3. Resolva a expressao (100-413*(20-(5*4)))/(5)

expressao = (100-413*(20-(5*4)))/(5)
print(expressao)

# 4. Capacitores:
## Paralelo
C1 = 10
C2 =22
C3 = 6.8

Cp = (C1 + C2 + C3)
print(F"Capacitores ligados em paralelo {Cp}")

Cs = 1/((1/C1)+(1/C2)+(1/C3))
print(F"Capacitores ligados em série {Cs:.2f}")

# 5.

totalp = 5
totalc = 75*2.50
totalm = 8.73*2
tomate = 3.45
cebola = 5.40*0.42
alho = 30*0.45
paes = 25*0.45

valort = (totalc+totalm+tomate+cebola+alho+paes)/totalp

print(f"O valor total por pessoa é igual a {valort:.2f}")

# 6. ## fazer :P