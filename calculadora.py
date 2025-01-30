#calculadora um pouco mais complexa
while True:
    print('qual tipo de conta você gostaria de fazer? ')
    print('1 = soma 2 = subtração 3 = divisão 4 = multiplicação 5= sair do programa')
    r1 = int(input(": "))
    if r1 == 1:
        print('então vamos começar com a soma: ')
        n1 = float(input('qual o primeiro numero: '))
        n2 = float(input('qual o segundo numero: '))
        r2 = n1 + n2
        print('o valor das somas de {} e {} é: {}'.format(n1, n2, r2))
    elif r1 == 2:
        print('então vamos começar com a subtração: ')
        n1 = float(input('qual o primeiro numero: '))
        n2 = float(input('qual o segundo numero: '))
        r2 = n1 - n2
        print('o valor da subtração de {} e {} é: {}'.format(n1, n2, r2))
    elif r1 == 3:
        print('então vamos começar com a divisão: ')
        n1 = float(input('qual o primeiro numero: '))
        n2 = float(input('qual o segundo numero: '))
        r2 = n1 / n2
        print('o valor da divisão de {} e {} é: {}'.format(n1, n2, r2))
    elif r1 == 4:
        print('então vamos começar com a multiplicação: ')
        n1 = float(input('qual o primeiro numero: '))
        n2 = float(input('qual o segundo numero: '))
        r2 = n1 * n2
        print('o valor da multiplicação de {} e {} é: {}'.format(n1, n2, r2))
    elif r1 == 5:
        print('volte novamente...')
        break
    else:
        print('resposta invalida, tente de novo')