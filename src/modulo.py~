#!/usr/bin/python
#!encoding:UTF-8
import sys
import math

def calcular_pi (n):
  PI35DT = 3.1415926535897931159979634685441852
  sumatorio = 0.0
  ini = 0
  intervalos = 1.0 / float (n)
  for i in range(n):
    x_i = ((i+1) - 1.0/2.0) / n
    fx_i = 4.0 / (1.0 + x_i * x_i)
    ini += intervalos
    sumatorio += fx_i
  valor_pi = sumatorio / n
  return (valor_pi)

if (__name__ == "__main__"):

argumentos = sys.argv[1:]
if (len(argumentos) == 2):
  n = int (argumentos[0])
  aproximaciones = int (argumentos[1])
else:
  print "Introduzca el número de intervalos (n>0):"
  n = int (raw_input())
  print "Introduzca el número de aproximaciones:"
  aproximaciones = int (raw_input())
if (n>0):
  PI35DT = 3.1415926535897931159979634685441852
  intervalo = n
  lista = []
  for i in range (aproximaciones):
    valor = calcular_pi (intervalo)
    lista.append (valor)
    intervalo += n
  print lista
  diferencia = []
  for i in range (aproximaciones):
    dif = abs (PI35DT - lista[i])
    diferencia.append (dif)
  print "i\tPI35DT\tlista i\tPI35DT - lista i"
  for i in range (aproximaciones):
    print "%d\t%1.10f\t%1.10f\t%1.10f" % (i+1,PI35DT,lista[i],diferencia[i])
  #print "El valor de PI con 35 decimales es: %10.35f", % PI35
else:
    print "El valor de los intervalos debe ser positivo"