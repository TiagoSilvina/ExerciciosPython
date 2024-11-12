# For Loop
'''
#1)
n = int(input('Escolha um número inteiro até 200: '))

mult5 = range(5,1001,5)

for num in mult5:
    print(num)
    if n > 200:
        print('n não pode ser maior que 200')
    elif num == n * 5:
        break

#2)
frutas = ['maçã', 'laranja', 'banana', 'pera', 'uva']

for fruta in frutas:
    print(fruta)
'''

#While loop

'''
#1)
count = 0
while count < 10:
    count +=1
    print(count)
    
#2)
import random

secret_num = random.randint(1,20)

tries = 0

guess = None

while secret_num !=guess:
    guess = int(input('Tente adivinhar um número entre 1 e 20: '))

    tries +=1

    if guess > secret_num:
        print('Tente um número menor')
    elif guess < secret_num:
        print('Tente um número maior')
    else:
        print(f'Adivinhou o número {secret_num} em {tries} tentativas')
'''

