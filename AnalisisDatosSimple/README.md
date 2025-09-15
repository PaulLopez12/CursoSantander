# Análisis de Datos Simple

## Descripción

Este proyecto es una herramienta de análisis de datos básico que permite procesar archivos CSV y realizar cálculos estadísticos fundamentales. El programa lee archivos CSV, calcula estadísticas descriptivas (media, mediana, desviación estándar) para cada fila de datos y genera gráficos de dispersión para visualizar las relaciones entre las variables.

## Características

- Lectura de archivos CSV
- Cálculo de estadísticas descriptivas:
  - Media aritmética
  - Mediana
  - Desviación estándar
- Visualización de datos mediante gráficos de dispersión
- Interfaz de línea de comandos simple

## Requisitos

Para ejecutar este proyecto, necesitas tener instalado Python 3.x y las siguientes librerías:

```bash
pip install numpy matplotlib
```

### Dependencias específicas:
- `numpy`: Para cálculos numéricos y estadísticos
- `matplotlib`: Para la generación de gráficos
- `csv`: Librería estándar de Python (incluida por defecto)

## Instalación

1. Clona o descarga este repositorio
2. Navega al directorio del proyecto:
   ```bash
   cd AnalisisDatosSimple
   ```
3. Instala las dependencias:
   ```bash
   pip install numpy matplotlib
   ```

## Instrucciones de uso

1. Ejecuta el script:
   ```bash
   python analisis.py
   ```

2. Cuando se te solicite, ingresa la ruta completa del archivo CSV que deseas analizar:
   ```
   Ingrese la ruta del archivo csv: C:\ruta\a\tu\archivo.csv
   ```

3. El programa procesará el archivo y mostrará:
   - Los datos de cada fila
   - Las estadísticas calculadas (media, mediana, desviación estándar)
   - Un gráfico de dispersión de los datos

## Formato de archivo CSV

El archivo CSV debe contener datos numéricos en cada fila. El programa asume que:
- Cada fila representa un conjunto de datos a analizar
- Los valores deben ser numéricos (enteros o decimales)
- Los valores están separados por comas

### Ejemplo de archivo CSV:
```csv
1.5,2.3,3.7
4.1,5.2,6.8
7.3,8.9,9.1
```

## Limitaciones

- El programa actualmente está diseñado para archivos CSV con datos numéricos únicamente
- El gráfico de dispersión muestra la relación entre la primera y segunda columna de cada fila
- No incluye validación de errores para archivos malformados

## Estructura del proyecto

```
AnalisisDatosSimple/
├── analisis.py          # Script principal de análisis
└── README.md           # Este archivo de documentación
```

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, considera:
- Agregar validación de errores
- Soporte para diferentes formatos de archivo
- Más tipos de gráficos y visualizaciones
- Interfaz gráfica de usuario

## Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
