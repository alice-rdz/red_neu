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


class neurona(object):
    def __init__(self,d,a,num):
        self.d = d
        self.a = a
        self.tam = d+1
        pesos = self.generar_pesos()
        self.entradas(num,pesos)
        

    def generar_pesos(self):
        w = zeros(self.tam)
        for i in range (self.tam):
            w[i] = (uniform(LOW,HIGH))
        return w
        
    def entradas(self,num,pesos):
        entrada = zeros(self.tam)
        archivo = open('puntos.dat', 'w')
        for i in range(num):
            entrada = self.generar(entrada)
            salida = self.activar(entrada,pesos)
            for m in range(self.d):
                archivo.write(str(entrada[m]) + ' ')    
            print >>archivo, '%d' % (salida)
        archivo.close()
        self.comparar(pesos,entrada)
        return 
    
    def generar(self,entrada):
        for i in range(self.tam):
            entrada[i] = (uniform(LOW,HIGH))
            entrada[-1] = -1
        return entrada
    
    def activar(self,entrada,pesos):
        suma=sum(pesos * entrada)
        y = 0
        c = 0.6
        if (suma >= c):
            y = 1 
        return y
        
    def comparar(self,pesos,entrada):                
        archivo = open('puntos.dat','r')
        archivo2 = open('puntos2.dat','w')
        for line in archivo:
            t = int(uniform(0,2)) 
            line = line.strip()
            if len(line) == 0:
                continue
            dato =line.split()
            dato.append(t)
            y = int(dato[self.d])
            for m in range(self.d):
                entrada[m] = float(dato[m]) 
            if t !=y:
                pesos=self.recalcular(entrada,pesos,t,y)
                y = self.activar(entrada,pesos)
                dato.append(y)
                
            else:
                dato.append(y)
            print 'dato',dato
    
            for n in dato:
                print 'n',n
                archivo2.write(str(n)+' ')
            archivo2.write('\n')
            self.graficar()
        archivo.close()

        return                                                                
    
    def recalcular(self,entrada,pesos,t,y):
        for i in range(self.tam): 
            pesos[i]=pesos[i]+(self.a*(t-y)*entrada[i])
        return pesos


#class capa(neurona):
 #   def __init__(self,):

def main():
    d = int(argv[1]) 
    a = float(argv[2])
    num = int(argv[3])
    neu1 = neurona(d,a,num)
main()








