# Curso: Introducción a Python en QGIS
## Automatización básica de procesos geoespaciales

**Duración:** 8 horas totales

**Modalidad:** En línea

**Nivel:** Principiantes (sin experiencia previa en programación)

**Dirigido a:** Arquitectos, biólogos, arqueólogos, urbanistas y profesionales afines a los Sistemas de Información Geográfica (SIG).

**Instructora:** Jessica Daniela Ocaña Falcón
---

## 📖 Descripción del Curso
Este curso está diseñado para profesionales que utilizan QGIS en su día a día y desean aprender a automatizar tareas repetitivas, gestionar bases de datos pesadas y optimizar sus flujos de trabajo utilizando Python (PyQGIS). No se requieren conocimientos previos de programación; aprenderás desde la sintaxis básica hasta la creación de scripts funcionales.

---

## 🗺️ Temario

### MÓDULO 1: Fundamentos de Python desde cero
*El objetivo de este módulo es perder el miedo al código, entendiendo la sintaxis básica antes de interactuar con el mapa.*

* **Introducción a Python:** ¿Qué es y por qué usarlo en Sistemas de Información Geográfica?
* 
* **Primer contacto:** Uso de la consola de Python integrada en QGIS.
* 
* **Sintaxis básica:** Creación de variables y tipos de datos (texto, números, booleanos).
* 
* **Estructuras y decisiones:** Uso de Listas y sentencias condicionales (If / Else).
* 
* **Buenas prácticas:** Cómo comentar y organizar el código de forma limpia.

### MÓDULO 2: Introducción a PyQGIS y Primeras Automatizaciones
*Damos el salto a la interfaz de QGIS, aplicando código para consultar información y resolver problemas comunes de coordenadas.*
* **Conectando Python con QGIS:** Acceso al proyecto actual y selección de capas activas.
* **Exploración de datos:** Consulta de geometrías, campos y atributos mediante código.
* **Sistemas de Coordenadas (CRS):** Entendiendo la transformación de EPSG en memoria.
* **PRÁCTICA ESTRELLA:** Extracción automatizada de coordenadas X, Y. 
  * *Caso práctico:* Tomaremos una capa de puntos, transformaremos sus coordenadas al vuelo (Ej. del sistema oficial de México EPSG:6372 a otro sistema métrico) y las guardaremos en la tabla de atributos redondeadas a dos decimales.

### MÓDULO 3: Procesamiento Geométrico y Filtros Masivos
*Aprenderemos a manipular capas masivas y a realizar cálculos tediosos en cuestión de segundos.*
* **PRÁCTICA 1: Automatización de cálculos y uniones.**
  * Uso de código para leer múltiples lotes/polígonos.
  * Cálculo automático de Área y Perímetro en nuevas columnas.
  * Unión masiva (Merge) de todos los lotes procesados en una sola capa final.
* **Trabajo con bases de datos pesadas:** Identificación de atributos en capas oficiales.
* **PRÁCTICA 2: Filtros de alta velocidad (Datos INEGI).**
  * Carga de una capa masiva vectorial (Ej. Uso de Suelo, Vegetación o DENUE).
  * Aplicación de filtros mediante Python para extraer información específica sin colapsar QGIS (Ej. "De 50,000 polígonos, extráeme únicamente los Manglares").

### MÓDULO 4: Automatización Avanzada y Cierre de Proyecto
*Usaremos las herramientas de geoproceso de QGIS (Processing) directamente desde Python para tareas complejas.*
* **Llamado a algoritmos nativos:** Cómo usar la Caja de Herramientas desde el código.
* **PRÁCTICA 1: Interpolación y Recorte (Clip).**
  * Generación de un modelo de interpolación (IDW) a partir de puntos de muestreo.
  * Recorte automático del raster resultante utilizando un polígono de límite (Área de estudio).
* **PRÁCTICA 2 (PROYECTO FINAL): Limpieza y empaquetado de proyectos.**
  * Script para buscar múltiples archivos Shapefiles sueltos en una carpeta y convertirlos automáticamente en una base de datos unificada en formato **GeoPackage**.
* **Cierre del curso:** Repaso general, resolución de dudas y recursos para seguir aprendiendo.

---

## 💻 Requisitos
* QGIS versión 3.x instalado.
* Computadora con Windows, Linux o MacOS.
* Ningún conocimiento previo de programación requerido.

## 📦 Material Incluido
* Manual del curso.
* Código fuente de todos los scripts utilizados.
* Archivos SIG de práctica (Vectores y Rasters).
* Acceso al repositorio del curso.
* Constancia digital de participación.
