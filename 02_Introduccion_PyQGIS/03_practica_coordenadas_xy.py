# ==============================================================================
# MÓDULO 2 — PRÁCTICA ESTRELLA
# Extracción automatizada de coordenadas X, Y con transformación de CRS
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================
# CONTEXTO:
# Tienes una capa de puntos en un CRS proyectado (ej. UTM zona 16N,
# EPSG:32616) y necesitas obtener las coordenadas en geográficas (WGS84,
# EPSG:4326) para entregarlas en un reporte o subirlas a Google Earth.
#
# INSTRUCCIONES:
# 1. Carga una capa de puntos en QGIS.
# 2. Selecciónala en el panel de capas (que quede activa).
# 3. Ajusta el CRS_DESTINO si necesitas algo diferente a WGS84.
# 4. Ejecuta este script en la consola de Python.
# ==============================================================================

# ── CONFIGURACIÓN ────────────────────────────────────────────────────────────
# CRS de destino: WGS84 geográfico (latitud / longitud)
CRS_DESTINO = QgsCoordinateReferenceSystem("EPSG:4326")
# ─────────────────────────────────────────────────────────────────────────────

# PASO 1: Obtener la capa activa y verificar que sea de puntos
capa = iface.activeLayer()

if capa is None:
    print("⚠️ No hay capa seleccionada. Selecciona una capa de puntos.")
elif capa.geometryType() != QgsWkbTypes.PointGeometry:
    print(f"⚠️ La capa '{capa.name()}' no es de puntos.")
    print("   Selecciona una capa de puntos y vuelve a ejecutar.")
else:
    print(f"✓ Capa: {capa.name()}")
    print(f"  CRS de la capa (origen): {capa.crs().authid()}")
    print(f"  CRS de destino: {CRS_DESTINO.authid()}")
    print(f"  Entidades: {capa.featureCount()}")

    # PASO 2: Crear el transformador de coordenadas
    # QgsCoordinateTransform convierte coordenadas de un CRS a otro "al vuelo".
    # Necesita: CRS origen, CRS destino, y el proyecto actual.
    transformador = QgsCoordinateTransform(
        capa.crs(),           # CRS de origen (el que tiene la capa)
        CRS_DESTINO,          # CRS de destino (al que queremos convertir)
        QgsProject.instance() # Proyecto actual
    )

    # PASO 3: Recorrer las entidades y extraer coordenadas transformadas
    print("\n" + "=" * 65)
    print(f"  {'ID':<6} {'X (Lon)':<15} {'Y (Lat)':<15}")
    print("=" * 65)

    # Aquí guardaremos los resultados para usarlos después
    resultados = []

    for feature in capa.getFeatures():
        # Obtenemos el punto original
        punto_original = feature.geometry().asPoint()

        # Transformamos las coordenadas al CRS de destino
        punto_transformado = transformador.transform(punto_original)

        # Redondeamos a 6 decimales (precisión estándar para WGS84)
        lon = round(punto_transformado.x(), 6)
        lat = round(punto_transformado.y(), 6)

        # Imprimimos en formato de tabla
        print(f"  {feature.id():<6} {lon:<15} {lat:<15}")

        # Guardamos en la lista
        resultados.append({
            "id": feature.id(),
            "lon": lon,
            "lat": lat
        })

    print("=" * 65)
    print(f"  Total de puntos procesados: {len(resultados)}")

    # PASO 4: Guardar los campos X e Y directamente en la tabla de atributos
    # Primero verificamos si los campos ya existen para no duplicarlos.
    nombres_campos = [campo.name() for campo in capa.fields()]

    campos_nuevos = []
    if "X_WGS84" not in nombres_campos:
        campos_nuevos.append(QgsField("X_WGS84", QVariant.Double))
    if "Y_WGS84" not in nombres_campos:
        campos_nuevos.append(QgsField("Y_WGS84", QVariant.Double))

    if campos_nuevos:
        # Para editar una capa necesitamos activar el modo de edición
        capa.startEditing()
        capa.dataProvider().addAttributes(campos_nuevos)
        capa.updateFields()
        print("\n  ✓ Campos 'X_WGS84' y 'Y_WGS84' creados.")
    else:
        capa.startEditing()
        print("\n  ℹ Los campos 'X_WGS84' y 'Y_WGS84' ya existen. Se actualizarán.")

    # Ahora llenamos los campos con los valores transformados
    for feature in capa.getFeatures():
        punto = feature.geometry().asPoint()
        punto_t = transformador.transform(punto)

        # Actualizamos los atributos de cada feature
        capa.changeAttributeValue(
            feature.id(),
            capa.fields().indexOf("X_WGS84"),
            round(punto_t.x(), 6)
        )
        capa.changeAttributeValue(
            feature.id(),
            capa.fields().indexOf("Y_WGS84"),
            round(punto_t.y(), 6)
        )

    # Guardamos los cambios
    capa.commitChanges()
    print("  ✓ Coordenadas guardadas en la tabla de atributos.")
    print("\n  Abre la tabla de atributos para ver las nuevas columnas.")
    print("  Script finalizado con éxito. ✓")
