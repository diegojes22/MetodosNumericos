import os
from datetime import datetime
import html

def generate_code_document():
    """Genera un documento HTML con todo el código Python del proyecto"""
    
    project_root = r"d:\CodeProjects\NumericalMethods"
    output_file = os.path.join(project_root, "codigo_completo.html")
    
    # Buscar todos los archivos .py
    python_files = []
    for root, dirs, files in os.walk(project_root):
        # Excluir directorios que no son código fuente
        dirs[:] = [d for d in dirs if d not in ['__pycache__', '.git', 'env', 'venv', '.venv']]
        
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    
    # Crear el contenido HTML
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Código Fuente - Métodos Numéricos</title>
    <style>
        body {{
            font-family: 'Courier New', monospace;
            margin: 40px;
            line-height: 1.4;
            font-size: 11px;
        }}
        
        .header {{
            text-align: center;
            margin-bottom: 30px;
            font-family: Arial, sans-serif;
        }}
        
        .header h1 {{
            color: #2c3e50;
            font-size: 24px;
            margin-bottom: 10px;
        }}
        
        .header .info {{
            color: #7f8c8d;
            font-size: 14px;
        }}
        
        .file-section {{
            margin-bottom: 40px;
            page-break-inside: avoid;
        }}
        
        .file-header {{
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            font-weight: bold;
            font-size: 14px;
            margin-bottom: 0;
            border-radius: 5px 5px 0 0;
        }}
        
        .file-path {{
            background-color: #ecf0f1;
            padding: 5px 15px;
            font-size: 11px;
            color: #2c3e50;
            margin: 0;
            border-bottom: 1px solid #bdc3c7;
        }}
        
        .code-block {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            border-top: none;
            padding: 0;
            margin: 0;
            font-family: 'Courier New', monospace;
            font-size: 10px;
            border-radius: 0 0 5px 5px;
        }}
        
        .code-content {{
            padding: 15px;
            white-space: pre-wrap;
            overflow-x: auto;
        }}
        
        .line-numbers {{
            background-color: #f1f3f4;
            color: #70757a;
            padding: 15px 10px;
            border-right: 1px solid #e9ecef;
            float: left;
            font-size: 9px;
            line-height: 1.4;
            user-select: none;
        }}
        
        .code-with-lines {{
            overflow: hidden;
        }}
        
        .code-main {{
            margin-left: 60px;
            padding: 15px;
        }}
        
        .toc {{
            background-color: #f8f9fa;
            border: 1px solid #e9ecef;
            padding: 20px;
            margin-bottom: 30px;
            border-radius: 5px;
        }}
        
        .toc h2 {{
            margin-top: 0;
            color: #2c3e50;
            font-family: Arial, sans-serif;
        }}
        
        .toc ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        
        .toc li {{
            padding: 5px 0;
            border-bottom: 1px dotted #bdc3c7;
        }}
        
        .toc a {{
            text-decoration: none;
            color: #3498db;
        }}
        
        .toc a:hover {{
            text-decoration: underline;
        }}
        
        .stats {{
            background-color: #e8f5e8;
            border-left: 4px solid #27ae60;
            padding: 15px;
            margin-bottom: 20px;
        }}
        
        @media print {{
            body {{ margin: 20px; }}
            .file-section {{ page-break-after: auto; }}
            .code-block {{ page-break-inside: avoid; }}
        }}
    </style>
</head>
<body>
    <div class="header">
        <h1>Proyecto Métodos Numéricos</h1>
        <div class="info">
            Código fuente completo<br>
            Generado el: {datetime.now().strftime('%d/%m/%Y a las %H:%M')}<br>
            Total de archivos: {len(python_files)}
        </div>
    </div>
"""

    # Generar estadísticas
    total_lines = 0
    total_code_lines = 0
    
    # Tabla de contenidos
    html_content += """
    <div class="toc">
        <h2>📋 Índice de Archivos</h2>
        <ul>
"""
    
    for file_path in sorted(python_files):
        relative_path = os.path.relpath(file_path, project_root)
        file_id = relative_path.replace('\\', '_').replace('/', '_').replace('.', '_')
        html_content += f'            <li><a href="#{file_id}">{relative_path}</a></li>\n'
        
        # Contar líneas para estadísticas
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                total_lines += len(lines)
                code_lines = sum(1 for line in lines if line.strip() and not line.strip().startswith('#'))
                total_code_lines += code_lines
        except:
            pass
    
    html_content += """        </ul>
    </div>
"""
    
    # Estadísticas
    html_content += f"""
    <div class="stats">
        <strong>📊 Estadísticas del Proyecto:</strong><br>
        • {len(python_files)} archivos Python<br>
        • {total_lines} líneas totales<br>
        • {total_code_lines} líneas de código<br>
        • Aproximadamente {total_lines // 50} páginas (estimado)
    </div>
"""
    
    # Procesar cada archivo
    for file_path in sorted(python_files):
        relative_path = os.path.relpath(file_path, project_root)
        file_id = relative_path.replace('\\', '_').replace('/', '_').replace('.', '_')
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Escapar HTML
            content_escaped = html.escape(content)
            
            # Generar números de línea
            lines = content.split('\n')
            line_numbers = '\n'.join(str(i+1) for i in range(len(lines)))
            
            html_content += f"""
    <div class="file-section" id="{file_id}">
        <div class="file-header">📄 {os.path.basename(file_path)}</div>
        <div class="file-path">{relative_path} ({len(lines)} líneas)</div>
        <div class="code-block">
            <div class="code-with-lines">
                <div class="line-numbers">{line_numbers}</div>
                <div class="code-main">{content_escaped}</div>
            </div>
        </div>
    </div>
"""
            
        except Exception as e:
            html_content += f"""
    <div class="file-section" id="{file_id}">
        <div class="file-header">❌ {os.path.basename(file_path)}</div>
        <div class="file-path">{relative_path}</div>
        <div class="code-block">
            <div class="code-content">Error al leer el archivo: {str(e)}</div>
        </div>
    </div>
"""
    
    html_content += """
</body>
</html>
"""
    
    # Guardar el archivo HTML
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ Documento generado exitosamente!")
    print(f"📄 Archivo: {output_file}")
    print(f"📊 {len(python_files)} archivos procesados")
    print(f"📏 {total_lines} líneas totales")
    print(f"\n🔥 Pasos para convertir a PDF:")
    print("1. Abre el archivo codigo_completo.html en tu navegador")
    print("2. Presiona Ctrl+P para imprimir")
    print("3. Selecciona 'Guardar como PDF' como destino")
    print("4. En opciones de impresión:")
    print("   - Márgenes: Mínimos")
    print("   - Escala: 85-90% (para que quepa mejor)")
    print("   - Incluir gráficos de fondo: ✓")
    print("5. ¡Listo! Tendrás tu PDF con todo el código")
    
    return output_file

if __name__ == "__main__":
    generate_code_document()