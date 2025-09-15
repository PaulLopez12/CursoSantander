# CursoSantander - Colección de Proyectos de Programación

## Descripción

Este repositorio contiene una colección de proyectos de programación desarrollados durante el curso de Santander. Los proyectos abarcan diferentes conceptos fundamentales de programación en Python, desde ejercicios básicos hasta herramientas de análisis de datos más avanzadas.

## Estructura del Repositorio

### 📊 **AnalisisDatosSimple**
Herramienta de análisis estadístico para archivos CSV.
- **Archivo principal**: `analisis.py`
- **Funcionalidad**: Cálculo de estadísticas descriptivas (media, mediana, desviación estándar) y visualización de datos
- **Dependencias**: numpy, matplotlib

### 🧮 **CalculadoraSimple**
Calculadora básica con operaciones aritméticas.
- **Archivo principal**: `Calculadora.py`
- **Funcionalidad**: Suma, resta, multiplicación y división con validación de errores
- **Características**: Interfaz interactiva, manejo de división por cero

### 📝 **ContadorPalabras**
Analizador de texto para contar palabras y frecuencias.
- **Archivo principal**: `Contador.py`
- **Funcionalidad**: Conteo de palabras totales y frecuencia de cada palabra
- **Características**: Procesamiento de texto con expresiones regulares

### 🎯 **FizzBuzz**
Implementación clásica del algoritmo FizzBuzz.
- **Archivo principal**: `FizzBuzz.py`
- **Funcionalidad**: Imprime números del 1 al 50 con reglas FizzBuzz
- **Reglas**: Fizz (múltiplos de 3), Buzz (múltiplos de 5), FizzBuzz (múltiplos de 3 y 5)

### 📚 **Introducción**
Ejercicios básicos de programación.
- **Archivos**:
  - `EjercicioAutocompletar.py`: Generación de cuadrados de números naturales
  - `EjercicioNumeroPrimo.py`: Verificación de números primos con pruebas
  - `prueba.py`: Archivo de pruebas adicionales

### 📄 **Archivos de Datos**
- `CSVPrueba.csv`: Archivo de ejemplo para pruebas de análisis de datos
- `ArchivoPrueba.txt`: Archivo de texto de ejemplo para pruebas

## Requisitos del Sistema

### Requisitos Mínimos
- **Python**: 3.6 o superior
- **Sistema Operativo**: Windows, macOS, o Linux

### Dependencias por Proyecto

#### AnalisisDatosSimple
```bash
pip install numpy matplotlib
```

#### Otros Proyectos
Los demás proyectos utilizan únicamente librerías estándar de Python, no requieren instalación adicional de dependencias.

## Instalación y Configuración

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd CursoSantander
   ```

2. **Instalar dependencias** (solo para AnalisisDatosSimple):
   ```bash
   pip install numpy matplotlib
   ```

3. **Verificar la instalación**:
   ```bash
   python --version
   ```

## Guía de Uso por Proyecto

### 🚀 **Inicio Rápido**

#### AnalisisDatosSimple
```bash
cd AnalisisDatosSimple
python analisis.py
# Ingresa la ruta del archivo CSV cuando se solicite
```

#### CalculadoraSimple
```bash
cd CalculadoraSimple
python Calculadora.py
# Sigue las instrucciones en pantalla
```

#### ContadorPalabras
```bash
cd ContadorPalabras
python Contador.py
# Ingresa la ruta del archivo de texto
```

#### FizzBuzz
```bash
cd FizzBuzz
python FizzBuzz.py
# Ejecuta directamente, no requiere entrada del usuario
```

#### Ejercicios de Introducción
```bash
cd Introducción
python EjercicioAutocompletar.py
python EjercicioNumeroPrimo.py
```

## Características Destacadas

### ✅ **Validación de Datos**
- Manejo de errores en entrada de usuario
- Validación de archivos existentes
- Prevención de división por cero

### 📊 **Análisis de Datos**
- Cálculos estadísticos robustos
- Visualización de datos
- Procesamiento de archivos CSV

### 🔧 **Código Limpio**
- Comentarios descriptivos
- Estructura modular
- Nombres de variables claros

### 🧪 **Pruebas Incluidas**
- Casos de prueba para funciones
- Validación de algoritmos
- Archivos de ejemplo incluidos

## Estructura de Archivos

```
CursoSantander/
├── AnalisisDatosSimple/
│   ├── analisis.py
│   └── README.md
├── CalculadoraSimple/
│   └── Calculadora.py
├── ContadorPalabras/
│   ├── Contador.py
│   └── texto_prueba.txt
├── FizzBuzz/
│   └── FizzBuzz.py
├── Introducción/
│   ├── EjercicioAutocompletar.py
│   ├── EjercicioNumeroPrimo.py
│   └── prueba.py
├── CSVPrueba.csv
├── ArchivoPrueba.txt
└── README.md
```

## Ejemplos de Uso

### Análisis de Datos
```python
# Usar el archivo CSV de ejemplo
python analisis.py
# Ingresa: CSVPrueba.csv
```

### Contador de Palabras
```python
# Usar el archivo de texto de ejemplo
python Contador.py
# Ingresa: texto_prueba.txt
```

## Contribuciones

Este repositorio es parte de un curso educativo. Las contribuciones son bienvenidas para:
- Mejorar la documentación
- Agregar más ejemplos
- Optimizar el código existente
- Añadir nuevas funcionalidades

## Licencia

Este proyecto es educativo y está disponible para fines de aprendizaje. Todos los archivos están bajo licencia MIT.

## Contacto

Para preguntas sobre este repositorio o los proyectos incluidos, contacta al desarrollador o consulta la documentación específica de cada proyecto en sus respectivos directorios.