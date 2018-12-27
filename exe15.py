peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura: "))

imc = peso / (alt ** 2)

if imc < 17:
    print('Muito abaixo do peso')
elif imc >= 17 and imc <=18.49:
    print ('Abaixo do peso, {:.2f}'.format(imc))
elif imc >= 18.5 and imc <= 24.99:
    print('Peso Normal, {:.2f}'.format(imc))
elif imc >= 25 and imc <=29.99:
    print('Acima peso, {:.2f}'.format(imc))
elif imc >= 30 and imc <=34.99:
    print('Obesidade, {:.2f}'.format(imc))
elif imc >= 35 and imc <= 39.99:
    print('Obesidade II {:.2f}'.format(imc))
elif imc >= 40:
    print('VOCE VAI EXPLODIR SEU BALEIA!!!!, {:.2f}'.format(imc))




