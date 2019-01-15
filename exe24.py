import random as rd

rand = rd.randint(1,5)

num = int(input('Chute um numero de 1 a 5 '))
if num == rand:
     print('Você acertou',rand)
else:
     print('Você errou, o numero certo é',rand)

