'''
#EX1
conjunto_Dudu = {'Espirito Santo', 'São Paulo'}
conjunto_Sami = {'Rio de Janeiro', 'Bahia'}

#1)
conjunto_Dudu.update(['Bahia', 'Acre','Santa Catarina','Segripe'])
conjunto_Sami.update(['Bahia','Minas gerais','Amazonas','Paraná'])

print(f'Estados Dudu: {conjunto_Dudu}')
print(f'Estados Sami: {conjunto_Sami}')

#2)
print(f'Estados que apenas o Dudu visitou: {conjunto_Dudu.difference(conjunto_Sami)}')

#3)
print(f'Estados que ambos visitaram: {conjunto_Dudu.intersection(conjunto_Sami)}')

#4)
if len(conjunto_Dudu) > len(conjunto_Sami) :
    vencedor = conjunto_Dudu
elif len(conjunto_Sami) == len(conjunto_Dudu):
    print('Empate')
else:
    vencedor = conjunto_Sami

percentagemVencedor = (len(vencedor)/27) * 100

print(f'O vencedor visitou {percentagemVencedor:.2f}% dos estados')
'''

'''
#EX2
conjunto = {num ** 2 for num in range(1, 10) if num % 2 == 0}

for num in range(1, 10):
    if num % 2 != 0:
        conjunto.add("Sou")
        conjunto.add("Ímpar")

print(conjunto)

# Resposta: 4,16,36,64,'Sou','Ímpar'
# 'Sou' e 'Ímpar' aparecem apenas uma vez, pois os conjuntos não devolvem dados repetidos
'''


