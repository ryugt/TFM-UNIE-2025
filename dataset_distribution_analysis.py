import pandas as pd
import matplotlib.pyplot as plt

archivo_entrada = "cicids2017_clasificado_limpio.csv"

# 1. Cargar el dataset
df = pd.read_csv(archivo_entrada, encoding='ISO-8859-1', dtype=str)

# 2. Mostrar conteo absoluto de etiquetas
conteo = df['Label'].value_counts()
print("Conteo de ejemplos por clase:\n", conteo)

# 3. Mostrar porcentaje de cada clase
porcentaje = df['Label'].value_counts(normalize=True) * 100
print("\nPorcentaje por clase:\n", porcentaje)

# 4. Visualizar distribución
plt.figure(figsize=(12,6))
conteo.plot(kind='bar')
plt.title('Distribución de clases en el dataset')
plt.xlabel('Clase (Label)')
plt.ylabel('Cantidad de flujos')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(axis='y')
plt.show()
