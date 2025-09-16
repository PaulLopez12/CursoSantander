from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from datetime import datetime
import os

# Crear la instancia de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto en producción

# Lista para almacenar tareas (en una aplicación real usarías una base de datos)
tareas = []

@app.route('/')
def index():
    """Página principal que muestra todas las tareas"""
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_tarea():
    """Agregar una nueva tarea"""
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        prioridad = request.form.get('prioridad', 'media')
        
        if titulo:
            nueva_tarea = {
                'id': len(tareas) + 1,
                'titulo': titulo,
                'descripcion': descripcion,
                'prioridad': prioridad,
                'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'completada': False
            }
            tareas.append(nueva_tarea)
            flash('Tarea agregada exitosamente!', 'success')
            return redirect(url_for('index'))
        else:
            flash('El título es obligatorio!', 'error')
    
    return render_template('agregar.html')

@app.route('/completar/<int:tarea_id>')
def completar_tarea(tarea_id):
    """Marcar una tarea como completada"""
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea['completada'] = True
            flash('Tarea marcada como completada!', 'success')
            break
    return redirect(url_for('index'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea(tarea_id):
    """Eliminar una tarea"""
    global tareas
    tareas = [tarea for tarea in tareas if tarea['id'] != tarea_id]
    flash('Tarea eliminada!', 'success')
    return redirect(url_for('index'))

@app.route('/api/tareas')
def api_tareas():
    """API endpoint para obtener todas las tareas en formato JSON"""
    return jsonify(tareas)

@app.route('/api/tareas', methods=['POST'])
def api_agregar_tarea():
    """API endpoint para agregar una tarea via JSON"""
    data = request.get_json()
    
    if not data or not data.get('titulo'):
        return jsonify({'error': 'El título es obligatorio'}), 400
    
    nueva_tarea = {
        'id': len(tareas) + 1,
        'titulo': data['titulo'],
        'descripcion': data.get('descripcion', ''),
        'prioridad': data.get('prioridad', 'media'),
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'completada': False
    }
    
    tareas.append(nueva_tarea)
    return jsonify(nueva_tarea), 201

@app.route('/about')
def about():
    """Página de información sobre la aplicación"""
    return render_template('about.html')

if __name__ == '__main__':
    # Configuración para desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
