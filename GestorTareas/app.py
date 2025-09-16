from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from datetime import datetime
import os
from data_manager import cargar_tareas, agregar_tarea, completar_tarea, eliminar_tarea, obtener_estadisticas, backup_tareas

# Crear la instancia de la aplicación Flask
app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Cambia esto en producción

# Cargar tareas desde el archivo JSON al iniciar la aplicación
tareas = cargar_tareas()

@app.route('/')
def index():
    """Página principal que muestra todas las tareas"""
    return render_template('index.html', tareas=tareas)

@app.route('/agregar', methods=['GET', 'POST'])
def agregar_tarea_route():
    """Agregar una nueva tarea"""
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descripcion = request.form.get('descripcion')
        prioridad = request.form.get('prioridad', 'media')
        
        if titulo:
            nueva_tarea = agregar_tarea(tareas, titulo, descripcion, prioridad)
            if nueva_tarea:
                flash('Tarea agregada exitosamente!', 'success')
                return redirect(url_for('index'))
            else:
                flash('Error al guardar la tarea. Inténtalo de nuevo.', 'error')
        else:
            flash('El título es obligatorio!', 'error')
    
    return render_template('agregar.html')

@app.route('/completar/<int:tarea_id>')
def completar_tarea_route(tarea_id):
    """Marcar una tarea como completada"""
    if completar_tarea(tareas, tarea_id):
        flash('Tarea marcada como completada!', 'success')
    else:
        flash('Error al completar la tarea. Inténtalo de nuevo.', 'error')
    return redirect(url_for('index'))

@app.route('/eliminar/<int:tarea_id>')
def eliminar_tarea_route(tarea_id):
    """Eliminar una tarea"""
    if eliminar_tarea(tareas, tarea_id):
        flash('Tarea eliminada!', 'success')
    else:
        flash('Error al eliminar la tarea. Inténtalo de nuevo.', 'error')
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
    
    nueva_tarea = agregar_tarea(
        tareas, 
        data['titulo'], 
        data.get('descripcion', ''), 
        data.get('prioridad', 'media')
    )
    
    if nueva_tarea:
        return jsonify(nueva_tarea), 201
    else:
        return jsonify({'error': 'Error al guardar la tarea'}), 500

@app.route('/api/estadisticas')
def api_estadisticas():
    """API endpoint para obtener estadísticas de las tareas"""
    return jsonify(obtener_estadisticas(tareas))

@app.route('/backup')
def crear_backup():
    """Crear una copia de seguridad de las tareas"""
    backup_file = backup_tareas()
    if backup_file:
        flash(f'Backup creado exitosamente: {backup_file}', 'success')
    else:
        flash('Error al crear el backup', 'error')
    return redirect(url_for('index'))

@app.route('/about')
def about():
    """Página de información sobre la aplicación"""
    return render_template('about.html')

if __name__ == '__main__':
    # Configuración para desarrollo
    app.run(debug=True, host='0.0.0.0', port=5000)
