# Día 1: espacio de trabajo del estudiante.
import pandas as pd 

#ejemplo 1 


ventas = {
    "producto": ["Mouse", "Teclado", "Monitor"],
    "cantidad": [3, 2, 1],
    "precio": [50000, 90000, 650000]
}



def nuevo_producto(nombre, cantidad, precio):
    ventas["producto"].append(nombre)
    ventas["cantidad"].append(cantidad)
    ventas["precio"].append(precio)

nuevo_producto("Audífonos", 4, 120000)

datos_ventas = pd.DataFrame(ventas)
print(datos_ventas)


print(datos_ventas.shape)
print(datos_ventas.head())
print(datos_ventas.dtypes)

#parte 2
ventas = pd.read_csv("DemandLab-AI/data/raw/ventas_techstore.csv")

print(ventas.head())
ventas.info()
print(ventas.isna().sum())

ventas["ingreso"] = ventas["cantidad"] * ventas["precio_unitario"]
cant_faltante = ventas[ventas["cantidad"].isna()]
precio_faltante = ventas[ventas["precio_unitario"].isna()]
print(cant_faltante)
print(precio_faltante)

ingresos_por_producto = ventas.groupby("producto")["ingreso"].sum().sort_values(ascending=False)
print(ingresos_por_producto)

print(f"ventas con cantidades negativas que faltan por revisar si fueron devolucion u otra cosa: \n {ventas[ventas["cantidad"]<0]}")



#parte 3


print(ventas.dtypes)
ventas["fecha"] = pd.to_datetime(ventas["fecha"])
print(ventas.dtypes)

agrupar_por_fechas = ventas.groupby("fecha")["ingreso"].sum()
agrupar_por_fechas = agrupar_por_fechas.sort_index()

print(agrupar_por_fechas)
print(f"dia de ingreso maximo : \n{agrupar_por_fechas.idxmax()} el cual fue de {agrupar_por_fechas.max()}")
suma_por_fecha = agrupar_por_fechas.sum()
print(f"suma de ingreso por fecha: {suma_por_fecha} y suma de ingreso por producto: {ventas['ingreso'].sum()}")


cant_productos = ventas.groupby("producto")["cantidad"].sum()
venta_total  = ventas["ingreso"]
vehnta_total_productos = ventas.groupby("producto")["ingreso"].sum().sort_values(ascending=False)
print(cant_productos)
print(vehnta_total_productos)

#Fórmula de Participación (Peso de cada producto)



# 2. Agrupar por producto y sumar cantidades e ingresos
##resumen = ventas.groupby('producto', as_index=False)[['cantidad', 'ingreso']].sum()

# 3. Calcular el peso (%) de cada producto sobre el total
#resumen['Peso_Cantidad_%'] = (resumen['cantidad'] / resumen['cantidad'].sum()) * 100
#resumen['Peso_Ingreso_%'] = (resumen['ingreso'] / resumen['ingreso'].sum()) * 100
#
# 4. (Opcional) Calcular el ingreso promedio por unidad de cada producto
#resumen['Ingreso_Medio_Unidad'] = resumen['ingreso'] / resumen['cantidad']
#
# 5. Ordenar de mayor a menor peso en ingresos y redondear a 2 decimales
#resumen = resumen.sort_values(by='Peso_Ingreso_%', ascending=False).round(2)
#
##print(resumen)







