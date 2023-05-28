'''
Autores:
    Karen Rugerio Armenta
    Bryan González Arellano
    Salvador Alejandro Gaytán Ibañez
Fecha: 28 de Mayo de 2023
Programa que implementa el método de la congruencia lineal para generar números pseudoaleatorios sin usar librerìas
'''

def find_periodo_ciclo(semilla, multiplicador, corrimiento, modulo, n):
    periodo = [semilla]
    ciclo = []
    cont = 0

    while cont < n:
        semilla = (multiplicador * semilla + corrimiento) % modulo

        if semilla in periodo:
            indice_inicio_ciclo = periodo.index(semilla)
            ciclo = periodo[indice_inicio_ciclo:]
            break

        periodo.append(semilla)
        cont += 1

    return periodo[:n], ciclo

semilla = int(input("Semilla: "))
multiplicador = int(input("Multiplicador: "))
corrimiento = int(input("Corrimiento: "))
modulo = int(input("Módulo: "))
n = int(input("Números pseudoaleatorios a generar: "))

periodo, ciclo = find_periodo_ciclo(semilla, multiplicador, corrimiento, modulo, n)
print("\nPeriodo: ", periodo)
print("Ciclo: ", ciclo)

media = 0
mediana = 0
moda = 0
desviacion_estandar_muestral = 0
varianza_muestral = 0
porcentaje_valores_ajustados = 0

