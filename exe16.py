nome = input('Digite nome: ')
idade = input('Digite idade: ')
cargo = input('Digite cargo: ')
sal = float(input('Digite seu salario: '))
reaj = ((sal * 0.38) + sal)
grat = ((reaj * 0.2) + reaj)
salT = (grat - (grat * 0.15))

print('Olá {},{} cargo: {}. Seu salario bruto será de {} e liquido será de {}'.format(nome, idade, cargo, reaj, salT))