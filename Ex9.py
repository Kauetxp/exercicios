a1 = int(input("Digite o valor inicial: "))
n = int(input("Digite a quantidade de termos: "))
q = int(input("Digite a razão: "))
while q < 2:
    q = int(input("A razão deve ser maior ou igual a 2, digite outro valor: "))
    
sn = a1*(q**n -1) / (q-1)
print(sn)