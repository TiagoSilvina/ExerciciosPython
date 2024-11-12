'''
#1
heroi = {'Pequeno almoço':25,
         'Almoço':100,
         'Lanche':25,
         'Jantar':80}

armas = {'Cereais':25,
         'Tosta mista':25,
         'Sopa':50,
         'Bitoque': 100}

viloes = {'Fome':175,
          'Fomeca':100,
          'Larica': 50}

heroiUser = input('Escolha um herói: ')
armaUser = input('Escolha uma arma: ')
vilaoUser = input('Escolha um vilão: ')

if heroiUser in heroi and armaUser in armas:
    poderHeroi = heroi[heroiUser] + armas[armaUser]
else:
    print('Escola outra combinação')

if vilaoUser in viloes:
    poderVilao = viloes[vilaoUser]
    if poderVilao > poderHeroi:
        print(f'{armaUser} ao {heroiUser} não venceu a {vilaoUser}')
    elif poderVilao < poderHeroi:
        print(f'{armaUser} ao {heroiUser} acabou com a {vilaoUser}')
    else:
        print('Empate')
else:
    print('Vilão não encontrado')
'''

'''
#2
denominador = {n: max([d for d in range(1, 10) if n % d == 0]) for n in range(1, 100)}

for n, divisor in denominador.items():
    print(f"{n}: {divisor}")
'''