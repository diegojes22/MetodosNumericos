# 🧮 Métodos Numéricos – Scripts y Herramientas

Bienvenido a mi repositorio de **Métodos Numéricos**, un espacio donde almaceno todos mis scripts, algoritmos y proyectos relacionados con técnicas numéricas para resolución de problemas matemáticos y de ingeniería.  

Aquí encontrarás soluciones implementadas principalmente en **Python**, aunque también hay ejemplos en **Octave**, y algunos pequeños programas gráficos e interfaces para **visualizar y experimentar con los problemas**.

---

## 🔹 Contenido del Repositorio

- **Python**: Scripts y funciones para métodos numéricos clásicos como:
  - Resolución de ecuaciones no lineales
  - Sistemas de ecuaciones lineales
  - Interpolación y aproximación
  - Integración y derivación numérica
  - Métodos iterativos y de optimización
  - Métodos para ecuaciones diferenciales ordinarias (EDO)  

- **Octa**: Ejemplos rápidos de métodos numéricos para aprendizaje y comparación.  

- **Proyectos con interfaz / visualización**:  
  - Mini aplicaciones gráficas para explorar métodos numéricos
  - Gráficas interactivas para analizar convergencia, error y comportamiento de los algoritmos  

---

## ⚙️ Tecnologías utilizadas

- **Python**: Numpy, Scipy, Matplotlib, Tkinter (para interfaces simples)  
- **Octave / MATLAB**: Scripts educativos y comparativos  
- **Otras herramientas**: Pequeños programas gráficos para visualización y exploración  

---
# Novedades del commit
- Interfaz grafica de usuario completa en un 90%
- Correcion de errores menores con respecto a la eleccion de los modelos
- Refactorizacion interna del codigo

> Notas: 
> - Este readme sera modificado en los proximos commits
> - Proximamente se finalizara la version alpha para empezar con la beta.
----
# Sobre el entorno vitual
Es necesario crear un entorno virtual de la siguiente forma:
``` sh
python -m venv <nombre-del-entorno>
```
por ejemplo:
``` sh
python -m venv env
```

Lo siguiente es activar en entorno virtual de la siguiente forma:
* UNIX:
  ``` sh 
  # posiblemente debas de dar permisos de ejecucion con +x
  # o en caso de no ejecutarse deberas revisar que shell estas usando
  source env/bin/activate
  ```
* Windows:
  ``` sh 
  env\Scripts\activate
  ```

Una vez este activado el entorno virtual, deberas instalar las siguientes dependencias:
``` sh 
pip install pillow customtkinter tkinter
```

Para compilar el archivo `./SolverOne/main.py` se debe descargar el modulo de **PyInstaler**
y luego se debera ejecutar el siguiente comando:
```sh
 pyinstaller --onefile --windowed --name="SolverOne" --add-data "logic/*;logic/" --add-data "panels/*;panels/" --add-data "sources/*;sources/" --hidden-import="customtkinter" main.py
```