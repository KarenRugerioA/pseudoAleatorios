'''
Autores:
    Karen Rugerio Armenta
    Bryan González Arellano
    Salvador Alejandro Gaytán Ibañez
Fecha: 28 de Mayo de 2023
Programa que implementa el método de la congruencia lineal para generar números pseudoaleatorios sin usar librerìas
'''
#no debería funcionar si no son int? 
semilla = int(input("Semilla: "))
multiplicador = int(input("Multiplicador: "))
corrimiento = int(input("Corrimiento: "))
modulo = int(input("Módulo: "))
n = int(input("Números pseudoaleatorios a generar: "))
    
def find_cuantos(semilla,multiplicador,corrimiento,modulo, n):
    periodo = [semilla]
    cont = 0
    while cont<n: 
        semilla = (multiplicador * semilla + corrimiento) % modulo
        periodo.append(semilla)
        cont += 1            
    return periodo

def find_ciclo(semilla, multiplicador, corrimiento, modulo):
    cont = 0
    ciclo = []
    periodo = []

    while cont < modulo:
        periodo.append(semilla)
        semilla = (multiplicador * semilla + corrimiento) % modulo
        cont += 1

        if semilla in periodo[:-1]:
            indice_inicio_ciclo = periodo.index(semilla)
            ciclo = periodo[indice_inicio_ciclo:]
            return ciclo, indice_inicio_ciclo

    return ciclo, 0

def calcular_media(lista):
    suma = sum(lista)
    media = suma / len(lista)
    return float(media)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    longitud = len(lista_ordenada)

    if longitud % 2 == 0:
        indice_medio = longitud // 2
        mediana = (lista_ordenada[indice_medio - 1] + lista_ordenada[indice_medio]) // 2
    else:
        indice_medio = longitud // 2
        mediana = lista_ordenada[indice_medio]
    return int(mediana)

def calcular_moda(lista):
    frecuencias = {}
    moda = []
    
    for elemento in lista:
        frecuencias[elemento] = frecuencias.get(elemento, 0) + 1
    
    max_frecuencia = max(frecuencias.values())
    
    if max_frecuencia == 0:
        moda = []
    if max_frecuencia > 1:
        moda = [elemento for elemento, frecuencia in frecuencias.items() if frecuencia == max_frecuencia]
        moda = ", ".join(str(elemento) for elemento in moda)
    
    return moda

cuantos = find_cuantos(semilla, multiplicador, corrimiento, modulo, n)
ciclo, indice_inicio_ciclo = find_ciclo(semilla, multiplicador, corrimiento, modulo)
cola = cuantos[:indice_inicio_ciclo]
periodo = cola + ciclo
media = calcular_media(periodo) 
mediana = calcular_mediana(periodo)
moda = calcular_moda(cuantos)

print("\nCuantos: ", cuantos) #!!!  quitar el comentario para ver los cuantos #no se hace nada con xi?
print("Cola: ", cola) #!!!  quitar el comentario para ver la cola
print("Periodo: ", periodo) #!!!  quitar el comentario para ver el periodo
print("Ciclo: ", ciclo) #!!!  quitar el comentario para ver el ciclo
print("Longitud de la cola: ", len(cola))
print("Longitud del periodo: ", len(periodo))
print("Longitud del ciclo: ", len(ciclo))
#esto si es de "cuantos"????
print("Media: ", round(media, 2))
print("Mediana: ", mediana)
print("Moda: ", moda)

desviacion_estandar_muestral = 0
varianza_muestral = 0
porcentaje_valores_ajustados = 0

        
