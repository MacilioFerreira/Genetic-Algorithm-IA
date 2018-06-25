#-*- coding: utf-8 -*-

import random as R
import Populacao as P

class A_Genetico:

    def __init__(self, elitismo, mutacao, tamanho_populacao, qtd_iteracoes , qtd_enfermeiros=10, qtd_turnos=21):
        self.elitismo = elitismo
        self.mutacao = mutacao
        self.qtd_enfermeiros = qtd_enfermeiros
        self.qtd_turnos = qtd_turnos
        self.tam_populacao = tamanho_populacao
        self.qtd_iteracoes = qtd_iteracoes

    def algoritmo(self):

        # Inicializando os dados da população
        populacao = P.Populacao(self.qtd_enfermeiros, self.qtd_turnos)
        # Criando uma população aleatória
        populacao.gerarPopulacao(self.tam_populacao)
        # Ordenando de modo não crescente.
        populacao.ordenar()
        print "\nPopulação Inicial:"
        print populacao.mostrarPopulacao()
        media = 0
        arquivo = open('resultados1.txt', 'a')
        log = 'Elitismo: ' + str(self.elitismo) + ', Taxa mutacao: ' + str(self.mutacao) + ', '
        log += 'Tamanho populacao: ' + str(self.tam_populacao) + ', Qtd_Iteracoes: ' + str(self.qtd_iteracoes)
        log += '\n'
        arquivo.write(log)

        for i in range(0, self.qtd_iteracoes):
            log = 'Iteracao: ' + str(i + 1) + ' \n'
            condicaoParada = (3 * self.qtd_enfermeiros * self.qtd_turnos)
            if populacao.populacao[0].get_aptdao() == condicaoParada:
                break

            contador = populacao.totalaptdao()
            mediaAptdao = contador/float(self.tam_populacao)
            media += mediaAptdao
            melhorAptdao = populacao.populacao[0].get_aptdao()
            log += 'Media Fitness: ' + str(mediaAptdao) + '  |  Melhor Fitness:' + str(melhorAptdao) + '\n\n'
            arquivo.write(log)
            cruzamento = P.Populacao(self.qtd_enfermeiros, self.qtd_turnos)
            for j in range(0,self.tam_populacao):
                numero = R.random()
                cromossomo = None
                for cromossomo in populacao.populacao:
                    percentual = cromossomo.get_aptdao()/float(contador)
                    if numero > percentual:
                        numero -= percentual
                    else:
                        break
                cruzamento.adicionarCromossomo(cromossomo)

            # Nova geração
            nova = P.Populacao(self.qtd_enfermeiros, self.qtd_turnos)
            tamanho = self.tam_populacao if self.tam_populacao %2 == 0 else self.tam_populacao-1
            for k in range(0,tamanho,2):
                c1 = cruzamento.getElemento(k)
                c2 = cruzamento.getElemento(k+1)

                filho1,filho2 = c1.cruzamento(c2, self.mutacao)
                nova.adicionarCromossomo(filho1)
                nova.adicionarCromossomo(filho2)

            quantidade = int(self.tam_populacao * self.elitismo)
            nova.avaliar()
            nova.ordenar()
            anteriores = populacao.populacao[:quantidade]
            qtd_sucessores = int(self.tam_populacao-quantidade)
            sucessores = nova.populacao[0:qtd_sucessores]

            # nova População
            nova_populacao = P.Populacao(self.qtd_enfermeiros, self.qtd_turnos)
            nova_populacao.populacao = anteriores + sucessores
            nova_populacao.ordenar()
            # Alterando para a nova população gerada
            populacao = nova_populacao
        # Mostrando melhor cromossomo
        self.converterParaString(populacao.populacao[0])
        log = 'Fitness: ' + str(populacao.populacao[0].get_aptdao()) + '   ' + 'Media geral Fitness: ' + str(media / float(i + 1))
        arquivo.write(log)
        arquivo.write('\n___________________________________________________________________________________________\n\n\n')
        arquivo.close()

    def converterParaString(self, cromossomo):
        string = '\n         Turno:  '
        for t in range(self.qtd_turnos):
            string+='  '+str(t+1)
        print string
        string = ''
        for e in range(self.qtd_enfermeiros):
            string = 'Enfermeiro(a)-'+str(e+1)+': '
            for t in range(self.qtd_turnos):
                a = t
                while(a/10 > 0):
                    string+=' '
                    a = a/10
                string += '  '+cromossomo.string[e*self.qtd_turnos+t]+''
            print string
