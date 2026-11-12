# Día 1 — Fundamentos de análisis de datos

**Estado: en progreso.** Mañana terminaré la evaluación.

Ya tenía algunas bases con pandas. Hoy las reforcé trabajando con datos de ventas y aprendí nuevas formas de agrupar y analizar la información.

## Lo aprendido

- **DataFrames y CSV:** crear una tabla con `pd.DataFrame()` y leer un CSV con `pd.read_csv()`. Repasé `head()`, `shape`, `dtypes` e `info()` para conocer los datos.
- **Agrupar y sumar:** usar `groupby()` para agrupar por producto o fecha y `sum()` para sumar cantidades e ingresos.
- **Valores faltantes:** detectarlos con `isna()` y contarlos por columna con `isna().sum()`.
- **Ordenar:** usar `sort_values(ascending=False)` para ver los ingresos de mayor a menor y `sort_index()` para ordenar por fecha.
- **Fechas:** convertirlas con `pd.to_datetime()`. Con `idxmax()` puedo encontrar la fecha del mayor ingreso y con `max()` ver ese valor.
- **Ingresos:** calcular `cantidad × precio_unitario` y guardar el resultado en una nueva columna. También comparé la suma por fecha con el total de ingresos.

## Notas para recordar

- Un valor faltante (`NaN`) no es lo mismo que cero. Si falta la cantidad o el precio, no puedo calcular el ingreso de esa fila. `sum()` omite los faltantes por defecto, así que el total puede estar incompleto.
- Una cantidad negativa puede ser un error, un ajuste o una devolución. Debo revisar su origen antes de sacar conclusiones o borrar el registro.
- Que las sumas coincidan no significa que todos los datos estén correctos. Tampoco debo confundir ingresos con beneficios: todavía faltaría descontar costos y gastos.
- La participación porcentual y el ingreso promedio por unidad quedaron comentados como referencia para revisar. Un promedio puede ser engañoso si incluye unidades cuyo precio falta.

## Actividades


Bueno, en la actividad 2, al leer el archivo CSV y utilizar las funciones `isna()` e `info()`, pude notar que `info()` me muestra las columnas, sus tipos de datos y cuántos valores no nulos tienen. También muestra cuántas columnas hay de cada tipo. Con `isna()` pude notar que en algunas filas había valores faltantes. Si ponía `isna().sum()`, me mostraba la cantidad de faltantes por columna, pero si no ponía `sum()`, me mostraba fila por fila dónde faltaba un valor con `True` y dónde no con `False`.


# Día 2 — Limpieza y calidad de datos

## ¿Qué aprendí?

Aprendí a identificar valores faltantes con `isna()` y `notna()`, detectar duplicados, filtrar cantidades negativas y utilizar `dropna()` con `subset` para eliminar registros incompletos en columnas específicas.

También aprendí a separar registros aceptados y rechazados mediante condiciones booleanas y a guardar los resultados en archivos CSV sin modificar los datos originales.

## Conceptos importantes

- `any()`: comprueba si al menos una condición es verdadera.
- `all()`: comprueba si todas las condiciones son verdaderas.
- `assert`: permite verificar condiciones durante la ejecución.
- `to_csv(index=False)`: exporta un DataFrame sin agregar el índice.

## Decisiones de limpieza

No todos los valores faltantes deben reemplazarse por cero. Tampoco debemos eliminar automáticamente las cantidades negativas, porque podrían representar devoluciones.

## Por mejorar

Necesito practicar más las validaciones automáticas y comprender mejor cuándo utilizar `any()` y `all()`.