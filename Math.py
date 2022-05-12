from time import sleep

sleep(1)
print("Olá Sejá Bem Vindo!")
sleep(1)
print("Eu Fiz Essa Tool Para Testar Meus Conhecimentos.")
sleep(1)
nome1 = str(input("Qual o seu nome?: ")).capitalize()
sleep(1)
print("Sejá Bem Vindo {}".format(nome1))
sleep(1)
escolha1 = str(input("Vocẽ Quer Fazer Calculos De Adição(A) Ou Subtração(S): ")).upper()
sleep(1)
print("Carregando...")
sleep(2)
if escolha1 == ("A"):
    numero1 = int(input("Esolha O Seu Primeiro Numéro: "))
    sleep(1)
    numero2 = int(input("Esolha O Seu Segundo Numéro: "))
    s = numero1 + numero2
    sleep(1)
    print("Calculando Resultados...")
    sleep(2)
    print("A Soma de {} + {} = {}".format(numero1,numero2,s))
if escolha1 == ("S"):
    numero1 = int(input("Esolha O Seu Primeiro Numéro: "))
    sleep(1)
    numero2 = int(input("Esolha O Seu Segundo Numéro: "))
    s = numero1 - numero2
    sleep(1)
    print("Calculando Resultados...")
    sleep(2)
    print("A Subtração de {} - {} = {}".format(numero1,numero2,s))
