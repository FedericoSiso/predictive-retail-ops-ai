import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

print("Cargando datos...")
# 1. Cargar el dataset (debe estar en la misma carpeta)
df = pd.read_csv('cafe_ventas_sinteticas.csv')
df['Fecha'] = pd.to_datetime(df['Fecha'])

# 2. División de datos
fecha_corte = df['Fecha'].max() - pd.Timedelta(days=90)
train_df = df[df['Fecha'] <= fecha_corte]
test_df = df[df['Fecha'] > fecha_corte]

features = ['Dia_Semana', 'Temp_Max_C', 'Lluvia', 'Promocion', 'Producto']
X_train = train_df[features]
y_train = train_df['Cantidad_Vendida']
X_test = test_df[features]
y_test = test_df['Cantidad_Vendida']

# 3. Construir el Pipeline
preprocesador = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(handle_unknown='ignore'), ['Dia_Semana', 'Producto'])
    ],
    remainder='passthrough'
)

modelo = Pipeline(steps=[
    ('preprocesador', preprocesador),
    ('regresor', GradientBoostingRegressor(random_state=42, n_estimators=100))
])

# 4. Entrenar el modelo
print("Entrenando el modelo con tu versión local de Python (3.11)...")
modelo.fit(X_train, y_train)

# Evaluar para comprobar que funciona
predicciones = modelo.predict(X_test)
mae = mean_absolute_error(y_test, predicciones)
print(f"📊 MAE Local: {mae:.2f} unidades")

# 5. Exportar el modelo
joblib.dump(modelo, 'modelo_cafe.joblib')
print("✅ ¡Listo! El archivo 'modelo_cafe.joblib' ha sido sobrescrito y es 100% compatible.")