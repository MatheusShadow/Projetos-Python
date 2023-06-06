
while True:

    num_1 = input('Digite o primeiro numéro: ')
    try:
        num_1 = float(num_1)
    except:
        print('O primeiro número digitado é invalido, repita o processo novamente')
        continue


    num_2 = input('Digite o segundo número: ')
    try:
        
        num_2 = float(num_2)
    except:
        print('O segundo número é inválido, repita o processo novamente')
        continue

    operador = input('Digite um operador básico:  '
                     '\n "+" - ADIÇÃO' 
                     '\n "-" - SUBTRAÇÃO '
                     '\n "*" - MULTIPLICAÇÃO '
                     '\n "/" - DIVISÃO'
                     '\n: ')
    while operador != '+' and operador != '-' and operador != '*' and operador != '/':
        operador = input('Digite um operador básico correto:  '
                         '\n "+" - ADIÇÃO'
                         '\n "-" - SUBTRAÇÃO '
                         '\n "*" - MULTIPLICAÇÃO '
                         '\n "/" - DIVISÃO'
                         '\n: ')

    if operador == '+':
        print(f'O resultado da sua operação é: {num_1 + num_2}')
    elif operador == '-':
        print(f'O resultado da sua operação é: {num_1 - num_2}')
    elif operador == '/':
        print(f'O resultado da sua operação é: {num_1 / num_2}')
    else:
        print(f'O resultado da sua operação é: {num_1 * num_2}')


    qst = input('Deseja fazer outra operação?'
                    '\nDigite [s]im ou [n]ão: ')
    while qst.lower() != 's' and qst.lower() != 'n':
        qst = input('Digite uma opção válida!'
                    '\n[s]im ou [n]ão: ')
    if qst == 'n':
        print('Obrigado por usar o programa! :)')
        break
