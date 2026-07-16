# ==============================================================================
# MÓDULO 1: VARIABLES, TIPOS DE DATOS Y CONDICIONALES
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================

# 1. CREACIÓN DE VARIABLES
# Una variable es como una caja donde guardamos información para usarla después.
nombre_proyecto = "Análisis Ambiental Mérida"  # Tipo Texto (String)
numero_de_lotes = 45                           # Tipo Número Entero (Integer)
area_promedio = 520.75                         # Tipo Número Decimal (Float)
proyecto_activo = True                         # Tipo Booleano (True o False)

# Mostramos el contenido de nuestras variables en la consola
print("--- Información del Proyecto ---")
print("Nombre del proyecto:", nombre_proyecto)
print("Cantidad de lotes a procesar:", numero_de_lotes)
print("Área promedio de cada lote:", area_promedio, "metros cuadrados.")

# 2. ESTRUCTURAS CONDICIONALES (Toma de decisiones con IF / ELSE)
# Le pedimos a Python que evalúe una situación y decida qué camino tomar.
print("\n--- Evaluación de Condiciones ---")

# Ejemplo 1: Verificar si el proyecto está activo
if proyecto_activo == True:
    print("El proyecto está ACTIVO. Iniciando procesos en QGIS...")
else:
    print("El proyecto está INACTIVO. No se realizarán cambios.")

# Ejemplo 2: Evaluar la carga de trabajo según el número de lotes
# Usamos operadores de comparación como > (mayor que) o < (menor que)
if numero_de_lotes > 30:
    print("Alerta: El volumen de lotes es alto. Se recomienda automatizar con Python.")
else:
    print("El volumen de lotes es bajo. Se puede procesar manualmente.")