#-*- coding: utf-8 -*-

import AGenetico as AG


def main():

    elitismo = [0, 0.1, 0.25, 0.5, 0.75]
    populacao = [10, 25, 50, 100, 500,1000]
    mutacao = 0.1

    qtd_iteracoes = 10
    k = 0
    while k < qtd_iteracoes:
        print "\nIteração: " + str(k+1)
        # Parte 1
        print "\nExperimento 1: Variação do Elitismo. "
        for i in range(len(elitismo)):
            problema =AG.A_Genetico(elitismo[i], mutacao, 100, 1000, 10, 21)
            problema.algoritmo()

        # Parte 2
        print "Experimento 2: Variação da População. "
        for i in range(len(populacao)):
            problema = AG.A_Genetico(0.1, mutacao, populacao[i], 1000, 10, 21)
            problema.algoritmo()
        k += 1


if __name__ == '__main__':
    main()
