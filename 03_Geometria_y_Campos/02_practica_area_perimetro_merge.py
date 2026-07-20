# ==============================================================================
# MÓDULO 3 — PRÁCTICA ESTRELLA
# Automatización de cálculos de Área, Perímetro y Merge de polígonos
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================
# CONTEXTO:
# Tienes varios lotes/polígonos cargados en un proyecto QGIS (pueden ser
# capas separadas o una sola capa con múltiples features). Necesitas:
#   1. Calcular el área y perímetro de cada lote automáticamente.
#   2. Guardar esos valores en nuevos campos.
#   3. Unir (merge) todos los lotes procesados en una sola capa final.
#
# INSTRUCCIONES:
# 1. Carga una o varias capas de polígonos en tu proyecto QGIS.
# 2. Asegúrate de que estén en un CRS proyectado (ej. UTM EPSG:32616)
#    para que las áreas salgan en m².
# 3. Ejecuta este script desde la consola de Python.
# ==============================================================================

import processing

# ── CONFIGURACIÓN ────────────────────────────────────────────────────────────
# Nombre del archivo de salida (merge final).
# Cambia la ruta si quieres guardarlo en otro lugar.
RUTA_MERGE = "C:/Users/TU_USUARIO/Documents/merge_lotes.shp"   # ← CAMBIA ESTO
# ─────────────────────────────────────────────────────────────────────────────

proyecto = QgsProject.instance()

# PASO 1: Obtener todas las capas vectoriales de polígonos del proyecto
capas_poligonos = []
for capa in proyecto.mapLayers().values():
    if capa.type() == QgsMapLayerType.VectorLayer:
        if capa.geometryType() == QgsWkbTypes.PolygonGeometry:
            capas_poligonos.append(capa)

print(f"Capas de polígonos encontradas: {len(capas_poligonos)}")
for c in capas_poligonos:
    print(f"  • {c.name()} ({c.featureCount()} entidades)")

if len(capas_poligonos) == 0:
    print("\n⚠️ No hay capas de polígonos en el proyecto.")
else:
    # PASO 2: Calcular área y perímetro en cada capa
    print("\n--- Calculando Área y Perímetro ---")

    for capa in capas_poligonos:
        nombres_campos = [campo.name() for campo in capa.fields()]

        # Definir los campos nuevos que necesitamos
        campos_nuevos = []
        if "area_m2" not in nombres_campos:
            campos_nuevos.append(QgsField("area_m2", QVariant.Double))
        if "perim_m" not in nombres_campos:
            campos_nuevos.append(QgsField("perim_m", QVariant.Double))
        if "area_ha" not in nombres_campos:
            campos_nuevos.append(QgsField("area_ha", QVariant.Double))

        # Agregar campos si es necesario
        capa.startEditing()
        if campos_nuevos:
            capa.dataProvider().addAttributes(campos_nuevos)
            capa.updateFields()

        # Obtener índices de los campos
        idx_area = capa.fields().indexOf("area_m2")
        idx_perim = capa.fields().indexOf("perim_m")
        idx_ha = capa.fields().indexOf("area_ha")

        # Recorrer cada feature y calcular
        for feature in capa.getFeatures():
            geom = feature.geometry()
            area_m2 = geom.area()
            perimetro = geom.length()
            area_ha = area_m2 / 10000  # Conversión m² → hectáreas

            capa.changeAttributeValue(feature.id(), idx_area, round(area_m2, 2))
            capa.changeAttributeValue(feature.id(), idx_perim, round(perimetro, 2))
            capa.changeAttributeValue(feature.id(), idx_ha, round(area_ha, 4))

        capa.commitChanges()
        print(f"  ✓ {capa.name()}: {capa.featureCount()} entidades procesadas")

    # PASO 3: Merge (unión) de todas las capas en una sola
    print("\n--- Uniendo capas (Merge) ---")

    # Usamos processing.run() para llamar al algoritmo de merge nativo de QGIS.
    # Este es un adelanto del Módulo 4 — aquí solo lo usamos como herramienta.
    resultado = processing.run("native:mergevectorlayers", {
        'LAYERS': capas_poligonos,
        'CRS': capas_poligonos[0].crs(),      # Usamos el CRS de la primera capa
        'OUTPUT': RUTA_MERGE
    })

    # Cargar la capa resultante al proyecto
    capa_merge = QgsVectorLayer(resultado['OUTPUT'], "Merge_Lotes_Final", "ogr")

    if capa_merge.isValid():
        QgsProject.instance().addMapLayer(capa_merge)
        print(f"  ✓ Capa unificada creada: {capa_merge.featureCount()} entidades totales")
        print(f"  ✓ Guardada en: {RUTA_MERGE}")
    else:
        print("  ⚠️ Error al crear la capa de merge.")

    # PASO 4: Reporte final
    print("\n" + "=" * 55)
    print("  REPORTE FINAL")
    print("=" * 55)

    total_area = 0
    for feature in capa_merge.getFeatures():
        nombre = capa_merge.name()
        area = feature["area_ha"]
        total_area += area

    print(f"  Total de lotes: {capa_merge.featureCount()}")
    print(f"  Área total: {round(total_area, 4)} ha")
    print(f"  Archivo: {RUTA_MERGE}")
    print("=" * 55)
    print("\n  Script finalizado con éxito. ✓")
