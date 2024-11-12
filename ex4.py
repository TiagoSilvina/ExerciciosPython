'''
#1)
jogos = ['jogo1','jogo2','jogo3','jogo4','jogo5','jogo6']

precos = [69.99, 59.99, 49.99, 39.99, 29.99, 19.99 ]

quantidades = [60, 50, 40, 30, 20, 0]

custoFabrica = [30,30,30,15,15,15]

vendas = []

compraStock = []

ops = ['Registar venda: 1',
       'Comprar stock: 2',
       'Resumo da loja: 3',
       'Sair: 4',
       '\n']

open = True

while open ==  True:
    print('Bem vindo à Game Shop \n')

    for op in ops:
        print(op)

    menu = int(input('Escolha uma opção: '))

    if menu == 1:

        jogoAVender = input('Insira o nome do jogo: ')

        if jogoAVender in  jogos:
            i = jogos.index(jogoAVender)
            qtyV = int(input('Insira o nº de unidades: '))

            if quantidades[i] > 0 and quantidades[i] > qtyV:
                totalV = round(precos[i] * qtyV, 2)
                vendas.append(totalV)
                quantidades[i] -= qtyV
                print(f'Venda de {jogoAVender} efectuada com sucesso')
                print('\n')

            else:
                print('Não há stock disponível')
                print('\n')

        else:
            print('Não vendemos esse jogo')
            print('\n')

    elif menu == 2:

        jogoAComprar = input('Insira o nome do jogo a comprar: ')
        qtyC = int(input('Insira o nº de unidades: '))

        if jogoAComprar in  jogos:
            i = jogos.index(jogoAComprar)
            totalC = round(precos[i] * qtyC, 2)
            compraStock.append(totalC)
            quantidades[i] += qtyC
            print(f'Compra de {jogoAComprar} efectuada com sucesso')
            print('\n')
        else:
            print('Não compramos stock desse jogo')
            print('\n')

    elif menu == 3:
        for i, jogo in enumerate(jogos):
            print(f'{jogo} (preço: {precos[i]}€, qty: {quantidades[i]}, custo: {custoFabrica[i]}€)')
        print('\n')

        valorVendas = sum(vendas)
        qtyVendas = len(vendas)
        valorStock = sum(compraStock)
        qtyStock = len(compraStock)

        print(f'Valor de vendas: {valorVendas}')
        print(f'Quantidade de vendas: {qtyVendas}')
        print(f'valor gasto em Stock: {valorStock}')
        print(f'Compras de stock: {qtyStock}')
        print('\n')

    elif menu == 4:
        open = False
    else:
        print('Erro')

    continue_option = input('Deseja continuar? (s/n): ')
    print('\n')
    if continue_option != 's':
        open = False

print('Loja encerrada')
'''

""" 
#2)
produtos = []
precos = []

while len(produtos) < 5:
    produto = input('Insira o nome do produto: ')
    preco = float(input('Insira o preço do produto: '))
 
    produtos.append(produto)
    precos.append(preco)

total = sum(precos)


print(f'Carrinho de compras: ')

for produto in produtos:
    print(f'- {produto}')

print(f'Total carrinho: {total}€')
 """

