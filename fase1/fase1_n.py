from random import uniform
from sys import argv
from numpy import*

class neurona(object):
    def __init__(self, tam):
        pesos = self.generar(tam)
        self.recibir_entrada(tam,pesos)

    def generar(self,tam):
        tam=tam+1
        w = zeros(tam)
        for m in range(tam):
            w[m]=(uniform(-1,1))
        return w

    def recibir_entrada(self, tam,pesos):
        entrada=zeros(tam)
        entradas = int(argv[2])
        archivo=open('puntos.txt','w')
        for m in range(entradas):
            entrada = self.generar_entradas(entrada)
            entraday=append(entrada,-1)
            salida = self.activar(tam,pesos,entraday)
            print >>archivo, '%f %f %d' % (entrada[0],entrada[1], salida)
        archivo.close()  
        

    def generar_entradas(self,entrada):
        for i in range(2):
            entrada[i]= (uniform(-1,1))
        return entrada

    def activar(self,tam,pesos,entrada):
        suma=sum(pesos*entrada)
        c=.6
        if suma >= c:
            salida=1 #Salida = ACTIVADO
        else:
            salida=0 #Salida = DESACTIVADO
        return salida
        


def main():
    tam=int(argv[1])
    neu=neurona(tam)
main()
