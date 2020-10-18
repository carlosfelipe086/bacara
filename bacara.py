# EP - Design de Software
# Equipe: Carlos Felipe Borges Mesquita e Keiya Nishio
# Data: 18/10/2020

import random
# cartas possiveis e seus valores 
# vários baralhos
cartas = {"A" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6, "7" : 7, "8" : 8, "9" : 9, "10" : 0, "J" : 0, "Q" : 0, "K" : 0}
chaves = list(cartas.keys())

#quantia inicial
dinheiro = 100

print ('Bem vindo ao Bacará!')
print ('Você começará com 100 fichas.')

# perguntando o valor da aposta e em quem vai apostar
while dinheiro != 0:
    
    #2 cartas aleatorias para o jogador
    cartas_jogador = []
    for e in range(2):
        cartas_jogador.append(chaves[random.randint(0, len(chaves) - 1)])

    #2 cartas aleatorias para o banco
    cartas_banco = []
    for e in range(2):
        cartas_banco.append(chaves[random.randint(0, len(chaves) - 1)])

    #carta para o jogador
    terceira_carta = []
    for e in range (1):
        terceira_carta.append(chaves[random.randint(0, len(chaves)-1)])

    #carta para o banco
    quarta_carta = []
    for e in range(1):
        quarta_carta.append(chaves[random.randint(0, len(chaves)-1)])

    aposta = int(input('Quanto quer apostar? '))
    escolha = input('Em quem você quer apostar (Jogador/Banco/Empate): ')

    if escolha == 'Jogador': #escolheu Jogador
    #cartas e soma do jogador   
        soma1 = 0
        novo_valor = 0
        print('CARTAS DO JOGADOR:')
        for e in cartas_jogador:
            print("Carta: {0} Valor: {1}".format(e, cartas[e]))
            soma1 += cartas[e]
        print ("Soma das cartas do Jogador igual a: {0}".format(soma1)) 

    #cartas e soma do banco   
        soma2 = 0
        novo_valor2 = 0
        print('CARTAS DO BANCO:')
        for e in cartas_banco:
            print("Carta: {0} Valor: {1}".format(e, cartas[e]))
            soma2 += cartas[e]
        print ("Soma das cartas do Banco igual a: {0}".format(soma2))

        if soma1 <= 5: #soma do jogador seja menor ou igual a 5
            print('Jogador, sua soma é igual a {0}, logo receberá mais uma carta.'.format(soma1))
            for e in terceira_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
            soma1 += cartas[e]
            print ('A nova soma é: {0}'.format(soma1))
            if soma1 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor = (int(str(soma1)[-1]))
                print('Jogador, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma1,novo_valor))
                print('Sua soma é igual a: {0}'.format(novo_valor))

        elif soma1 >= 10: #soma maior ou igual a 10
            novo_valor = (int(str(soma1)[-1]))
            print('Jogador, sua soma é igual {0}, consideraremos apenas a unidade ({1}) e mais uma carta'.format(soma1,novo_valor))
            for e in terceira_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
                soma1 = novo_valor + cartas[e]
            print('Sua soma é igual a: {0}'.format(soma1))
            if soma1 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor = (int(str(soma1)[-1]))
                print('Jogador, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma1,novo_valor))
                print('Sua soma é igual a: {0}'.format(novo_valor))
       
        if soma2 <= 5: #soma do banco seja menor ou igual a 5
            print('Banco, sua soma é igual a {0}, receberá mais uma carta.'.format(soma2))
            for e in quarta_carta:
                print ('Carta: {0} Valor: {1}'.format(e, cartas[e]))
            soma2 += cartas[e]
            print ('A nova soma é: {0}'.format(soma2))
            if soma2 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor2 = (int(str(soma2)[-1]))
                print('Banco, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma2,novo_valor2))
                print('Sua soma é igual a: {0}'.format(novo_valor2))

        elif soma2 >= 10: #soma maior ou igual a 10
            novo_valor2 = (int(str(soma2)[-1]))
            print('Banco, sua soma é igual {0}, consideraremos a unidade ({1}) e mais uma carta'.format(soma2,novo_valor2))
            for e in quarta_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
                soma2 = novo_valor2 + cartas[e]
            print('Sua soma é igual a: {0}'.format(soma2))  
            if soma2 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor2 = (int(str(soma2)[-1]))
                print('Banco, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma2,novo_valor2))
                print('Sua soma é igual a: {0}'.format(novo_valor2))
            
        if soma1 > soma2:
            dinheiro += int(aposta-(aposta*0.0124))
            print('Você ganhou esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        elif novo_valor > novo_valor2:
            dinheiro += int(aposta-(aposta*0.0124))
            print('Você ganhou esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        else:
            dinheiro -= aposta
            print ('Você perdeu esta rodada, Jogador.')
            print ('Agora você tem', dinheiro)

    elif escolha == 'Banco': #escolha Banco
    #cartas e soma do jogador 
        soma1 = 0
        novo_valor = 0
        print('CARTAS DO JOGADOR:')
        for e in cartas_jogador:
            print("Carta: {0} Valor: {1}".format(e, cartas[e]))
            soma1 += cartas[e]
        print ("Soma das cartas do Jogador igual a: {0}".format(soma1))

        #cartas e soma do banco
        soma2 = 0
        novo_valor2 = 0
        print('CARTAS DO BANCO:')
        for e in cartas_banco:
            print("Carta: {0} Valor: {1}".format(e, cartas[e]))
            soma2 += cartas[e]
        print ("Soma das cartas do Banco igual a: {0}".format(soma2))

        if soma1 <= 5: #soma do jogador seja menor ou igual a 5
            print('Jogador, sua soma é igual a {0}, logo receberá mais uma carta.'.format(soma1))
            for e in terceira_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
            soma1 += cartas[e]
            print ('A nova soma é: {0}'.format(soma1))
            if soma1 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor = (int(str(soma1)[-1]))
                print('Jogador, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma1,novo_valor))
                print('Sua soma é igual a: {0}'.format(novo_valor))

        elif soma1 >= 10: #soma maior ou igual a 10
            novo_valor = (int(str(soma1)[-1]))
            print('Jogador, sua soma é igual {0}, consideraremos apenas a unidade ({1}) e mais uma carta'.format(soma1,novo_valor))
            for e in terceira_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
                soma1 = novo_valor + cartas[e]
            print('Sua soma é igual a: {0}'.format(soma1))
            if soma1 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor = (int(str(soma1)[-1]))
                print('Jogador, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma1,novo_valor))
                print('Sua soma é igual a: {0}'.format(novo_valor))

        if soma2 <= 5: #soma do banco seja menor ou igual a 5
            print('Banco, sua soma é igual a {0}, logo receberá mais uma carta.'.format(soma2))
            for e in quarta_carta:
                print ('Carta: {0} Valor: {1}'.format(e, cartas[e]))
            soma2 += cartas[e]
            print ('A nova soma é: {0}'.format(soma2))
            if soma2 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor2 = (int(str(soma2)[-1]))
                print('Banco, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma2,novo_valor2))
                print('Sua soma é igual a: {0}'.format(novo_valor2))

        elif soma2 >= 10: #soma maior ou igual a 10
            novo_valor2 = (int(str(soma2)[-1]))
            print('Banco, sua soma é igual {0}, consideraremos a unidade ({1}) e mais uma carta'.format(soma2,novo_valor2))
            for e in quarta_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
                soma2 = novo_valor2 + cartas[e]
            print('Sua soma é igual a: {0}'.format(soma2))  
            if soma2 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor2 = (int(str(soma2)[-1]))
                print('Banco, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma2,novo_valor2))
                print('Sua soma é igual a: {0}'.format(novo_valor2))

        if soma2 > soma1:
            dinheiro = int(dinheiro+(aposta*0.95)-(aposta*0.0106))
            print('Você ganhou esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        elif novo_valor2 > novo_valor:
            dinheiro = int(dinheiro+(aposta*0.95)-(aposta*0.0106))
            print('Você ganhou esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        else:
            dinheiro -= aposta
            print ('Você perdeu esta rodada, Jogador.')
            print ('Agora você tem', dinheiro)

    elif escolha == 'Empate': #escolha Banco
    #cartas e soma do jogador 
        soma1 = 0
        novo_valor = 0
        print('CARTAS DO JOGADOR:')
        for e in cartas_jogador:
            print("Carta: {0} Valor: {1}".format(e, cartas[e]))
            soma1 += cartas[e]
        print ("Soma das cartas do Jogador igual a: {0}".format(soma1))

        #cartas e soma do banco
        soma2 = 0
        novo_valor2 = 0
        print('CARTAS DO BANCO:')
        for e in cartas_banco:
            print("Carta: {0} Valor: {1}".format(e, cartas[e]))
            soma2 += cartas[e]
        print ("Soma das cartas do Banco igual a: {0}".format(soma2))

        if soma1 <= 5: #soma do jogador seja menor ou igual a 5
            print('Jogador, sua soma é igual a {0}, logo receberá mais uma carta.'.format(soma1))
            for e in terceira_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
            soma1 += cartas[e]
            print ('A nova soma é: {0}'.format(soma1))
            if soma1 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor = (int(str(soma1)[-1]))
                print('Jogador, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma1,novo_valor))
                print('Sua soma é igual a: {0}'.format(novo_valor))

        elif soma1 >= 10: #soma maior ou igual a 10
            novo_valor = (int(str(soma1)[-1]))
            print('Jogador, sua soma é igual {0}, consideraremos apenas a unidade ({1}) e mais uma carta'.format(soma1,novo_valor))
            for e in terceira_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
                soma1 = novo_valor + cartas[e]
            print('Sua soma é igual a: {0}'.format(soma1))
            if soma1 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor = (int(str(soma1)[-1]))
                print('Jogador, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma1,novo_valor))
                print('Sua soma é igual a: {0}'.format(novo_valor))

        if soma2 <= 5: #soma do banco seja menor ou igual a 5
            print('Banco, sua soma é igual a {0}, logo receberá mais uma carta.'.format(soma2))
            for e in quarta_carta:
                print ('Carta: {0} Valor: {1}'.format(e, cartas[e]))
            soma2 += cartas[e]
            print ('A nova soma é: {0}'.format(soma2))
            if soma2 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor2 = (int(str(soma2)[-1]))
                print('Banco, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma2,novo_valor2))
                print('Sua soma é igual a: {0}'.format(novo_valor2))

        elif soma2 >= 10: #soma maior ou igual a 10
            novo_valor2 = (int(str(soma2)[-1]))
            print('Banco, sua soma é igual {0}, consideraremos a unidade ({1}) e mais uma carta'.format(soma2,novo_valor2))
            for e in quarta_carta:
                print('Carta: {0} Valor: {1}'.format(e, cartas[e]))
                soma2 = novo_valor2 + cartas[e]
            print('Sua soma é igual a: {0}'.format(soma2))  
            if soma2 >= 10: #soma maior ou igual a 10 apos ganhar uma nova carta
                novo_valor2 = (int(str(soma2)[-1]))
                print('Banco, sua soma é igual {0}, logo só consideraremos a unidade ({1})'.format(soma2,novo_valor2))
                print('Sua soma é igual a: {0}'.format(novo_valor2))

        if soma2 > soma1:
            dinheiro -= aposta 
            print('Você perdeu esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        elif novo_valor2 > novo_valor:
            dinheiro -= aposta
            print('Você perdeu esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        elif soma1 > soma2:
            dinheiro -= aposta
            print('Você perdeu esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        elif novo_valor > novo_valor2:
            dinheiro -= aposta
            print('Você perdeu esta rodada, Jogador.')
            print('Agora você tem', dinheiro)
        else:
            dinheiro += int((aposta*8)-(aposta*0.1436))
            print ('Você ganhou esta rodada, Jogador.')
            print ('Agora você tem', dinheiro)

print ('Fim de jogo!')