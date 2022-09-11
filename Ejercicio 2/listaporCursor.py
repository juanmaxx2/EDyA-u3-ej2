import numpy as np

class Celda:
    __sig = None
    __item = None

    def __init__(self, item = None):
        self.__sig = -1
        self.__item = item

    def setItem(self, item):
        self.__item = item
    
    def setSig(self, celda):
        self.__sig = celda

    def getItem(self):
        return self.__item
    
    def getSig(self):
        return self.__sig

class ListaPorContenido:
    __cant = None
    __cab = None
    __ul = None

    def __init__(self,cant):
        self.__item = np.empty(cant, dtype = Celda)
        for i in range(cant):
            self.__item[i] = Celda()
        self.__cant = cant
        self.__cab = -1
        self.__ul = -1

    def vacio(self):
        return self.__ul == -1

    def lleno(self):
        return self.__cant == self.__ul+1
    
    def rec(self, pos):
        i = self.__cab
        k = 0
        while i != -1 and k != pos:
            i = self.__item[i].getSig()
            k += 1
        return i

    def insertar(self, x, pos):
        pos -= 1
        if 0 <= pos <= self.__ul+1:
            if not self.lleno():
                if self.vacio():
                    self.__item[0].setItem(x)
                    self.__cab = 0
                else:
                    self.__item[self.__ul+1].setItem(x)
                    if self.__cant != self.__ul+2:
                        self.__item[self.__ul+1].setSig(self.rec(pos))
                    self.__item[self.rec(pos-1)].setSig(self.__ul+1)
                    if pos == 0:
                        self.__cab = pos
                self.__ul += 1

    def suprimir(self, pos):
        pos -= 1
        if self.__ul+1 > pos > 0:
            ant = self.__item[self.anterior(pos)]
            actual = self.__item[self.recuperar(pos)]
            ant.setSig(actual.getSig())
            self.__ul -= 1
            actual.setItem(None)
            actual.setItem(-1)
            print('Eliminado')
        else: print('\nError posicion no valida')
    
    def primerElemento(self):
        return self.__item[self.__cab].getItem()
    
    def ultimoElemento(self):
        return self.__item[self.__ul].getItem()
    
    def recuperar(self, pos):
        pos -= 1
        return self.__item[self.rec(pos)].getItem()
    
    def anterior(self, pos):
        if pos != 0:
            pos -= 2
            return self.__item[self.rec(pos)].getItem()
        else: return -1
    
    def siguiente (self, pos):
        if pos != self.__ul:
            return self.__item[self.rec(pos)].getItem()
        else: return -1

    def mostrar(self):
        i = self.__cab
        while i != -1:
            print(self.__item[i].getItem())
            i = self.__item[i].getSig()