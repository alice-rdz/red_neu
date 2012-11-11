from random import uniform
from sys import argv
from numpy import*
from subprocess import call
LOW=-1
HIGH=1

#Variables
#d = dimensiones
#a = taza de aprendizaje
#tam = tamano del vector 


class Neurona(object):
    def __init__(self,d,a,num):
        self.d = d
        self.a = a
        self.tam = d+1
        pesos = self.generar()
        condicion=self.generar()
        print pesos
        print condicion
        raw_input()
        self.entradas(num,pesos,condicion)
        

    def generar(self):
        w = zeros(self.tam)
        for i in range (self.tam):
            w[i] = (uniform(LOW,HIGH))
        return w
        
    def entradas(self,num,pesos,condicion):
        x = zeros(self.tam)
        for i in range(num):
            entrada = self.generar_entrada(x)
            t = self.activar(entrada,condicion)  
            y = self.activar(entrada,pesos)
            print 'y', y
            print 't',t
            print 'entrada',entrada
            print ''
            #for m in range(self.d):
             #   archivo.write(str(entrada[m]) + ' ')    
           # print >>archivo, '%d' % (salida)
       # archivo.close()
            self.recalcular(entrada,pesos,y,t)
            self.clasificacion(entrada,y,t)
        return 
    
    def clasificacion(self,entrada,y,t):
        c=str(t)+str(y)
        print c
        if (c=='00'):
            archivo='00.txt'
        elif (c=='01'):
            archivo='01.txt'
        elif (c=='10'):
            archivo='10.txt'
        elif (c=='11'):
            archivo='11.txt'
        archivo = open(archivo,'a')
        for m in range(self.d):
            archivo.write(str(entrada[m])+ ' ')
        archivo.write(str(t)+' '+str(y)+'\n')
        archivo.close
        return
        
        
    def generar_entrada(self,x):
        for i in range(self.tam):
            x[i] = (uniform(LOW,HIGH))
            x[-1] = -1
        return x
    
    def activar(self,entrada,pesos):
        suma=sum(pesos * entrada)
        y = 0
        if (suma >= 0):
            y = 1 
        return y
                                                               
    
    def recalcular(self,entrada,pesos,y,t):
        for i in range(self.tam): 
            pesos[i]=pesos[i]+(self.a*(t-y)*entrada[i])
        return pesos

def main():
    d = int(argv[1]) 
    a = float(argv[2])
    num = int(argv[3])
    neurona = Neurona(d,a,num)

main()








