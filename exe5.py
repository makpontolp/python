n1 = input('Digite algo: ')
if n1.isnumeric() == False:
     print('O Valor digitado não é numerico')
else:
        print('O valor digitado é numerico')

if n1.isdecimal() == False:
     print('O Valor digitado não é decimal')
else:
        print('O valor digitado é decimal')

if n1.isupper() == False:
     print('O Valor digitado não é MAIUSCULO')
else:
        print('O valor digitado é MAIUSCULO')

if n1.isalnum() == False:
     print('O Valor digitado não é alfanumerico')
else:
        print('O valor digitado é alfanumerico')

print('Somente espaços ? {}'.format(n1.isspace()))

# VAI RETORNAR SE É NUMERICO OU NÃO (TRUE OR FALSE)
