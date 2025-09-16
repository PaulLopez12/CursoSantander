# Gestor de Tareas Flask

Una aplicación web simple desarrollada con Flask para gestionar tareas diarias.

## 🚀 Características

- ✅ Crear nuevas tareas con título, descripción y prioridad
- ✅ Marcar tareas como completadas
- ✅ Eliminar tareas
- ✅ Ver estadísticas de tareas
- ✅ Interfaz web moderna con Bootstrap
- ✅ API REST para integración
- ✅ Responsive design

## 🛠️ Tecnologías Utilizadas

- **Backend**: Python 3 + Flask
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Iconos**: Font Awesome
- **Templates**: Jinja2

## 📦 Instalación

### 1. Clonar o descargar el proyecto
```bash
cd G:\CursoSantander\GestorTareas
```

### 2. Crear y activar entorno virtual
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1  # Windows PowerShell
# o
venv\Scripts\activate.bat    # Windows CMD
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

## 🚀 Ejecución

### Modo desarrollo
```bash
python app.py
```

La aplicación estará disponible en: `http://localhost:5000`

### Modo producción
```bash
# Usando gunicorn (recomendado)
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:5000 app:app

# O usando waitress (Windows)
pip install waitress
waitress-serve --host=0.0.0.0 --port=5000 app:app
```

## 📁 Estructura del Proyecto

```
GestorTareas/
├── app.py                 # Aplicación principal Flask
├── requirements.txt       # Dependencias del proyecto
├── README.md             # Documentación
├── venv/                 # Entorno virtual
├── templates/            # Templates HTML
│   ├── base.html         # Template base
│   ├── index.html        # Página principal
│   ├── agregar.html      # Formulario agregar tarea
│   └── about.html        # Página acerca de
└── static/               # Archivos estáticos (CSS, JS, imágenes)
```

## 🔌 API Endpoints

### GET /api/tareas
Obtiene todas las tareas en formato JSON.

**Respuesta:**
```json
[
  {
    "id": 1,
    "titulo": "Mi tarea",
    "descripcion": "Descripción de la tarea",
    "prioridad": "media",
    "fecha_creacion": "2024-01-01 12:00:00",
    "completada": false
  }
]
```

### POST /api/tareas
Crea una nueva tarea.

**Request Body:**
```json
{
  "titulo": "Nueva tarea",
  "descripcion": "Descripción opcional",
  "prioridad": "alta"
}
```

**Respuesta:**
```json
{
  "id": 2,
  "titulo": "Nueva tarea",
  "descripcion": "Descripción opcional",
  "prioridad": "alta",
  "fecha_creacion": "2024-01-01 12:00:00",
  "completada": false
}
```

## 🎨 Personalización

### Cambiar el puerto
Edita `app.py` línea final:
```python
app.run(debug=True, host='0.0.0.0', port=8000)  # Cambiar puerto
```

### Cambiar la clave secreta
Edita `app.py`:
```python
app.secret_key = 'tu_nueva_clave_secreta_muy_segura'
```

## 🐛 Solución de Problemas

### Error de permisos en PowerShell
Si tienes problemas ejecutando scripts, ejecuta:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Puerto ya en uso
Si el puerto 5000 está ocupado, cambia el puerto en `app.py` o mata el proceso:
```bash
# Windows
netstat -ano | findstr :5000
taskkill /PID <PID> /F
```

## 📝 Notas

- Las tareas se almacenan en memoria (se pierden al reiniciar)
- Para persistencia, considera usar SQLite, PostgreSQL o MySQL
- La aplicación está configurada para desarrollo (debug=True)
- En producción, desactiva el modo debug

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Siéntete libre de:
- Reportar bugs
- Sugerir nuevas características
- Enviar pull requests

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.
