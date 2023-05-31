'''
Autores:
    Karen Rugerio Armenta
    Bryan González Arellano
    Salvador Alejandro Gaytán Ibañez
Fecha: 28 de Mayo de 2023
Programa que implementa el método de la congruencia lineal para generar números pseudoaleatorios sin usar librerìas
'''
from math import sqrt 
#Input values
semilla = int(input())
multiplicador = int(input())
corrimiento = int(input())
modulo = int(input())
n = int(input())
    
def find_cuantos(semilla,multiplicador,corrimiento,modulo, n):
    periodo = [semilla]
    cont = 0
    while cont<n: 
        semilla = (multiplicador * semilla + corrimiento) % modulo
        periodo.append(semilla)
        cont += 1            
    return periodo

def find_ciclo(semilla, multiplicador, corrimiento, modulo):
    cont = 0 #Contador para el ciclo
    ciclo = [] #Lista para guardar el ciclo
    periodo = [] #Lista para guardar el periodo
    while cont < modulo: #Mientras el contador sea menor al modulo
        periodo.append(semilla) #Se agrega la semilla a la lista del periodo
        semilla = (multiplicador * semilla + corrimiento) % modulo #Se calcula la semilla
        cont += 1 #Se aumenta el contador

        if semilla in periodo[:-1]: #Si la semilla está en el periodo
            indice_inicio_ciclo = periodo.index(semilla) #Se obtiene el índice del inicio del ciclo
            ciclo = periodo[indice_inicio_ciclo:] #Se obtiene el ciclo
            return ciclo, indice_inicio_ciclo #Se regresa el ciclo y el índice del inicio del ciclo
    return ciclo, 0

def calcular_media(lista): #Función para calcular la media
    suma = sum(lista) #Se suman los valores de la lista
    media = suma / len(lista) #Se divide la suma entre el número de elementos de la lista
    return float(media) #Se regresa la media

def calcular_mediana(lista): #Función para calcular la mediana
    lista_ordenada = sorted(lista) #Se ordena la lista
    longitud = len(lista_ordenada) #Se obtiene la longitud de la lista

    if longitud % 2 == 0: #Si la longitud es par
        indice_medio = longitud // 2 #Se obtiene el índice medio
        mediana = (lista_ordenada[indice_medio - 1] + lista_ordenada[indice_medio]) / 2 #Se obtiene la mediana
    else:
        indice_medio = longitud // 2 #Se obtiene el índice medio
        mediana = lista_ordenada[indice_medio] #Se obtiene la mediana
    return float(mediana) 

def calcular_moda(lista): #Función para calcular la moda
    frecuencias = {} #Diccionario para guardar las frecuencias
    moda = [] #Lista para guardar la moda
    
    for elemento in lista: #Para cada elemento en la lista
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1 #Se obtiene la frecuencia de cada elemento
    
    max_frecuencia = max(frecuencias.values()) #Se obtiene la frecuencia máxima
    
    if max_frecuencia == 0: #Si la frecuencia máxima es 0
        moda = []
    if max_frecuencia > 1: #Si la frecuencia máxima es mayor a 1
        moda = [elemento for elemento, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
        moda = ",".join(str(elemento) for elemento in moda)
    
    return moda

def percentiles(cuantos): #Función para calcular los percentiles
    #Se inicializan las variables
    perc10 = 0
    perc20 = 0
    perc30 = 0
    perc40 = 0
    perc50 = 0
    perc60 = 0
    perc70 = 0
    perc80 = 0
    perc90 = 0
    perc100 = 0
    percentiles_generales = [] #Lista para guardar los percentiles generales
    #Se calculan los percentiles generales
    for valor in cuantos:
        percentiles_generales.append(valor/(modulo))
    #Se calculan los percentiles
    for modificado in percentiles_generales:
        if(modificado <=0.1):
            perc10= perc10 + 1
        elif( modificado > 0.1 and modificado <= 0.2):
            perc20=perc20+1
        elif( modificado > 0.2 and modificado <= 0.3):
            perc30=perc30+1
        elif( modificado > 0.3 and modificado <= 0.4):
            perc40=perc40+1
        elif( modificado > 0.4 and modificado <= 0.5):
            perc50=perc50+1
        elif( modificado > 0.5 and modificado <= 0.6):
            perc60=perc60+1
        elif( modificado > 0.6 and modificado <= 0.7):
            perc70=perc70+1
        elif( modificado > 0.7 and modificado <= 0.8):
            perc80=perc80+1
        elif( modificado > 0.8 and modificado <= 0.9):
            perc90=perc90+1
        elif( modificado > 0.9 and modificado <= 1):
            perc100=perc100+1
    #Se calculan los porcentajes
    perc10 = perc10/len(cuantos)*100
    perc20 = perc20/len(cuantos)*100
    perc30 = perc30/len(cuantos)*100
    perc40 = perc40/len(cuantos)*100
    perc50 = perc50/len(cuantos)*100
    perc60 = perc60/len(cuantos)*100
    perc70 = perc70/len(cuantos)*100
    perc80 = perc80/len(cuantos)*100
    perc90 = perc90/len(cuantos)*100
    perc100 = perc100/len(cuantos)*100
    #Se imprimen los resultados
    print(perc10)
    print(perc20)
    print(perc30)
    print(perc40)
    print(perc50)
    print(perc60)
    print(perc70)
    print(perc80)
    print(perc90)
    print(perc100) 
    return

#Función para calcular la desviación estandar
def desviacion_estandar(cuantos):
    media = calcular_media(cuantos) #Se calcula la media
    varianza = 0 #Se inicializa la varianza
    for valor in cuantos: #Para cada valor en la lista
        varianza = varianza + (valor - media)**2 #Se calcula la varianza
    varianza = varianza/len(cuantos) #Se divide la varianza entre el número de elementos
    desviacion = varianza**(1/2) #Se calcula la desviación estandar
    print("Desviacion estandar: ", desviacion) #Se imprime el resultado
    return

#Función para calcular la varianza muestral
def varianza_muestral(cuantos): 
    media = calcular_media(cuantos) #Se calcula la media
    varianza = 0 #Se inicializa la varianza
    for valor in cuantos: #Para cada valor en la lista
        varianza = varianza + (valor - media)**2 #Se calcula la varianza
    varianza = varianza/len(cuantos) #Se divide la varianza entre el número de elementos
    print("Varianza muestral: ", varianza) #Se imprime el resultado
    return

def desviacion_estandar_y_varianza(cuantos): #Función para calcular la desviación estandar y varianza 
    x_ = calcular_media(cuantos) #Se calcula la media
    suma = 0 #Se inicializa la suma
    for observacion in cuantos: #Para cada valor en la lista
        suma += (observacion - x_)**2 #Se calcula la suma

    desv_std = suma / (len(cuantos) -1) #Se calcula la desviación estandar
    print(desv_std) #Se imprime el resultado
    print(sqrt(desv_std)) #

def comas(arreglo): #Función para imprimir los valores con comas
    if(len(arreglo)>=1):
        print(*arreglo,sep=',') #Se imprime el arreglo con comas
    else:
        print("")
    
#Calculo e impresion de resultados
cuantos = find_cuantos(semilla, multiplicador, corrimiento, modulo, n)
ciclo, indice_inicio_ciclo = find_ciclo(semilla, multiplicador, corrimiento, modulo)
if len(ciclo) == 2 and ciclo[0] == ciclo[1]:
    temp = ciclo[0]
    ciclo = [temp]
cola = cuantos[:indice_inicio_ciclo]
periodo = cola + ciclo
media = calcular_media(cuantos) 
mediana = calcular_mediana(cuantos)
moda = calcular_moda(cuantos)

comas(cola) #!!!  quitar el comentario para ver la cola
comas(periodo)
comas(ciclo)
print(len(cola))
print(len(periodo))
print(len(ciclo))
print(media)
print(mediana)
if len(moda)>=1:
    print(moda)
else: 
    print("")
desviacion_estandar_y_varianza(cuantos)
percentiles(cuantos)


        
