# ==============================================================================
# MÓDULO 4: INTRODUCCIÓN A PROCESSING
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================
# processing.run() es la forma de ejecutar CUALQUIER algoritmo de la
# Caja de Herramientas de QGIS desde Python. Todo lo que puedes hacer
# con clics en la interfaz, lo puedes automatizar con esta función.
#
# La estructura siempre es la misma:
#   processing.run("proveedor:algoritmo", { diccionario de parámetros })
# ==============================================================================

import processing

# 1. ¿CÓMO ENCONTRAR EL NOMBRE DE UN ALGORITMO?
# En QGIS, abre la Caja de Herramientas (Processing Toolbox), busca
# la herramienta que quieres usar, haz clic derecho → "Copy as Python Command".
# Eso te da el nombre exacto y los parámetros.

# También puedes listar algoritmos por palabra clave:
print("--- Algoritmos que contienen 'buffer' ---")
for alg in QgsApplication.processingRegistry().algorithms():
    if "buffer" in alg.id().lower():
        print(f"  {alg.id()}")

# 2. ¿CÓMO SABER QUÉ PARÁMETROS NECESITA?
# processing.algorithmHelp() te muestra la documentación completa.
print("\n--- Ayuda del algoritmo 'native:buffer' ---")
processing.algorithmHelp("native:buffer")

# 3. EJEMPLO BÁSICO: CREAR UN BUFFER
# Vamos a crear un buffer de 100 metros alrededor de la capa activa.

capa = iface.activeLayer()

if capa is None:
    print("\n⚠️ No hay capa seleccionada.")
else:
    print(f"\n--- Creando buffer de 100m para '{capa.name()}' ---")

    resultado = processing.run("native:buffer", {
        'INPUT': capa,               # La capa de entrada
        'DISTANCE': 100,             # Distancia del buffer (en unidades del CRS)
        'SEGMENTS': 10,              # Segmentos para redondear las esquinas
        'END_CAP_STYLE': 0,          # 0 = redondeado
        'JOIN_STYLE': 0,             # 0 = redondeado
        'DISSOLVE': False,           # No disolver en un solo polígono
        'OUTPUT': 'memory:'          # Guardar en memoria (temporal)
    })

    # 'memory:' crea una capa temporal que no se guarda en disco.
    # Útil para pruebas rápidas. Para guardar, usa una ruta de archivo.

    # Cargar el resultado al proyecto
    capa_buffer = resultado['OUTPUT']
    QgsProject.instance().addMapLayer(capa_buffer)
    print(f"  ✓ Buffer creado: {capa_buffer.featureCount()} entidades")

# 4. GUARDAR EN DISCO vs EN MEMORIA
# 'OUTPUT': 'memory:'                          → capa temporal (se pierde al cerrar)
# 'OUTPUT': 'C:/ruta/archivo.shp'              → shapefile en disco
# 'OUTPUT': 'C:/ruta/archivo.gpkg'             → GeoPackage en disco
# 'OUTPUT': 'TEMPORARY_OUTPUT'                 → igual que memory:

# 5. ENCADENAR ALGORITMOS
# Lo poderoso de processing.run() es que puedes encadenar varios:
# resultado1 → resultado2 → resultado3
# Ejemplo: Buffer → Clip → Dissolve
# El output de uno es el input del siguiente.

print("\n--- Ejemplo de encadenamiento ---")
print("  processing.run('native:buffer', ...)    → capa con buffer")
print("  processing.run('native:clip', ...)       → recortada al área de estudio")
print("  processing.run('native:dissolve', ...)   → disuelta en un solo polígono")
print("\n  Esto lo veremos en acción en la demo de interpolación.")
