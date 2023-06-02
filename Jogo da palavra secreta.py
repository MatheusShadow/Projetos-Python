palavra_secreta = 'flash'
t = ''
tentativas = 0
print('Bem vindo ao jogo de adivinhar a palavra secreta!')
while True:
    letra_user = input('Digite uma letra: ')

    if len(letra_user) != 1:
        print('Digite uma letra válida!')
        continue
    if letra_user in palavra_secreta:
        t += letra_user
        print(f'A letra {letra_user} está na palavra secreta!')

    if letra_user not in palavra_secreta:
        tentativas += 1
        print(f'A letra {letra_user} não está na palavra secreta!')
        print(f'Erros {tentativas}x')

    t2 = ''
    for y in palavra_secreta:
        if y in t:
            t2 += y
        else:
             t2 += '*'
    print(t2)
    if t == palavra_secreta:
        print(f'Parabéns você ganhou a palavra secreta era {palavra_secreta}')
        t = ''
        tentativas = 0
