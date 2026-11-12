# DemandLab AI

Proyecto educativo de 16 semanas para aprender análisis de datos, predicción de demanda y automatización empresarial con Python. La dedicación prevista es de 5 sesiones semanales de 2 horas: 80 sesiones y 160 horas en total.

El estudiante desarrollará los ejercicios y construirá el proyecto progresivamente con el acompañamiento de su mentor y un asistente de desarrollo.

## Objetivo y visión del sistema

Aprender a transformar datos de ventas en información útil para tomar decisiones empresariales: comprender los datos, detectar problemas de calidad, analizar ingresos y patrones de venta, y comunicar hallazgos.

A futuro, se espera construir un sistema capaz de recibir datos de ventas, preparar y validar esos datos, generar análisis, estimar la demanda y automatizar reportes. Estas capacidades son objetivos de aprendizaje; todavía no están implementadas.

## Estado inicial

Este repositorio contiene únicamente la estructura y la documentación iniciales. No incluye datasets, análisis, modelos, automatizaciones ni pruebas implementadas. El ejercicio del Día 1 está pendiente y su archivo Python contiene solo un comentario. El entorno virtual y las dependencias se prepararán manualmente con el mentor.

## Tecnologías

### Base de la etapa inicial

- Windows y Visual Studio Code: entorno de trabajo y editor.
- Python: lenguaje de programación.
- Pandas: única dependencia inicial declarada para trabajar con datos tabulares; aún no se ha instalado como parte de esta preparación.
- Git y GitHub: herramientas previstas para aprender control de versiones y colaboración. Esta preparación no inicializa un repositorio ni lo publica.

### Tecnologías futuras, sujetas al avance

- Matplotlib para visualizaciones.
- scikit-learn para introducir modelos predictivos y su evaluación.
- Herramientas de pruebas y programación de tareas cuando sean necesarias para validar y automatizar el trabajo.

Las dependencias futuras se evaluarán con el mentor y se añadirán solo cuando exista una necesidad concreta.

## Organización de carpetas

| Ruta | Utilidad |
| --- | --- |
| `docs/` | Notas, documentación y decisiones importantes del proyecto. |
| `data/raw/` | Datasets originales pequeños, sintéticos o públicos; conservarlos sin cambios para poder reproducir el trabajo. |
| `data/processed/` | Datos preparados o transformados durante ejercicios futuros. |
| `sessions/` | Ejercicios y registros de aprendizaje organizados por día; por ahora solo existe el Día 1. |
| `sessions/dia_01_fundamentos_analisis_datos/` | Objetivos, notas y archivo de trabajo del Día 1: fundamentos de análisis de datos. |
| `projects/` | Proyectos prácticos independientes, cada uno en su propia carpeta con su README; consultar la [guía de proyectos](projects/README.md). |
| `src/` | Futuros módulos reutilizables; actualmente solo contiene un `__init__.py` vacío. |
| `tests/` | Futuras pruebas del código desarrollado. |

Los archivos `.gitkeep` permiten conservar en Git las carpetas que todavía no tienen contenido. `AGENTS.md` establece las reglas del acompañamiento, `.gitignore` excluye archivos locales y `requirements.txt` declara únicamente Pandas, sin fijar una versión.

## Preparar el entorno en Windows

Estas instrucciones son para realizarlas manualmente como ejercicio con el mentor. No se han ejecutado durante la creación del esqueleto.

1. Tener Python y Visual Studio Code instalados. Abrir la carpeta `DemandLab-AI` en Visual Studio Code.
2. Abrir una terminal PowerShell en la raíz del proyecto, donde se encuentra este README, y comprobar Python:

   ```powershell
   python --version
   ```

3. Cuando corresponda en la sesión con el mentor, crear el entorno virtual:

   ```powershell
   python -m venv .venv
   ```

4. Activarlo en esa terminal:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Instalar manualmente la dependencia inicial dentro del entorno:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. En Visual Studio Code, con la extensión de Python disponible, usar **Python: Select Interpreter** y seleccionar `.venv\Scripts\python.exe`.
7. Leer `sessions/dia_01_fundamentos_analisis_datos/README.md` antes de comenzar el ejercicio. Escribir el código en `analisis_ventas.py`, dentro de esa misma carpeta, y registrar los aprendizajes en su README. Al terminar de trabajar, se puede salir del entorno con `deactivate`.

Si PowerShell impide activar el entorno, revisar el mensaje con el mentor antes de cambiar la configuración del sistema. La inicialización de Git y la publicación en GitHub serán ejercicios manuales independientes.

## Registro de progreso

Actualizar los registros al finalizar cada sesión con el trabajo realmente realizado. Añadir los siguientes días a medida que se trabajen, sin crear ejercicios anticipadamente.

### Por semana

Cada semana contempla cinco sesiones de dos horas. Ninguna sesión se considera completada todavía.

| Semana | Sesiones completadas | Estado |
| --- | --- | --- |
| 1 | 0/5 | Pendiente |
| 2 | 0/5 | Pendiente |
| 3 | 0/5 | Pendiente |
| 4 | 0/5 | Pendiente |
| 5 | 0/5 | Pendiente |
| 6 | 0/5 | Pendiente |
| 7 | 0/5 | Pendiente |
| 8 | 0/5 | Pendiente |
| 9 | 0/5 | Pendiente |
| 10 | 0/5 | Pendiente |
| 11 | 0/5 | Pendiente |
| 12 | 0/5 | Pendiente |
| 13 | 0/5 | Pendiente |
| 14 | 0/5 | Pendiente |
| 15 | 0/5 | Pendiente |
| 16 | 0/5 | Pendiente |

### Por día

| Semana | Día | Tema | Estado | Registro |
| --- | --- | --- | --- | --- |
| 1 | 1 | Fundamentos de análisis de datos | Pendiente | [Día 1](sessions/dia_01_fundamentos_analisis_datos/README.md) |
