# Día 1 — Fundamentos de análisis de datos

Ya tenía algunas bases con pandas. En esta sesión las reforcé trabajando con datos de ventas y aprendí nuevas formas de agrupar, resumir y analizar la información.

## Lo aprendido

- Agrupar datos con `groupby()` por producto o por fecha y usar `sum()` para obtener totales de cantidades e ingresos.
- Ordenar los resultados con `sort_values(ascending=False)` para ver los productos con mayores ingresos y con `sort_index()` para organizar las fechas cronológicamente.
- Crear la columna `ingreso` multiplicando `cantidad` por `precio_unitario`.
- Detectar valores faltantes con `isna()`, contarlos por columna con `isna().sum()` y filtrar las filas con cantidades o precios faltantes.
- Filtrar cantidades negativas e identificar que hace falta revisar si corresponden a devoluciones u otra situación.
- Convertir la columna de fechas con `pd.to_datetime()` y comprobar el cambio de tipo con `dtypes`.
- Encontrar la fecha con mayores ingresos mediante `idxmax()` y obtener su valor con `max()`.
- Comparar la suma de los ingresos agrupados por fecha con la suma de la columna `ingreso` para comprobar que coincidan.

También reforcé la creación de DataFrames desde diccionarios, la lectura de CSV con `pd.read_csv()` y la exploración de datos con `head()`, `shape`, `dtypes` e `info()`.

En el archivo quedaron como referencia, todavía comentados y sin ejecutar, los cálculos de participación porcentual por producto e ingreso promedio por unidad.

## Actividades

Bueno en la actividad 2 sobre el csv de ller archivos y utilizando funcion isna e info pude notar que al urtlizar info me da la cantidad de columnas que utlizan los distintos tipos de variabnles ya sea tipo str o int u otro y con la funcion isna pude notar que en algunas filas habian valores faltantes y con isna pude ver en cada columan cuantas habian y si ponia sum me mostraba esa suma por columna pero si no ponia sum me mostrat linea por linea y  en donde estaba el fatltna con tru y false
