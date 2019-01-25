def nb_year(populacao, porcentagem, novos, final):
    anos = 0

    while populacao < final:
        populacao = ((populacao * porcentagem / 100) + populacao) + novos
        anos += 1
    return anos

print(nb_year(1500,5,100,5000))



