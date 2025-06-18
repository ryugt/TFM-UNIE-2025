import os 
import pandas as pd
import glob

carpeta="C:/Users/manue/Documents/Master Ciberseguridad/Trabajo Final de Master/Datasets/CICIDS2017/TrafficLabelling"


import pandas as pd
import os
import glob

archivos_csv = glob.glob(os.path.join(carpeta, '*.csv'))

print(f"Se encontraron {len(archivos_csv)} archivos.")

dataframes = []

# Leer todos los archivos
for idx, archivo in enumerate(archivos_csv):
    try:
        df = pd.read_csv(archivo, encoding='ISO-8859-1', low_memory=False, dtype=str)
        dataframes.append(df)
    except Exception as e:
        print(f"Error leyendo {archivo}: {e}")

# Concatenar
df_concatenado = pd.concat(dataframes, ignore_index=True)
df_concatenado.columns = df.columns.str.strip()
print(df_concatenado.columns)
input("punto de control")

# Guardar resultado
df_concatenado.to_csv('cicids2017_completo.csv', index=False)

print("Archivos combinados correctamente en 'cicids2017_completo.csv'.")


