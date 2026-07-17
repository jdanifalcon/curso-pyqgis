# ==============================================================================
# MÓDULO 1: LISTAS Y CICLOS FOR
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================

# 1. LISTAS
# Una lista es una colección ordenada de elementos.
# Se crean con corchetes [] y los elementos se separan con comas.

# Lista de texto (strings)
capas_del_proyecto = ["rios", "carreteras", "uso_de_suelo", "localidades"]

# Lista de números
areas_lotes = [320.5, 480.2, 150.0, 610.8, 275.3]

# Podemos saber cuántos elementos tiene una lista con len()
print("--- Información de las listas ---")
print("Capas en el proyecto:", capas_del_proyecto)
print("Total de capas:", len(capas_del_proyecto))
print("Total de lotes:", len(areas_lotes))

# Acceder a un elemento por su posición (índice).
# ¡Importante! En Python el primer elemento es el 0, no el 1.
print("\nPrimera capa:", capas_del_proyecto[0])   # "rios"
print("Tercera capa:", capas_del_proyecto[2])     # "uso_de_suelo"

# Agregar un elemento al final de la lista con .append()
capas_del_proyecto.append("curvas_de_nivel")
print("\nDespués de agregar una capa:", capas_del_proyecto)

# -----------------------------------------------------------------------------

# 2. CICLOS FOR
# Un ciclo for recorre cada elemento de una lista, uno por uno,
# y ejecuta el bloque de código indentado para cada uno.

# Ejemplo 1: Recorrer e imprimir cada nombre de capa
print("\n--- Recorriendo capas del proyecto ---")
for nombre in capas_del_proyecto:
    print("  Capa encontrada:", nombre)

# Ejemplo 2: Recorrer números y hacer un cálculo
# Convertimos cada área de m² a hectáreas (dividir entre 10,000)
print("\n--- Áreas convertidas a hectáreas ---")
for area in areas_lotes:
    area_ha = area / 10000
    print("  ", area, "m²  →", round(area_ha, 4), "ha")

# Ejemplo 3: Combinar for con if (filtrar elementos)
# Solo mostrar los lotes que superen los 300 m²
print("\n--- Lotes mayores a 300 m² ---")
for area in areas_lotes:
    if area > 300:
        print("  Lote grande:", area, "m²")

# -----------------------------------------------------------------------------

# 3. MINI-EJERCICIO INTEGRADOR
# Simulamos un listado de capas como las que encontraríamos en un proyecto QGIS.
# Recorremos la lista y reportamos cada una en la consola.

nombres_capas = [
    "puntos_muestreo",
    "limite_area_estudio",
    "modelo_elevacion",
    "red_hidrologica",
    "vegetacion_inegi"
]

print("\n========================================")
print("  REPORTE DE CAPAS DEL PROYECTO")
print("========================================")

contador = 0
for capa in nombres_capas:
    contador = contador + 1
    print("  [" + str(contador) + "]", capa)

print("----------------------------------------")
print("  Total de capas encontradas:", contador)
print("========================================")
