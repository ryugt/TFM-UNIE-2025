import pandas as pd
from sklearn.model_selection import train_test_split

# 1. Cargar el dataset original
df = pd.read_json("train.jsonl", lines=True)

# 2. Crear un subconjunto estratificado de 60.000 ejemplos
subset, _ = train_test_split(
    df,
    train_size=60000,
    stratify=df['target'],
    random_state=42
)

# 3. Dividir ese subset en 50k train y 10k val
mini_train, mini_val = train_test_split(
    subset,
    test_size=10000,
    stratify=subset['target'],
    random_state=42
)

# 4. Guardar los archivos
mini_train.to_json("mini_train.jsonl", orient="records", lines=True, force_ascii=False)
mini_val.to_json("mini_val.jsonl", orient="records", lines=True, force_ascii=False)

print("[OK] mini_train (50k) y mini_val (10k) creados correctamente.")
