# ==============================================================================
# MÓDULO 2: RECORRIENDO ENTIDADES Y LEYENDO ATRIBUTOS
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================
# INSTRUCCIONES: Antes de ejecutar, asegúrate de tener cargada una capa
# vectorial de puntos (o polígonos/líneas) con algunos atributos.
# ==============================================================================

# 1. SELECCIONAR LA CAPA ACTIVA
# iface.activeLayer() obtiene la capa que tienes seleccionada (resaltada)
# en el panel de capas de QGIS. Es la forma más rápida de trabajar.

capa = iface.activeLayer()

# Verificamos que hay una capa seleccionada
if capa is None:
    print("⚠️ No hay ninguna capa seleccionada.")
    print("   Haz clic en una capa en el panel de capas y vuelve a ejecutar.")
else:
    print(f"Capa activa: {capa.name()}")
    print(f"Entidades: {capa.featureCount()}")

# 2. CONOCER LOS CAMPOS (COLUMNAS) DE LA CAPA
# Antes de leer los atributos, necesitamos saber qué campos existen.
# Esto es como revisar los encabezados de una tabla de Excel.

print("\n--- Campos disponibles ---")
for campo in capa.fields():
    # campo.name()     → nombre de la columna
    # campo.typeName() → tipo de dato (String, Integer, Real, etc.)
    print(f"  {campo.name()} ({campo.typeName()})")

# 3. RECORRER ENTIDADES (QgsFeature)
# getFeatures() nos da un iterador con todas las entidades de la capa.
# Cada entidad (feature) tiene atributos y una geometría.

print("\n--- Primeras 5 entidades ---")
contador = 0
for feature in capa.getFeatures():
    # Limitamos a 5 para no saturar la consola
    if contador >= 5:
        break

    # feature.id()         → el ID interno de QGIS para esta entidad
    # feature.attributes() → una lista con TODOS los valores de sus campos
    print(f"\n  Feature ID: {feature.id()}")
    print(f"  Atributos: {feature.attributes()}")

    contador = contador + 1

# 4. ACCEDER A UN ATRIBUTO ESPECÍFICO POR NOMBRE
# Podemos usar feature["nombre_del_campo"] para leer un valor concreto.
# Esto es mucho más claro que usar la posición numérica.

# ⚠️ CAMBIA "nombre_del_campo" por un campo real de tu capa.
campo_consultar = "nombre_del_campo"   # ← CAMBIA ESTO

print(f"\n--- Valores del campo '{campo_consultar}' ---")
contador = 0
for feature in capa.getFeatures():
    if contador >= 10:
        break

    valor = feature[campo_consultar]
    print(f"  ID {feature.id()}: {valor}")

    contador = contador + 1

# 5. ACCEDER A LA GEOMETRÍA BÁSICA
# Cada feature tiene una geometría asociada. Podemos obtener el tipo
# y, en el caso de puntos, extraer las coordenadas directamente.

print("\n--- Geometrías (primeras 5) ---")
contador = 0
for feature in capa.getFeatures():
    if contador >= 5:
        break

    geom = feature.geometry()

    # Si es un punto, podemos obtener x e y directamente
    if geom.type() == QgsWkbTypes.PointGeometry:
        punto = geom.asPoint()
        print(f"  Feature {feature.id()}: X={punto.x():.2f}, Y={punto.y():.2f}")

    # Si es polígono o línea, mostramos el centroide (punto central)
    else:
        centroide = geom.centroid().asPoint()
        print(f"  Feature {feature.id()} (centroide): X={centroide.x():.2f}, Y={centroide.y():.2f}")

    contador = contador + 1

print("\n✓ Script finalizado.")
