# -*- coding: utf-8 -*-

import random as R
import Aptdao as F
import Cromossomo as C

class Populacao:

    def __init__(self, qtd_enfermeiros, qtd_turnos):
        self.qtd_enfermeiros = qtd_enfermeiros
        self.qtd_turnos = qtd_turnos
        self.tamanho = qtd_enfermeiros * qtd_turnos  #Tamanho do cromossomo para a representação
        self.populacao = []

    # Gera uma população aleatoriamente
    def gerarPopulacao(self, tamanho_populacao):
        aptdao = F.Aptdao(self.qtd_enfermeiros, self.qtd_turnos)
        self.populacao = []
        for i in range(0,tamanho_populacao):
            string = ""
            for j in range(0, self.tamanho):
                s = R.randint(0,1)
                string += str(s)
            n_cromossomo = C.Cromossomo(string)
            n_cromossomo.set_aptdao(aptdao.calcularViolacoes)
            self.populacao.append(n_cromossomo)

    # Adicionar um cromossomo
    def adicionarCromossomo(self, cromossomo):
        self.populacao.append(cromossomo)

    # Torna a população vazia
    def esvaziarPopulacao(self):
        self.populacao = []

    # Retorna o tamanho da população
    def tamanhoPopulacao(self):
        return len(self.populacao)

    # Retorna a soma total dos aptdao
    def totalaptdao(self):
        total = 0
        for elemento in self.populacao:
            total += elemento.get_aptdao()
        return total

    # Retorna o  elemento na posição passada
    def getElemento(self, posicao):
        return self.populacao[posicao]

    # Ordena a lista de modo não decrescente
    def ordenar(self):
        self.populacao.sort(reverse=True)

    # Avalia o aptdao de cada elemento da população
    def avaliar(self):
        aptdao = F.Aptdao(self.qtd_enfermeiros, self.qtd_turnos)
        for i in range(0, self.tamanhoPopulacao()):
            self.populacao[i].set_aptdao(aptdao.calcularViolacoes)

    # Printa a solução
    def mostrarPopulacao(self):
        for i in range(0, self.tamanhoPopulacao()):
            return self.populacao[i].string + ", " + str(self.populacao[i].aptdao)




