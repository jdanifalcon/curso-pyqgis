# ==============================================================================
# MÓDULO 4 — DEMOSTRACIÓN EN VIVO
# Interpolación IDW y Recorte (Clip)
# Instructora: Jessica Daniela Ocaña Falcón
# ==============================================================================
# CONTEXTO:
# Este script es para que la instructora lo ejecute en vivo como demo.
# Los alumnos observan cómo se arma el diccionario de parámetros y cómo
# se encadenan dos algoritmos de Processing.
#
# REQUISITOS:
# 1. Una capa de PUNTOS con un campo numérico (ej. elevación, temperatura).
# 2. Una capa de POLÍGONO que sirva como límite de recorte (área de estudio).
# ==============================================================================

import processing

# ── CONFIGURACIÓN ────────────────────────────────────────────────────────────
# Nombres de las capas (deben coincidir con las del panel de capas)
NOMBRE_PUNTOS = "puntos_muestreo"        # ← Capa de puntos con valores
NOMBRE_LIMITE = "limite_area_estudio"     # ← Polígono para recortar

# Campo numérico a interpolar (ej. "elevacion", "temperatura", "ph")
CAMPO_INTERPOLAR = "elevacion"            # ← CAMBIA ESTO

# Tamaño del pixel del raster resultante (en unidades del CRS)
TAMANO_PIXEL = 30  # 30 metros si el CRS es UTM

# Ruta de salida
RUTA_IDW = "C:/Users/TU_USUARIO/Documents/idw_resultado.tif"     # ← CAMBIA
RUTA_CLIP = "C:/Users/TU_USUARIO/Documents/idw_recortado.tif"    # ← CAMBIA
# ─────────────────────────────────────────────────────────────────────────────

proyecto = QgsProject.instance()

# Obtener las capas
capa_puntos = proyecto.mapLayersByName(NOMBRE_PUNTOS)
capa_limite = proyecto.mapLayersByName(NOMBRE_LIMITE)

if not capa_puntos:
    print(f"⚠️ No se encontró la capa '{NOMBRE_PUNTOS}'.")
elif not capa_limite:
    print(f"⚠️ No se encontró la capa '{NOMBRE_LIMITE}'.")
else:
    capa_puntos = capa_puntos[0]
    capa_limite = capa_limite[0]

    print(f"Puntos: {capa_puntos.name()} ({capa_puntos.featureCount()} entidades)")
    print(f"Límite: {capa_limite.name()}")
    print(f"Campo a interpolar: {CAMPO_INTERPOLAR}")

    # PASO 1: Interpolación IDW
    # IDW = Inverse Distance Weighting (Ponderación por Distancia Inversa)
    # Los puntos cercanos tienen más influencia que los lejanos.
    print("\n--- Paso 1: Interpolación IDW ---")

    # El algoritmo de interpolación IDW en QGIS necesita un string especial
    # para definir qué capa y campo usar. El formato es:
    # "ruta_capa::~::0::~::indice_campo::~::0"
    idx_campo = capa_puntos.fields().indexOf(CAMPO_INTERPOLAR)
    interpolation_data = f"{capa_puntos.source()}::~::0::~::{idx_campo}::~::0"

    # Obtenemos la extensión de la capa de puntos para definir el área del raster
    extent = capa_puntos.extent()
    extent_str = f"{extent.xMinimum()},{extent.xMaximum()},{extent.yMinimum()},{extent.yMaximum()} [{capa_puntos.crs().authid()}]"

    # Calculamos el número de columnas y filas según el tamaño de pixel
    n_cols = int((extent.xMaximum() - extent.xMinimum()) / TAMANO_PIXEL)
    n_rows = int((extent.yMaximum() - extent.yMinimum()) / TAMANO_PIXEL)

    resultado_idw = processing.run("qgis:idwinterpolation", {
        'INTERPOLATION_DATA': interpolation_data,
        'DISTANCE_COEFFICIENT': 2,       # Potencia (estándar = 2)
        'EXTENT': extent_str,
        'PIXEL_SIZE': TAMANO_PIXEL,
        'OUTPUT': RUTA_IDW
    })

    print(f"  ✓ Raster IDW generado: {RUTA_IDW}")

    # Cargar al proyecto
    raster_idw = QgsRasterLayer(RUTA_IDW, "IDW_Resultado")
    QgsProject.instance().addMapLayer(raster_idw)

    # PASO 2: Recorte (Clip) con el polígono límite
    print("\n--- Paso 2: Recorte con polígono ---")

    resultado_clip = processing.run("gdal:cliprasterbymasklayer", {
        'INPUT': raster_idw,
        'MASK': capa_limite,
        'NODATA': -9999,
        'CROP_TO_CUTLINE': True,         # Recortar al borde del polígono
        'KEEP_RESOLUTION': True,
        'OUTPUT': RUTA_CLIP
    })

    print(f"  ✓ Raster recortado: {RUTA_CLIP}")

    # Cargar el resultado recortado
    raster_clip = QgsRasterLayer(RUTA_CLIP, "IDW_Recortado")
    QgsProject.instance().addMapLayer(raster_clip)

    print("\n  Resultado: raster de interpolación recortado al área de estudio.")
    print("  Script finalizado con éxito. ✓")
