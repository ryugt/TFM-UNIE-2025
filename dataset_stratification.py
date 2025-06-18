import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Cargar el dataset JSONL final con campos "text" y "label"
df = pd.read_json("cicids2017_autotrain_full.jsonl", lines=True)

# Verificar clases presentes
print("Distribución original de clases:")
print(df['target'].value_counts(normalize=True) * 100)

# 2. Primera división: 70% train, 30% temp (val + test)
train, temp = train_test_split(
    df,
    test_size=0.30,
    stratify=df['target'],
    random_state=42
)

# 3. Segunda división: dividir temp en 15% val y 15% test
val, test = train_test_split(
    temp,
    test_size=0.50,  # 50% de 30% = 15%
    stratify=temp['target'],
    random_state=42
)

# 4. Guardar los archivos en formato JSONL
train.to_json("train.jsonl", orient="records", lines=True, force_ascii=False)
val.to_json("val.jsonl", orient="records", lines=True, force_ascii=False)
test.to_json("test.jsonl", orient="records", lines=True, force_ascii=False)

print("[OK] Conjuntos generados correctamente:")
print(f" - train.jsonl: {len(train)} ejemplos")
print(f" - val.jsonl: {len(val)} ejemplos")
print(f" - test.jsonl: {len(test)} ejemplos")
