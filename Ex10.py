i = int(input("Digite o ano que você nasceu: "))

vt = 2023 - i

if vt < 16:
    print("Você não pode votar ainda")
elif vt >=16 and vt <18:
    print("Você já pode votar")
else:
    print("Você é obrigado a votar, vá tirar o seu título agora !")
    

