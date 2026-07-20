# Curso: Introducción a Python en QGIS
## Automatización básica de procesos geoespaciales

**Fechas:** 27, 28, 29 y 30 de julio de 2026

**Horario:** 18:00 a 20:00 h (hora centro de México)

**Duración:** 8 horas totales

**Modalidad:** En línea

**Nivel:** Principiantes (sin experiencia previa en programación)

**Dirigido a:** Arquitectos, biólogos, arqueólogos, urbanistas y profesionales afines a los Sistemas de Información Geográfica (SIG).

## **Instructora:** Jessica Daniela Ocaña Falcón

## 📖 Descripción del Curso

Este curso está diseñado para profesionales que utilizan QGIS en su día a día y desean aprender a automatizar tareas repetitivas, gestionar bases de datos pesadas y optimizar sus flujos de trabajo utilizando Python (PyQGIS). No se requieren conocimientos previos de programación; aprenderás desde la sintaxis básica hasta la creación de scripts funcionales.

---

## 🗺️ Temario

### Día 1 · MÓDULO 1: Fundamentos de Python desde cero

*El objetivo de este módulo es perder el miedo al código, entendiendo la sintaxis básica antes de interactuar con el mapa.*

- **Introducción a Python:** ¿Qué es y por qué usarlo en Sistemas de Información Geográfica?
- **Primer contacto:** Uso de la consola de Python integrada en QGIS.
- **Sintaxis y estructuras:** Variables, tipos de datos (texto, números, booleanos), listas y sentencias condicionales (`if` / `else`).
- **Ciclos `for`:** Recorrer elementos de una lista.
- **Mini-ejercicio:** Crear una lista de nombres de capas y recorrerla con un ciclo `for` para imprimirlas en la consola de QGIS.

### Día 2 · MÓDULO 2: Primeros pasos con PyQGIS

*Conectar Python con el mapa, aprendiendo a leer capas, recorrer entidades y transformar coordenadas.*

- **¿Qué es PyQGIS y cómo está organizado?**
- **`QgsProject`:** Acceder al proyecto actual.
- **`QgsVectorLayer` y `QgsRasterLayer`:** Trabajar con capas.
- **`QgsFeature`:** Recorrer entidades y leer atributos.
- **PRÁCTICA:** Extracción automatizada de coordenadas X, Y.
  * Lectura de una capa de puntos cargada en QGIS. Recorrido de sus entidades para extraer coordenadas. Transformación de CRS proyectado a geográfico (WGS84) usando `QgsCoordinateTransform`. Guardado de las coordenadas en nuevos campos de la tabla de atributos.

### Día 3 · MÓDULO 3: Procesamiento geométrico y campos

*Aprender a manipular geometrías, crear campos nuevos y realizar cálculos masivos en cuestión de segundos.*

- **`QgsGeometry`:** Obtener áreas, perímetros y coordenadas.
- **`QgsField`:** Crear nuevos campos en la tabla de atributos.
- **Trabajo con datos oficiales:** Filtros rápidos con Python para extraer información específica (Ej. datos INEGI).
- **PRÁCTICA:** Automatización de cálculos y uniones.
  * Uso de código para leer múltiples lotes/polígonos. Cálculo automático de Área y Perímetro en nuevas columnas. Unión masiva (Merge) de todos los lotes procesados en una sola capa final.

### Día 4 · MÓDULO 4: Automatización con Processing y cierre

*Usar las herramientas de geoproceso de QGIS (Processing) directamente desde Python para tareas complejas.*

- **Introducción a Processing:** Llamado a algoritmos nativos con `processing.run()`. Cómo usar la Caja de Herramientas desde el código.
- **Demostración en vivo:** Interpolación (IDW) y recorte (Clip) de un raster con un polígono de límite.
- **PROYECTO FINAL:** Limpieza y empaquetado de proyectos.
  * Script para buscar múltiples archivos Shapefiles sueltos en una carpeta y convertirlos automáticamente en una base de datos unificada en formato GeoPackage.
- **Cierre:** Repaso general, resolución de dudas y recursos para seguir aprendiendo.

---

## 💻 Requisitos

- QGIS versión 3.x instalado.
- Computadora con Windows, Linux o MacOS.
- Ningún conocimiento previo de programación requerido.

## 📦 Material Incluido

- Código fuente de todos los scripts utilizados.
- Archivos SIG de práctica (vectores y rasters).
- Acceso al repositorio del curso.
- Constancia digital de participación.

## 📂 Estructura del Repositorio

```
curso-pyqgis/
├── 01_Fundamentos_Python/
│   ├── 01_conceptos_basicos.py
│   ├── 02_variables_y_condicionales.py
│   └── 03_listas_y_ciclos_for.py
├── 02_Primeros_Pasos_PyQGIS/
│   ├── 01_proyecto_y_capas.py
│   ├── 02_features_y_atributos.py
│   └── 03_practica_coordenadas_xy.py
├── 03_Geometria_y_Campos/
│   ├── 01_geometria_y_campos.py
│   └── 02_practica_area_perimetro_merge.py
├── 04_Processing_y_Cierre/
│   ├── 01_intro_processing.py
│   ├── 02_demo_interpolacion_clip.py
│   └── 03_proyecto_final_geopackage.py
├── datos/
├── index.html
└── README.md
```
