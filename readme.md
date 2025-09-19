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
- Se ha implemenbtado el patron de diseño **Mediador** para que todos los componentes de la interfaz puedan trabajar con una sola referencia, organizando y mejorando el codigo a futuro.
- Se ha cambiado la estructura del repositorio.
- EL uso de **customtkinter** es oficial.
- Se ha mejorado el concepto de la UI la cual esta disponible en **Figma**
- Para que el proyecto se pueda ejecutar se necesita un entorno virtual.

> Notas: 
> - Este readme sera modificado en los proximos commits

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