# Funcoes
def identificacao(nome,idade):
    print("Olá", nome, "\nSua idade", idade, "anos")

identificacao('Fulano', 65)

def maior(x,y):
    if x<y:
        print("O maior numero é",y)
    elif x == y:
        print("Os numeros sao iguais")
    else:
        print("O maior numero é",x)

maior(21,16)

def pitagoras(cat1, cat2, hip):
    if hip == "?":
        hip=(cat1**2+cat2**2)**(1/2)
        print("A hipotenusa é", hip)
    elif cat1 == "?":
        cat1 = ((hip**2-cat2**2)**(1/2))
        print("O cateto é", cat1)
    elif cat2 == "?":
        cat2 = (hip**2+cat1**2)**(1/2)
        print("O cateto é", cat2)
pitagoras("?", 4, 5)