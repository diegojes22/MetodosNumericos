import os
import glob
from pathlib import Path

def count_lines_in_file(file_path):
    """Cuenta las líneas de código en un archivo Python"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        total_lines = len(lines)
        empty_lines = sum(1 for line in lines if line.strip() == '')
        comment_lines = sum(1 for line in lines if line.strip().startswith('#'))
        code_lines = total_lines - empty_lines - comment_lines
        
        return {
            'total': total_lines,
            'code': code_lines,
            'empty': empty_lines,
            'comments': comment_lines
        }
    except Exception as e:
        print(f"Error leyendo {file_path}: {e}")
        return None

def analyze_python_project(project_root):
    """Analiza todos los archivos Python en el proyecto"""
    print(f"Analizando proyecto en: {project_root}")
    print("=" * 80)
    
    # Buscar todos los archivos .py
    python_files = []
    for root, dirs, files in os.walk(project_root):
        # Excluir directorios comunes que no son código fuente
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'env', 'venv', '.venv']]
        
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    if not python_files:
        print("No se encontraron archivos Python en el proyecto.")
        return
    
    total_stats = {
        'files': 0,
        'total': 0,
        'code': 0,
        'empty': 0,
        'comments': 0
    }
    
    file_stats = []
    
    # Analizar cada archivo
    for file_path in sorted(python_files):
        relative_path = os.path.relpath(file_path, project_root)
        stats = count_lines_in_file(file_path)
        
        if stats:
            file_stats.append((relative_path, stats))
            total_stats['files'] += 1
            total_stats['total'] += stats['total']
            total_stats['code'] += stats['code']
            total_stats['empty'] += stats['empty']
            total_stats['comments'] += stats['comments']
    
    # Mostrar resultados por archivo
    print(f"{'Archivo':<50} {'Total':<8} {'Código':<8} {'Vacías':<8} {'Comentarios':<12}")
    print("-" * 86)
    
    for file_path, stats in file_stats:
        print(f"{file_path:<50} {stats['total']:<8} {stats['code']:<8} {stats['empty']:<8} {stats['comments']:<12}")
    
    print("-" * 86)
    print(f"{'TOTALES:':<50} {total_stats['total']:<8} {total_stats['code']:<8} {total_stats['empty']:<8} {total_stats['comments']:<12}")
    print(f"\nResumen del proyecto:")
    print(f"• {total_stats['files']} archivos Python")
    print(f"• {total_stats['total']} líneas totales")
    print(f"• {total_stats['code']} líneas de código")
    print(f"• {total_stats['empty']} líneas vacías")
    print(f"• {total_stats['comments']} líneas de comentarios")
    
    # Estadísticas por directorio
    print("\n" + "=" * 80)
    print("ESTADÍSTICAS POR DIRECTORIO:")
    print("=" * 80)
    
    dir_stats = {}
    for file_path, stats in file_stats:
        dir_name = os.path.dirname(file_path)
        if dir_name == '':
            dir_name = 'raíz'
        
        if dir_name not in dir_stats:
            dir_stats[dir_name] = {'files': 0, 'total': 0, 'code': 0, 'empty': 0, 'comments': 0}
        
        dir_stats[dir_name]['files'] += 1
        dir_stats[dir_name]['total'] += stats['total']
        dir_stats[dir_name]['code'] += stats['code']
        dir_stats[dir_name]['empty'] += stats['empty']
        dir_stats[dir_name]['comments'] += stats['comments']
    
    print(f"{'Directorio':<40} {'Archivos':<8} {'Total':<8} {'Código':<8} {'Vacías':<8} {'Comentarios':<12}")
    print("-" * 94)
    
    for dir_name, stats in sorted(dir_stats.items()):
        print(f"{dir_name:<40} {stats['files']:<8} {stats['total']:<8} {stats['code']:<8} {stats['empty']:<8} {stats['comments']:<12}")

if __name__ == "__main__":
    project_root = r"d:\CodeProjects\NumericalMethods"
    analyze_python_project(project_root)