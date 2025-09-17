import os
from pathlib import Path
import shutil

def organizar_archivos_recursivo(carpeta_objetivo, consolidar_en_raiz=True):
    """
    Organiza archivos de forma recursiva en una carpeta y sus subdirectorios.
    
    Args:
        carpeta_objetivo (Path): Carpeta principal a organizar
        consolidar_en_raiz (bool): Si True, mueve todos los archivos a la carpeta raíz organizados.
                                 Si False, organiza archivos dentro de cada subdirectorio.
    """
    
    categorias = {
        "Imagenes": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".webp"],
        "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".doc", ".xls",".xlsm", ".ppt", ".pptx"],
        "Videos": [".mp4", ".avi", ".mkv", ".mov", ".wmv", ".flv", ".webm"],
        "Musica": [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
        "Archivos_Comprimidos": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Ejecutables": [".exe", ".msi", ".deb", ".dmg"],
        "Codigo": [".py", ".js", ".html", ".css", ".java", ".cpp", ".c", ".php"],
    }
    
    # Crear diccionario de extensiones a categorías
    extension_a_categoria = {}
    for categoria, exts in categorias.items():
        for ext in exts:
            extension_a_categoria[ext.lower()] = categoria
    
    archivos_procesados = 0
    errores = 0
    
    def procesar_directorio(directorio_actual):
        nonlocal archivos_procesados, errores
        
        try:
            # Obtener todos los archivos del directorio actual
            archivos = [f for f in directorio_actual.iterdir() if f.is_file()]
            
            for archivo in archivos:
                try:
                    ext = archivo.suffix.lower()
                    categoria = extension_a_categoria.get(ext, "Otros")
                    
                    if consolidar_en_raiz:
                        # Mover archivos a la carpeta raíz organizados por categoría
                        destino_dir = carpeta_objetivo / categoria
                        destino_dir.mkdir(exist_ok=True)
                        
                        # Verificar si ya existe un archivo con el mismo nombre
                        destino_archivo = destino_dir / archivo.name
                        if destino_archivo.exists():
                            # Agregar número al nombre si ya existe
                            contador = 1
                            nombre_base = archivo.stem
                            extension = archivo.suffix
                            while destino_archivo.exists():
                                nuevo_nombre = f"{nombre_base}_{contador}{extension}"
                                destino_archivo = destino_dir / nuevo_nombre
                                contador += 1
                        
                        archivo.rename(destino_archivo)
                        print(f"✓ Movido: {archivo.relative_to(carpeta_objetivo)} → {categoria}/{destino_archivo.name}")
                        archivos_procesados += 1
                    
                    else:
                        # Organizar archivos dentro del mismo directorio
                        destino_dir = directorio_actual / categoria
                        destino_dir.mkdir(exist_ok=True)
                        
                        # Verificar si ya existe un archivo con el mismo nombre
                        destino_archivo = destino_dir / archivo.name
                        if destino_archivo.exists():
                            contador = 1
                            nombre_base = archivo.stem
                            extension = archivo.suffix
                            while destino_archivo.exists():
                                nuevo_nombre = f"{nombre_base}_{contador}{extension}"
                                destino_archivo = destino_dir / nuevo_nombre
                                contador += 1
                        
                        archivo.rename(destino_archivo)
                        print(f"✓ Organizado: {archivo.relative_to(carpeta_objetivo)} → {categoria}/{destino_archivo.name}")
                        archivos_procesados += 1
                
                except Exception as e:
                    print(f"✗ Error procesando {archivo.name}: {e}")
                    errores += 1
            
            # Procesar subdirectorios recursivamente
            subdirectorios = [d for d in directorio_actual.iterdir() if d.is_dir() and d.name not in categorias.keys() and d.name != "Otros"]
            
            for subdir in subdirectorios:
                procesar_directorio(subdir)
                
                # Si consolidamos en raíz y el directorio está vacío, eliminarlo
                if consolidar_en_raiz and not any(subdir.iterdir()):
                    try:
                        subdir.rmdir()
                        print(f"🗑️ Directorio vacío eliminado: {subdir.relative_to(carpeta_objetivo)}")
                    except:
                        pass  # Ignorar errores al eliminar directorios
                        
        except Exception as e:
            print(f"✗ Error procesando directorio {directorio_actual}: {e}")
            errores += 1
    
    print(f"🚀 Iniciando organización recursiva de: {carpeta_objetivo}")
    print(f"📁 Modo: {'Consolidar en raíz' if consolidar_en_raiz else 'Organizar en cada directorio'}")
    print("-" * 50)
    
    # Procesar directorio principal
    procesar_directorio(carpeta_objetivo)
    
    print("-" * 50)
    print(f"✅ Proceso completado:")
    print(f"   📄 Archivos procesados: {archivos_procesados}")
    print(f"   ❌ Errores: {errores}")

def main():
    """Función principal con opciones de configuración"""
    carpeta_objetivo = Path.home() / "Downloads"
    
    print("🔧 Organizador de Archivos Recursivo")
    print("=" * 40)
    print(f"📁 Carpeta objetivo: {carpeta_objetivo}")
    print()
    print("Opciones:")
    print("1. Consolidar todos los archivos en la carpeta raíz organizados por categoría")
    print("2. Organizar archivos dentro de cada subdirectorio")
    print("3. Solo organizar archivos de la carpeta raíz (modo original)")
    
    try:
        opcion = input("\nSelecciona una opción (1-3): ").strip()
        
        if opcion == "1":
            organizar_archivos_recursivo(carpeta_objetivo, consolidar_en_raiz=True)
        elif opcion == "2":
            organizar_archivos_recursivo(carpeta_objetivo, consolidar_en_raiz=False)
        elif opcion == "3":
            # Modo original - solo archivos de la carpeta raíz
            categorias = {
                "Imagenes": [".png", ".jpg", ".jpeg", ".gif"],
                "Documentos": [".pdf", ".docx", ".txt", ".xlsx", ".xlsm", ".ppt", ".pptx"],
                "Videos": [".mp4", ".avi", ".mkv"],
                "Musica": [".mp3", ".wav"],
            }
            
            extension_a_categoria = {}
            for categoria, exts in categorias.items():
                for ext in exts:
                    extension_a_categoria[ext.lower()] = categoria
            
            archivos = [f for f in carpeta_objetivo.iterdir() if f.is_file()]
            
            for archivo in archivos:
                ext = archivo.suffix.lower()
                categoria = extension_a_categoria.get(ext, "Otros")
                destino_dir = carpeta_objetivo / categoria
                destino_dir.mkdir(exist_ok=True)
                archivo.rename(destino_dir / archivo.name)
                print(f"Movido {archivo.name} a {categoria}/")
        else:
            print("❌ Opción no válida")
            return
            
    except KeyboardInterrupt:
        print("\n\n⏹️ Proceso cancelado por el usuario")
    except Exception as e:
        print(f"\n❌ Error: {e}")

if __name__ == "__main__":
    main()