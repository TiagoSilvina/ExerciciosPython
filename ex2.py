
# Calculadora

'''
operator = input('Digite a operação: ')

num1 = float(input('Digite o primeiro número: '))

num2 = float(input('Digite o segundo número: '))

if operator == '+' or operator == 'adição' :
    result = num1 + num2
    print(f'O resultado é {result}')
elif operator  ==  '-' or operator == 'subtração' :
    print(f'No enunciado não é pedida a subtração')
elif operator == '*' or operator == 'multiplicação' :
    result = num1 * num2
    print(f'O resultado é {result}')
elif operator == '/' or operator == 'divisão' :
    result = num1 / num2
    print(f'O resultado é {result}')
elif operator == '**' or operator == 'potência' :
    result = num1 ** num2
    print(f'O resultado é {result}')
else:
    print('Por favor selecione +,*,/,**, ou o nome da operação com letra minúscula')
'''

#Login

'''
login = False

username = str(input('Escolha um username: '))

password = str(input('Escolha uma password: '))

usernameCk = str(input('Digite o seu username: '))

if username != usernameCk:
    print(f'Username errado, tente novamente (Shift + F10)')
else:
    passwordCk = str(input('Digite a sua password: '))

    if username == usernameCk and password == passwordCk:
        login = True
    elif username == username and password != passwordCk:
        print('Password errada, tente novamente (Shift + F10)')


if login == False:
    username
else:
    print(f'Bem vindo {username}')
'''

