import pandas as pd
import numpy as np
from datetime import timedelta, date

# Configuración inicial
np.random.seed(42)
start_date = date(2024, 1, 1)
dias_totales = 365
productos = ['Croissant', 'Iced Coffee', 'Sandwich', 'Banana Bread', 'Hot Chocolate']

# Generar fechas y variables diarias
fechas = [start_date + timedelta(days=i) for i in range(dias_totales)]
datos_diarios = []

for fecha in fechas:
    dia_semana = fecha.strftime('%A')
    # Simular clima estacional (más calor a principio y fin de año en el hemisferio sur)
    mes = fecha.month
    temp_base = 25 if mes in [11, 12, 1, 2, 3] else 15
    temp_max = int(np.random.normal(temp_base, 4))
    
    # Probabilidad de lluvia (15%) y promociones (solo fines de semana o aleatorio)
    lluvia = 1 if np.random.rand() < 0.15 else 0
    promocion = 1 if (dia_semana in ['Friday', 'Saturday'] and np.random.rand() < 0.5) else 0
    
    datos_diarios.append({'Fecha': fecha, 'Dia_Semana': dia_semana, 'Temp_Max_C': temp_max, 'Lluvia': lluvia, 'Promocion': promocion})

df_dias = pd.DataFrame(datos_diarios)

# Expandir para cada producto y calcular ventas
datos_finales = []

for _, row in df_dias.iterrows():
    for producto in productos:
        # Ventas base aleatorias
        ventas = np.random.normal(30, 5)
        
        # Multiplicadores de negocio
        if row['Dia_Semana'] in ['Saturday', 'Sunday']:
            ventas *= 1.5 # Más ventas los fines de semana
            
        if row['Promocion'] == 1:
            ventas *= 1.3 # Impulso por promoción
            
        # Lógica específica por producto y clima
        if producto == 'Iced Coffee':
            if row['Temp_Max_C'] > 25: ventas *= 1.8
            if row['Temp_Max_C'] < 15: ventas *= 0.4
        elif producto == 'Hot Chocolate':
            if row['Temp_Max_C'] < 18 or row['Lluvia'] == 1: ventas *= 1.7
            if row['Temp_Max_C'] > 25: ventas *= 0.2
        elif producto == 'Croissant':
            if row['Dia_Semana'] in ['Saturday', 'Sunday']: ventas *= 1.4 # Clásico de fin de semana
        elif producto == 'Sandwich':
            if row['Dia_Semana'] not in ['Saturday', 'Sunday']: ventas *= 1.2 # Consumo de oficinistas
            
        # Añadir algo de ruido y redondear
        ventas = max(0, int(ventas + np.random.normal(0, 3)))
        
        fila = row.to_dict()
        fila['Producto'] = producto
        fila['Cantidad_Vendida'] = ventas
        datos_finales.append(fila)

# Crear DataFrame final y exportar
df_ventas = pd.DataFrame(datos_finales)
df_ventas.to_csv('cafe_ventas_sinteticas.csv', index=False)

print(f"Dataset generado con éxito. Total de filas: {len(df_ventas)}")
print(df_ventas.head(10))