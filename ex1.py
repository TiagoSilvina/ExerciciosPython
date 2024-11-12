#Input Output
'''
#1
print (f'Hello World')

#2
nome = input('Qual é o seu nome?')

idade = input('Qual é a sua idade?')

print(f'O seu nome é {nome} e tem {idade} anos')
'''

# Variables
#1
'''
1- 2
2- 5
3- 2,8
4- 3, 6
5- 1,3,7,10
'''

'''
#2
nome = input('Qual é o seu nome?')

apelido = input('Qual é o seu apelido?')

nomeCompleto = nome + ' ' + apelido

nota = float(input('Qual foi a sua nota na prova?'))

print(f'{nomeCompleto} tirou {nota}.')
'''

#Variables 2
'''
#1
nota1 = 15
nota2 = 11
nota3 = 18
nota4 = 13

media = (nota1 + nota2 + nota3 + nota4)/4

print(f'A média dos quatro alunos é {media}')
'''

#2
'''
tempC = float(input('Temperatura em Celsius: '))

tempK = float(tempC + 273.15)

tempF = float((tempC * 1.8) + 32)

print (f'{tempC}º Celcius equivale a {tempK}º kelvin e {tempF}º Farenheit')
'''

#3

cabelo = str(input('Qual é a cor do cabelo?'))

pele = str(input('Qual é a cor da pele?'))

classe = str(input('Qual é a classe? Guerreiro, Mago, Arqueiro?'))

idade = int(input('Qual é a idade?'))

altura = float(input('Qual é a altura?'))

skill = str(input('Qual é a habilidade específica?'))

print(f'Cor do cabelo: {cabelo},\n'
      f'Cor de pele: {pele},\n'
      f'Classe: {classe},\n'
      f'Idade: {idade},\n'
      f'Altura: {altura},\n'
      f'Habilidade específica: {skill}')