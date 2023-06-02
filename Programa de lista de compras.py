lista = []

while True:
    qst1 = input('Você deseja [a]dicionar, [d]eletar, [v]er lista, [f]inalizar? ')
    while qst1.lower() != 'a' and qst1.lower() != 'd' and qst1.lower() != 'v' and qst1.lower() != 'f':
        qst1 = input('Digite corretamente!\nVocê deseja [a]dicionar, [d]eletar, [v]er, [f]inalizar? ')

    if qst1 == 'a':
        item = input('O que você quer adicionar? \nUm item por vez: ')

        lista.append(item)
        while True:
            qst2 = input('Deseja adicionar mais alguma coisa?\n[s]im ou [n]ão: ')
            while qst2.lower() != 's' and qst2.lower() != 'n':
                qst2 = input('Digite corretamente!\n[s]im ou [n]ão: ')
            if qst2 == 's':
                item = input('O que você quer adicionar? \nUm item por vez: ')
                lista.append(item)
            else:
                break

    elif qst1 == 'd':

        for i2, item2 in enumerate(lista):
            print(i2, item2)
        print('Se não tiver itens significa que você não adcionou nada ainda, aperte [v] para voltar!')
        qst3 = input('Escolha o número que deseja excluir: ')

        while True:
            while not qst3.isdigit() and not qst3.lower() == 'v':
                qst3 = input('Digite uma opção válida!: ')
            if qst3 == 'v':
                break
            qst3 = int(qst3)
            indice = qst3
            try:
                del lista[indice]
            except:
                print('Você digitou uma opção inválida, tente novamente nada foi alterado na sua lista')
            print('Sua lista de compras está assim:')
            for i2, item2 in enumerate(lista):
                print(i2, item2)
            qst4 = input('Você deseja deletar mais algum item?\n[s]im ou [n]ão: ')
            while qst4.lower() != 's' and qst4.lower() != 'n':
                qst4 = input('Digite corretamente!\n[s]im ou [n]ão: ')
            if qst4 == 's':
                for i2, item2 in enumerate(lista):
                    print(i2, item2)
                qst3 = input('Escolha o número que deseja excluir: ')
            else:
                break

    elif qst1 == 'v':
        print('Sua lista está assim:')
        for i in lista:
            print(i)

    else:
        print('Sua lista ficou assim:')
        for i in lista:
            print(i)
        print('Obrigado por utilizar o programa!')
        break