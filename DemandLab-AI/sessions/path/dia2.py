import pandas as pd

df = pd.read_csv("DemandLab-AI/data/raw/ventas_techstore.csv")
# dropna() Esto elimina cualquier fila que tenga un valor faltante en alguna columna.
# usar subset para especifar que columasn con valores faltantes 
df_limpio = df.dropna(subset=["cantidad","precio_unitario"])
print(df_limpio)

duplicados = df.duplicated().sum()
print(duplicados)
print(f"productos con cantidades negativas: \n{df[df["cantidad"] < 0]}")
precios_invalidos = df[df["precio_unitario"] <= 0]
print(precios_invalidos)


#isna() identifica valores faltantes.
#any() comprueba si existe al menos un True.
#axis=1 realiza esa comprobación horizontalmente, fila por fila.

print(df.isna().sum())
print(df.isna().any(axis=1).sum())



filas_incompletas = df.isna().any(axis=1).sum()
print(filas_incompletas)

print(len(df))
print(len(df_limpio))

df_limpio.to_csv("demandLab-AI/data/processed/ventas_techstore.csv",index=False)

# Validaciones de calidad

assert len(df_limpio) < len(df)
assert  df_limpio[["cantidad", "precio_unitario"]].notna().any().any()

assert len(df) == 15 

valores = [True, True, False]
# any()	Al menos una condición es verdadera
# all()	Todas las condiciones son verdaderas
# Su función es detectar los valores válidos (no faltantes) 
# en un DataFrame o Serie, devolviendo True donde sí hay datos y False donde hay valores nulos
print(any(valores))  # True
print(all(valores))  # False

print(df["cantidad"].notna())
print(df["cantidad"].isna())


condicion = (
    df["cantidad"].isna() |
    df["precio_unitario"].isna()
)
# Esta condición identifica los registros donde falta la cantidad o el precio unitario.
# y si queremos los que no tengan valores faltantes solo agregameos ~antes de la condicion [~condicion]
df_rechazados = df[condicion]
print(df_rechazados)
df_aceptados = df[~condicion]

assert (len(df_rechazados) + len(df_aceptados)) == len(df)

df_rechazados.to_csv("demandLab-AI/data/processed/ventas_rechazadas.csv",index=False)