# -*- coding:utf-8 -*-

import random as R

class Cromossomo:

    def __init__(self, string):
        self.string = string
        self.aptdao = 0

    # Altera a função aptdao
    def set_aptdao(self, funcao_aptdao):
        self.aptdao = funcao_aptdao(self.string)

    # Retorna a função aptdao
    def get_aptdao(self):
        return self.aptdao

    # retorna o tamanho do cromossono(tamanho da string que o representa)
    def len_cromossomo(self):
        return len(self.string)

    # Realiza a mutação
    def mutacao(self, probabilidade):
        if(R.random() <= probabilidade):
            pos_bit = R.randint(0, self.len_cromossomo()-1)
            bit = int(self.string[pos_bit])
            bit = str((bit+1)%2)
            self.string = self.string[:pos_bit]+bit+self.string[(pos_bit+1):]

    # Retorna a string que representa o cromossomo
    def get_string(self):
        return self.string

    # Realiza o cruzamento entre cromossomos
    def cruzamento(self, cromossomo, probabilidade):
        #Cruzamento único
        pontoCruzamento = R.randint(0,self.len_cromossomo()-1)

        string1 = self.string[:pontoCruzamento] + cromossomo.string[pontoCruzamento:]
        string2 = cromossomo.string[:pontoCruzamento] + self.string[pontoCruzamento:]

        filho1 = Cromossomo(string1)
        filho2 = Cromossomo(string2)
        filho1.mutacao(probabilidade)
        filho2.mutacao(probabilidade)

        return (filho1,filho2)

    # Comparação com um outro cromossomo
    def __gt__(self, c1):
        return self.aptdao > c1.aptdao

    def __lt__(self, c1):
        return self.aptdao < c1.aptdao

    def __eq__(self, c1):
        return  self.aptdao == c1.aptdao
