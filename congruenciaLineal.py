'''
Autores:
    Karen Rugerio Armenta
    Bryan González Arellano
    Salvador Alejandro Gaytán Ibañez
Fecha: 28 de Mayo de 2023
Programa que implementa el método de la congruencia lineal para generar números pseudoaleatorios sin usar librerìas
'''

semilla = int(input("Semilla: "))
multiplicador = int(input("Multiplicador: "))
corrimiento = int(input("Corrimiento: "))
modulo = int(input("Módulo: "))
n = int(input("Números pseudoaleatorios a generar: "))
    
def congruencia_lineal(semilla,multiplicador,corrimiento,modulo, n):
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
            break

    return ciclo
        
periodo = congruencia_lineal(semilla,multiplicador,corrimiento,modulo, n)
ciclo = find_ciclo(semilla,multiplicador,corrimiento,modulo)
print("\nPeriodo: ", periodo)
print("Ciclo: ", ciclo)


        
media = 0
mediana = 0
moda = 0
desviacion_estandar_muestral = 0
varianza_muestral = 0
porcentaje_valores_ajustados = 0

cola = []
ciclo = []
        
