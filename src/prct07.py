#!/usr/bin/python
#!encoding:UTF-8
import modulo
#Programa principal
tupla = (10, 20, 30, 40)
lista = [] #Creamos una lista
for i in tupla:
  valor_pi = modulo.calcular_pi (i)
  lista.append (valor_pi)
print lista

pi35 = []
for i in tupla:
  pi35.append (modulo.PI35DT) #Creamos una lista pi35
dif35 = []
for i in range (len (tupla)):
  dif35.append (abs(pi35[i] - lista[i]))
print "i\tPI35DT\t\tlista i\t\tPI35DT - list a i"
for i in range (len (tupla)):
  print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1, pi35[i], lista[i], dif35[i])
  
print "Pasando la salida a una matriz..."
print "i\tPI35DT\t\tlista i\t\tPI35DT - lista i", #
matriz = []
for i in range (len(tupla)):
  matriz.append ([i+1, pi35[i], lista[i], dif35[i]])
  print
  print matriz [i][0], #
  for j in range (1,4):
    print "\t%1.10f" % matriz[i][j], #