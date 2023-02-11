h = float(input("Digite sua altura: "))
s = int(input("Qual é seu sexo?\n1:Masculino -- 2:Feminino\n"))
while s != 1 and s != 2:
    s = int(input("Digite um valor válido:\n"))
if s == 1:
    p = (72.7 * h)- 58
    print("Seu peso ideal é:",p,"Kg")
elif s == 2:
    p = (62.1 * h)- 44.7
    print("Seu peso ideal é:",p,"Kg")

