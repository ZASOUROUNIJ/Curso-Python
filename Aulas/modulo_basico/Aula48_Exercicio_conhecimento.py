# Testando conhecimentos sobre strings, condicionais e prints
nome = input("Digite o seu nome : ")
idade = input("Digite sua idade: ")
if nome and idade:
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")

    if ' ' in nome:
        print ("Seu nome contém espaços.")
    else:
        print ("Seu nome não contém espaços.")

    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é : {nome[0]}")
    print(f"A última letra do seu nome é : {nome[-1]}")

    print(f"Sua Idade é {idade} anos.")
else:
    print("nome ou idade não informados.")

