import json
import random
from collections import Counter
from pathlib import Path

# Rutas de entrada y salida
input_file = "train_semantico_enriched_en_ver2.jsonl"         # Cambia esta ruta si tu archivo está en otra carpeta
output_file = "train_semantico_enriched_en_balanced.jsonl"

# Leer el archivo original
with open(input_file, "r", encoding="utf-8") as f:
    data = [json.loads(line.strip()) for line in f]

# Contar cuántos ejemplos tiene cada clase
label_counts = Counter(entry["target"] for entry in data)
print("Distribución original de clases:")
for label, count in label_counts.items():
    print(f"{label}: {count}")

# Umbral mínimo por clase que deseamos alcanzar
MIN_SAMPLES_PER_CLASS = 5000

# Agrupar entradas por clase
class_entries = {}
for entry in data:
    class_entries.setdefault(entry["target"], []).append(entry)

# Oversampling: duplicar entradas de clases con menos de MIN_SAMPLES_PER_CLASS
balanced_data = data.copy()
for label, samples in class_entries.items():
    current_count = len(samples)
    if current_count < MIN_SAMPLES_PER_CLASS:
        needed = MIN_SAMPLES_PER_CLASS - current_count
        oversampled = random.choices(samples, k=needed)
        balanced_data.extend(oversampled)
        print(f"Clase '{label}' aumentada con {needed} ejemplos (total: {MIN_SAMPLES_PER_CLASS})")

# Mezclar el dataset para evitar agrupamientos por clase
random.shuffle(balanced_data)

# Guardar el nuevo dataset balanceado
with open(output_file, "w", encoding="utf-8") as f:
    for entry in balanced_data:
        f.write(json.dumps(entry) + "\n")

# Verificación final
balanced_counts = Counter(entry["target"] for entry in balanced_data)
print("\nDistribución después del balanceo:")
for label, count in balanced_counts.items():
    print(f"{label}: {count}")

print(f"\nDataset balanceado guardado en: {output_file}")
