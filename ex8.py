
print('Bem vindo, vamos criar uma conta')

nome =  str(input('Qual é o seu nome? '))
saldo = float(input('Qual é o seu saldo inicial? '))

def id_generator():
    id_count = 1 
    while True:
        yield f"ID{id_count:04}" 
        id_count += 1  

generate_id = id_generator()
novo_id = next(generate_id) 

utilizador  = {'id':novo_id, 'nome': nome, 'saldo': saldo}

print(f'Bem vindo {nome}, ID {novo_id}')

if saldo > 50000:
    print(f'É um cliente muito valorizado')    

sessao = True

while sessao == True:

    funcionalidade = input('Por favor escolha uma opção \n 1:Depósito \n 2:Levantamento \n 3:Consultar Saldo \n 4:Sair \n Opção: ')

    if  funcionalidade == '1':
        deposito = float(input('Qual é o valor que deseja depositar? '))
        print(f'depositou {deposito}€')
        saldo += deposito
    elif funcionalidade == '2':
        levantamento = float(input('Qual é o valor que deseja levantar? '))
        if levantamento > saldo:
            print('Saldo infuficiente')
        else:
            print(f'Levantou {levantamento}€')
            saldo -= levantamento
    elif funcionalidade == '3':
        print(f'Seu saldo é {saldo}€')
    elif funcionalidade == '4':
        sair = input('Deseja sair? (s/n)')
        if sair == 's':
            print('Sessão encerrada')
            sessao = False
    else:
        print('Opção inválida')