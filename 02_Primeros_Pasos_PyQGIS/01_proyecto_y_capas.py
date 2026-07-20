# ==============================================================================
# MÓDULO 2: CONECTANDO PYTHON CON QGIS
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================
# INSTRUCCIONES: Este script se ejecuta dentro de la consola de Python de QGIS.
# Antes de correrlo, asegúrate de tener un proyecto abierto con al menos
# una o dos capas cargadas (vectoriales o ráster).
# ==============================================================================

# 1. ACCEDER AL PROYECTO ACTUAL
# QgsProject.instance() nos da acceso al proyecto que tenemos abierto en QGIS.
# Es nuestro punto de entrada a todo: capas, CRS del proyecto, rutas, etc.

proyecto = QgsProject.instance()

# Información básica del proyecto
print("--- Información del Proyecto ---")
print("Título:", proyecto.title())
print("Ruta del archivo:", proyecto.fileName())
print("CRS del proyecto:", proyecto.crs().authid())

# 2. LISTAR TODAS LAS CAPAS CARGADAS
# mapLayers() devuelve un diccionario con todas las capas del proyecto.
# Usamos .values() para obtener solo los objetos de capa (sin las llaves).

capas = proyecto.mapLayers().values()
print("\n--- Capas cargadas ---")
print("Total de capas:", len(list(capas)))

# Recorremos las capas e imprimimos su nombre y tipo
# (¡Aquí usamos el for que aprendimos en el Módulo 1!)
for capa in proyecto.mapLayers().values():
    # Verificamos si es vectorial o ráster
    if capa.type() == QgsMapLayerType.VectorLayer:
        tipo = "Vectorial"
    elif capa.type() == QgsMapLayerType.RasterLayer:
        tipo = "Ráster"
    else:
        tipo = "Otro"
    print(f"  • {capa.name()} → {tipo}")

# 3. OBTENER UNA CAPA ESPECÍFICA POR SU NOMBRE
# mapLayersByName() busca capas por nombre y devuelve una lista.
# Tomamos el primer resultado con [0].

# ⚠️ IMPORTANTE: Cambia "nombre_de_tu_capa" por el nombre real de una capa
# que tengas cargada en tu proyecto.

nombre_buscar = "nombre_de_tu_capa"   # ← CAMBIA ESTO
resultados = proyecto.mapLayersByName(nombre_buscar)

if len(resultados) > 0:
    mi_capa = resultados[0]
    print(f"\n--- Detalles de la capa: {mi_capa.name()} ---")
    print("CRS de la capa:", mi_capa.crs().authid())
    print("Extensión:", mi_capa.extent())
else:
    print(f"\n⚠️ No se encontró ninguna capa con el nombre '{nombre_buscar}'.")
    print("   Revisa el nombre exacto en el panel de capas.")

# 4. EXPLORAR UNA CAPA VECTORIAL (QgsVectorLayer)
# Si la capa es vectorial, podemos consultar su tipo de geometría,
# la cantidad de entidades (features) y los nombres de sus campos.

print("\n--- Explorando capas vectoriales ---")
for capa in proyecto.mapLayers().values():
    # Solo procesamos capas vectoriales
    if capa.type() != QgsMapLayerType.VectorLayer:
        continue

    # Tipo de geometría (punto, línea o polígono)
    tipos_geom = {0: "Punto", 1: "Línea", 2: "Polígono"}
    geom_tipo = tipos_geom.get(capa.geometryType(), "Desconocido")

    # Cantidad de entidades
    num_features = capa.featureCount()

    # Nombres de los campos (columnas de la tabla de atributos)
    campos = [campo.name() for campo in capa.fields()]

    print(f"\n  Capa: {capa.name()}")
    print(f"    Geometría: {geom_tipo}")
    print(f"    Entidades: {num_features}")
    print(f"    Campos: {campos}")
