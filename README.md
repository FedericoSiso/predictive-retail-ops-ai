# ☕ Asistente Inteligente de Producción para Retail Gastronómico

Un sistema predictivo *end-to-end* diseñado para optimizar la planificación de inventario en cafeterías y restaurantes, transformando datos históricos en decisiones operativas rentables.

---

## 📊 El Caso de Negocio: El Costo de la Incertidumbre

En la industria gastronómica, la planificación diaria de la producción suele basarse en la intuición. Este enfoque genera dos problemas financieros críticos:
1. **Exceso de producción (Mermas):** Si se hornean 200 *croissants* y la demanda real es de 100, el 50% de la inversión se convierte en desperdicio.
2. **Quiebre de stock (Ventas Perdidas):** Si se preparan 50 unidades y la demanda supera las 100, se pierde el margen de ganancia de 50 ventas potenciales y se deteriora la experiencia del cliente.

**La Solución:** Este proyecto reemplaza las estimaciones manuales por un modelo de *machine learning* que analiza múltiples variables de negocio (día de la semana, clima, promociones) para proyectar la demanda exacta de cada producto.

---

## 💡 Propuesta de Valor y Rentabilidad (ROI)

La implementación de esta herramienta impacta directamente en el *Bottom Line* (beneficio neto) del negocio:
* **Reducción de Costos de Materia Prima:** Minimiza el desperdicio de productos perecederos al ajustar la producción diaria a proyecciones matemáticas.
* **Optimización de Recursos Humanos:** Permite anticipar picos de demanda (ej. días calurosos para bebidas frías) y ajustar la dotación de personal en el local.
* **Escalabilidad Estratégica:** Convierte un modelo estadístico complejo en una interfaz visual intuitiva (Cero fricción de adopción para dueños de locales o gerentes de sucursal).

---

## 🧠 Arquitectura Técnica y Modelado Predictivo

El núcleo analítico del proyecto fue construido en Python, utilizando **scikit-learn** para asegurar un entrenamiento robusto y replicable.

* **Algoritmo (Gradient Boosting):** Se entrenó un `GradientBoostingRegressor`. Este modelo de ensamble es ideal para capturar relaciones no lineales en negocios (por ejemplo, cómo un pico de 30°C un día sábado dispara exponencialmente la venta de *Iced Coffee*, pero hunde la demanda de *Hot Chocolate*).
* **Evaluación de Precisión:** El rendimiento del modelo se auditó utilizando el **Error Absoluto Medio (MAE)**. 
* **Traducción a Negocio:** Lograr un MAE de aproximadamente `6.7` unidades significa que, en promedio, el modelo se desvía por menos de 7 productos por día. Operativamente, este margen de error es mínimo y altamente rentable comparado con el riesgo de error humano.

---

## 🖥️ Interfaz de Usuario (Streamlit)

Para salir del entorno de *Jupyter Notebooks* y entregar una solución corporativa, el modelo predictivo fue integrado en una aplicación web interactiva usando **Streamlit**. 

Se diseñó una interfaz minimalista, con un esquema de alto contraste (Dark mode, acentos dorados y verdes) enfocada en la usabilidad gerencial. El usuario final solo necesita ingresar las condiciones climáticas y promocionales del día siguiente para obtener la cuota exacta de producción recomendada.

---

## ⚙️ Estructura del Proyecto y Ejecución

### Archivos Principales
* `generador_datos.py`: Script ETL que simula la lógica transaccional, variaciones estacionales y promocionales de una base de datos real.
* `entrenar.py`: Pipeline completo de Machine Learning (carga de datos, *Time Split*, *OneHotEncoding*, entrenamiento y serialización del modelo con *Joblib*).
* `app.py`: Frontend interactivo que consume el modelo pre-entrenado y despliega los resultados.
* `cafe_ventas_sinteticas.csv`: Dataset histórico de muestra (1 año de transacciones).
* `modelo_cafe.joblib`: Modelo entrenado y listo para predicciones en vivo.

### Instrucciones de Uso Local
1. Clona este repositorio:
   ```bash
   git clone [https://github.com/FedericoSiso/predictive-retail-ops-ai.git](https://github.com/FedericoSiso/predictive-retail-ops-ai.git)
   cd predictive-retail-ops-ai
