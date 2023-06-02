while True:

    num_1 = input('Digite o primeiro numéro natural: ')
    while not num_1.isdigit():

        num_1 = input('O primeiro número é inválido digite novamente por favor: ')

    num_2 = input('Digite o segundo número natural: ')
    while not num_2.isdigit():

        num_2 = input('O segundo número é inválido digite novamente por favor: ')

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
    num_1 = int(num_1)
    num_2 = int(num_2)
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
