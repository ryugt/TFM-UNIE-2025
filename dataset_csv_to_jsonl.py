import pandas as pd
import json

archivo_entrada = "cicids2017_balanceado.csv"
# 1. Cargar el dataset procesado y balanceado

df = pd.read_csv(archivo_entrada, encoding='ISO-8859-1', dtype=str)

# 2. Lista de features numéricos clave según el paper
features_numericos = [
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
    "Init_Win_bytes_forward"
]

# 3. Función para generar texto completo con semántica + features
def generar_texto(fila):
    texto_base = (
        f"flujo desde IP {fila['Source IP Class']} hacia IP {fila['Destination IP Class']} "
        f"usando {fila['Protocol Class']} en puerto {fila['Destination Port Class']}"
    )
    # Añadir features numéricos
    texto_features = ", ".join([f"{nombre} es {fila[nombre]}" for nombre in features_numericos if nombre in fila])
    return texto_base + ", " + texto_features

# 4. Generar nueva columna
df['text'] = df.apply(generar_texto, axis=1)

# 5. Preparar el dataset final
if 'target' in df.columns:
    df_final = df[['text', 'target']]
elif 'label' in df.columns:
    df_final = df[['text', 'label']].rename(columns={'label': 'target'})
else:
    raise KeyError("No se encontró la columna 'target' ni 'label' en el DataFrame.")

# 6. Exportar a JSONL
with open("cicids2017_autotrain_full.jsonl", "w", encoding='utf-8') as f:
    for _, row in df_final.iterrows():
        json.dump({"text": row['text'], "target": row['target']}, f, ensure_ascii=False)
        f.write('\n')

print("[OK] Dataset JSONL enriquecido guardado como 'cicids2017_autotrain_full.jsonl'")
