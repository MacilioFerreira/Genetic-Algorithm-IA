#-*- coding: utf-8 -*-

class Aptdao:

    def __init__(self, qtd_enfermeiros, qtd_turnos):
        self.qtd_enfermeiros = qtd_enfermeiros
        self.qtd_turnos = qtd_turnos

    def r0(self, string):
        quantidade = 1
        cont = 0
        for e in range(self.qtd_enfermeiros):
            for t in range(0,self.qtd_turnos,3):
                qtd = 0
                for i in range(t,t+3):
                    qtd += int(string[e*self.qtd_turnos+i])

                if qtd > quantidade:
                    cont += qtd-quantidade
        return cont


    def r1(self,string):
        cont = 0
        minimo = 1
        maximo = 3
        for j in range(self.qtd_turnos):
            cont_col = 0
            for i in range(self.qtd_enfermeiros):
                cont_col += int(string[i*self.qtd_turnos+j])
            if cont_col < minimo:
                cont += (minimo - cont_col)
            elif cont_col > maximo:
                cont += (cont_col - maximo)
        return cont

    def r2(self, string):
        quantidade = 5
        cont = 0
        for e in range(self.qtd_enfermeiros):
            qtd_t = 0
            for t in range(self.qtd_turnos):
                qtd_t += int(string[e*self.qtd_turnos+t])
            cont += abs(quantidade - qtd_t)

        return cont



    def r3(self, string):
        quantidade = 3
        cont = 0
        for e in range(self.qtd_enfermeiros):
            qtd = 0
            for t in range(0,self.qtd_turnos,3):
                flag = False
                for i in range(t,t+3):
                    flag = string[e*self.qtd_turnos+i]  == '1'
                    if flag:
                        break
                if flag:
                    qtd += 1
                if (not flag) or t == self.qtd_turnos-3:
                    if qtd > quantidade:
                        cont += qtd-quantidade
                    qtd = 0
        return cont

    def r4(self, string):
        cont = 0
        for e in range(self.qtd_enfermeiros):
            turnos = [0,0,0]
            for t in range(0,self.qtd_turnos,3):
                x=0
                for i in range(t,t+3):
                    turnos[x] += int(string[e*self.qtd_turnos+i])
                    x+=1
            x = -1
            for i in range(3):
                if turnos[i] > 0:
                    x+=1
            if x > 0:
                cont += x

        return cont

    def calcularViolacoes(self, string):
        qtd_enfermeiros = 10
        qtd_turnos = 21
        maximo = 3*qtd_enfermeiros*qtd_turnos
        maximo -= (self.r0(string)+self.r1(string)+self.r2(string)+self.r3(string)+self.r4(string))
        return maximo
