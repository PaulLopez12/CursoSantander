import json
import os
from datetime import datetime

# Archivo donde se guardarán las tareas
DATA_FILE = 'tareas.json'

def cargar_tareas():
    """
    Carga las tareas desde el archivo JSON.
    Si el archivo no existe, retorna una lista vacía.
    """
    try:
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, 'r', encoding='utf-8') as file:
                tareas = json.load(file)
                # Asegurar que cada tarea tenga un ID único
                for i, tarea in enumerate(tareas):
                    if 'id' not in tarea:
                        tarea['id'] = i + 1
                return tareas
        else:
            return []
    except (json.JSONDecodeError, FileNotFoundError, IOError) as e:
        print(f"Error al cargar tareas: {e}")
        return []

def guardar_tareas(tareas):
    """
    Guarda las tareas en el archivo JSON.
    Retorna True si se guardó correctamente, False en caso contrario.
    """
    try:
        with open(DATA_FILE, 'w', encoding='utf-8') as file:
            json.dump(tareas, file, ensure_ascii=False, indent=2)
        return True
    except IOError as e:
        print(f"Error al guardar tareas: {e}")
        return False

def obtener_siguiente_id(tareas):
    """
    Obtiene el siguiente ID disponible para una nueva tarea.
    """
    if not tareas:
        return 1
    return max(tarea.get('id', 0) for tarea in tareas) + 1

def agregar_tarea(tareas, titulo, descripcion='', prioridad='media'):
    """
    Agrega una nueva tarea a la lista y la guarda en el archivo.
    Retorna la tarea creada o None si hubo error.
    """
    nueva_tarea = {
        'id': obtener_siguiente_id(tareas),
        'titulo': titulo,
        'descripcion': descripcion,
        'prioridad': prioridad,
        'fecha_creacion': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'completada': False
    }
    
    tareas.append(nueva_tarea)
    
    if guardar_tareas(tareas):
        return nueva_tarea
    else:
        # Si no se pudo guardar, remover la tarea de la lista
        tareas.remove(nueva_tarea)
        return None

def completar_tarea(tareas, tarea_id):
    """
    Marca una tarea como completada y guarda los cambios.
    Retorna True si se completó correctamente, False en caso contrario.
    """
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea['completada'] = True
            return guardar_tareas(tareas)
    return False

def eliminar_tarea(tareas, tarea_id):
    """
    Elimina una tarea de la lista y guarda los cambios.
    Retorna True si se eliminó correctamente, False en caso contrario.
    """
    tarea_encontrada = None
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            tarea_encontrada = tarea
            break
    
    if tarea_encontrada:
        tareas.remove(tarea_encontrada)
        return guardar_tareas(tareas)
    return False

def obtener_tarea_por_id(tareas, tarea_id):
    """
    Obtiene una tarea específica por su ID.
    Retorna la tarea o None si no se encuentra.
    """
    for tarea in tareas:
        if tarea['id'] == tarea_id:
            return tarea
    return None

def obtener_estadisticas(tareas):
    """
    Calcula estadísticas de las tareas.
    Retorna un diccionario con las estadísticas.
    """
    total = len(tareas)
    completadas = sum(1 for tarea in tareas if tarea.get('completada', False))
    pendientes = total - completadas
    alta_prioridad = sum(1 for tarea in tareas if tarea.get('prioridad') == 'alta')
    
    return {
        'total': total,
        'completadas': completadas,
        'pendientes': pendientes,
        'alta_prioridad': alta_prioridad,
        'porcentaje_completadas': (completadas / total * 100) if total > 0 else 0
    }

def backup_tareas():
    """
    Crea una copia de seguridad de las tareas con timestamp.
    Retorna el nombre del archivo de backup o None si hubo error.
    """
    try:
        tareas = cargar_tareas()
        if tareas:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_file = f'tareas_backup_{timestamp}.json'
            with open(backup_file, 'w', encoding='utf-8') as file:
                json.dump(tareas, file, ensure_ascii=False, indent=2)
            return backup_file
    except Exception as e:
        print(f"Error al crear backup: {e}")
    return None
