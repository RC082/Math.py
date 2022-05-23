from time import sleep
print("[1] Adição")
print("[2] Subtração")
print("[3] Multiplicação")
print("[4] Divisão")
sleep(0.5)
escolha1 = int(input("Digite aqui: "))
if escolha1 == (1):
    adi1 = int(input("Digite Seu Primero Número: "))
    adi2 = int(input("Digite Seu Segundo Número: "))
    s = adi1 + adi2 
    print("Resultado: {}".format(s))

if escolha1 == (2):
    sub1 = int(input("Digite Seu Primero Número: "))
    sub2 = int(input("Digite Seu Segundo Número: "))
    s = sub1 - sub2 
    print("Resultado: {}".format(s))

if escolha1 == (3):
    mul1 = int(input("Digite Seu Primero Número: "))
    mul2 = int(input("Digite Seu Segundo Número: "))
    s = mul1 * mul2 
    print("Resultado: {}".format(s))

if escolha1 == (4):
    div1 = int(input("Digite Seu Primero Número: "))
    div2 = int(input("Digite Seu Segundo Número: "))
    s = div1 / div2 
    print("Resultado: {}".format(s))