# ==============================================================================
# MÓDULO 3: GEOMETRÍA Y CAMPOS
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================
# INSTRUCCIONES: Carga una capa de POLÍGONOS en QGIS y selecciónala como
# capa activa antes de ejecutar este script.
# ==============================================================================

# 1. QgsGeometry — EXPLORAR GEOMETRÍAS
# Cada feature tiene un objeto QgsGeometry que contiene la forma espacial.
# De ahí podemos obtener área, perímetro, coordenadas, centroides, etc.

capa = iface.activeLayer()

if capa is None:
    print("⚠️ No hay capa seleccionada.")
elif capa.geometryType() != QgsWkbTypes.PolygonGeometry:
    print(f"⚠️ '{capa.name()}' no es de polígonos. Selecciona una capa poligonal.")
else:
    print(f"Capa: {capa.name()}")
    print(f"CRS: {capa.crs().authid()}")
    print(f"Entidades: {capa.featureCount()}")

    # Recorremos las primeras 5 entidades
    print("\n--- Propiedades geométricas (primeras 5) ---")
    contador = 0
    for feature in capa.getFeatures():
        if contador >= 5:
            break

        geom = feature.geometry()

        # .area()       → área en unidades del CRS (m² si es proyectado)
        # .length()     → perímetro en unidades del CRS
        # .centroid()   → punto central del polígono
        area = geom.area()
        perimetro = geom.length()
        centroide = geom.centroid().asPoint()

        print(f"\n  Feature ID: {feature.id()}")
        print(f"    Área:      {area:,.2f} unidades²")
        print(f"    Perímetro: {perimetro:,.2f} unidades")
        print(f"    Centroide: X={centroide.x():.4f}, Y={centroide.y():.4f}")

        contador += 1

    # ⚠️ IMPORTANTE SOBRE LAS UNIDADES:
    # Si tu CRS es geográfico (EPSG:4326), el área sale en grados² (inútil).
    # Si tu CRS es proyectado (ej. UTM EPSG:32616), el área sale en m².
    # Para cálculos reales, asegúrate de trabajar en un CRS proyectado.
    print(f"\n  ℹ Unidades del CRS: {capa.crs().mapUnits()}")
    print("    (Si sale '6' = grados → reproyecta a UTM para áreas reales)")

# -----------------------------------------------------------------------------

# 2. QgsField — CREAR NUEVOS CAMPOS EN LA TABLA DE ATRIBUTOS
# QgsField define una nueva columna. Necesitamos especificar:
#   - Nombre del campo
#   - Tipo de dato (QVariant.Double, QVariant.Int, QVariant.String)

# Ejemplo: Agregar un campo de texto llamado "categoria"
capa = iface.activeLayer()

if capa is not None and capa.type() == QgsMapLayerType.VectorLayer:
    # Verificamos si el campo ya existe
    nombres_existentes = [campo.name() for campo in capa.fields()]

    if "categoria" in nombres_existentes:
        print("\n  ℹ El campo 'categoria' ya existe.")
    else:
        # Activamos edición, agregamos el campo, y guardamos
        capa.startEditing()
        capa.dataProvider().addAttributes([
            QgsField("categoria", QVariant.String)
        ])
        capa.updateFields()
        capa.commitChanges()
        print("\n  ✓ Campo 'categoria' creado exitosamente.")
        print("    Abre la tabla de atributos para verificar.")

# -----------------------------------------------------------------------------

# 3. COMBINAR GEOMETRÍA + CAMPOS: CALCULAR Y GUARDAR
# Este es el patrón que usaremos en la práctica:
# Recorrer features → calcular algo con la geometría → guardar en un campo nuevo.

capa = iface.activeLayer()

if capa is not None and capa.geometryType() == QgsWkbTypes.PolygonGeometry:
    nombres = [c.name() for c in capa.fields()]

    # Creamos el campo si no existe
    if "area_m2" not in nombres:
        capa.startEditing()
        capa.dataProvider().addAttributes([
            QgsField("area_m2", QVariant.Double)
        ])
        capa.updateFields()
    else:
        capa.startEditing()

    # Llenamos el campo con el área de cada polígono
    idx_area = capa.fields().indexOf("area_m2")

    for feature in capa.getFeatures():
        area = feature.geometry().area()
        capa.changeAttributeValue(feature.id(), idx_area, round(area, 2))

    capa.commitChanges()
    print("\n  ✓ Campo 'area_m2' calculado y guardado para todas las entidades.")
