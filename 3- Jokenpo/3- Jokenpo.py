import random

print('Chega de calcular médias, vamos nos divertir!')

list = [1, 2, 3]
e = random.choice(list)

c = int(input('Escolha uma das 3 opções: \n'
              '[1] PEDRA\n'
              '[2] PAPEL\n'
              '[3] TESOURA\n'
              'Qual você decidiu? '))

if e == c:
    print('Empatemos!')
elif e == 1 and c == 2:
    print('Eu escolhi pedra, você ganhou!')
elif e == 1 and c == 3:
    print('Eu escolhi pedra, você perdeu!')
elif e == 2 and c == 1:
    print('Eu escolhi papel, você perdeu!')
elif e == 2 and c == 3:
    print('Eu escolhi papel, você ganhou!')
elif e == 3 and c == 1:
    print('Eu escolhi tesoura, você ganhou!')
elif e == 3 and c == 2:
    print('Eu escolhi tesoura, você perdeu!')
