"""
#1
animais = ['Cachorro', 'Avestruz', 'Alce', 'Cavalo',
                'Baleia', 'Gato', 'Urso', 'Abelha',
                'Carneiro', 'Cabra', 'Cobra', 'Coelho',
                'Mosquito', 'Peixe', 'Macaco', 'Aranha']

generator = (animal for animal in animais if len(animal) > 5 and (animal[0] == 'A' or animal[0] == 'C'))

print(list(generator)) 
"""

""" 
#2
animais = ['Cachorro', 'Cavalo', 'Baleia', 'Gato', 'Urso', 'Carneiro', 'Cabra', 'Cobra',
'Coelho', 'Mosquito', 'Peixe', 'Macaco']

animais2 = [animal for animal in animais if len(animal) < 8 and animal[0] == 'C']

print(list(animais2)) 
"""

""" 
#3
portão1 = (29,54,45)
portão2 = (12,28,37,54)
portão3 = (16,86,78,32,85,12)

senha1 = ''

for element in portão1:
    senha1 += '0' + str(element)[1:]

senha2 = str(portão2[1] + portão2[2]) + str(portão2[0] + portão2[3])

senha3 = str(min(portão3)) + str(max(portão3))

print(f'Portão 1: {senha1}')
print(f'Portão 2: {senha2}')
print(f'Portão 3: {senha3}') 
"""