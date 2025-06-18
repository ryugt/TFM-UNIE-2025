import pandas as pd

# 1. Nombre del archivo de entrada
archivo_entrada = "cicids2017_clasificado.csv"


# 2. Columnas a conservar (features finales)
columnas_a_conservar = [
    "Source IP Class",
    "Destination IP Class",
    "Source Port Class",
    "Destination Port Class",
    "Protocol Class",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets",
    "Fwd Packet Length Max",
    "Fwd Packet Length Mean",
    "Bwd Packet Length Max",
    "Bwd Packet Length Min",
    "Bwd Packet Length Std",
    "Flow Bytes/s",
    "Flow Packets/s",
    "Flow IAT Mean",
    "Flow IAT Std",
    "Fwd IAT Mean",
    "Fwd IAT Min",
    "Bwd IAT Mean",
    "Active Mean",
    "Idle Mean",
    "Subflow Fwd Bytes",
    "Init_Win_bytes_forward",
    "Label"
]

# 3. Cargar el archivo completo (todo como texto)
df = pd.read_csv(archivo_entrada, encoding='ISO-8859-1', dtype=str, low_memory=False)


# 4. Filtrar solo las columnas que existen (por si acaso hay alguna ausencia)
columnas_presentes = [col for col in columnas_a_conservar if col in df.columns]

# 5. Subconjunto del DataFrame con las columnas deseadas
df_filtrado = df[columnas_presentes]

print(df_filtrado.columns)
input("Punto de control")

# 6. Guardar el resultado
df_filtrado.to_csv("cicids2017_clasificado_limpio.csv", index=False)

print(f"[OK] Archivo limpio guardado como 'cicids2017_clasificado_limpio.csv' con {len(columnas_presentes)} columnas.")
