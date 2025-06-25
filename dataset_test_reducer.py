import pandas as pd
from sklearn.model_selection import train_test_split

def reducir_jsonl_estratificado(archivo_entrada, archivo_salida, n_muestras, semilla=42):
    # 1. Cargar el archivo .jsonl
    df = pd.read_json(archivo_entrada, lines=True)

    print(f"\n📊 Distribución original de clases (total {len(df)} muestras):")
    dist_original = df['target'].value_counts(normalize=True) * 100
    print(dist_original.sort_index())

    # 2. Validar que el tamaño de muestra solicitado es válido
    if n_muestras >= len(df):
        print(f"[!] El archivo tiene solo {len(df)} muestras. No se necesita reducción.")
        df.to_json(archivo_salida, orient="records", lines=True, force_ascii=False)
        return

    # 3. Submuestreo estratificado
    df_reducido, _ = train_test_split(
        df,
        train_size=n_muestras,
        stratify=df['target'],
        random_state=semilla
    )
    # 4. Guardar el nuevo archivo
    df_reducido.to_json(archivo_salida, orient="records", lines=True, force_ascii=False)

    print(f"\n✅ Archivo reducido guardado como: {archivo_salida} ({len(df_reducido)} muestras)\n")

    # 5. Mostrar la nueva distribución de clases
    print("📊 Distribución de clases tras reducción:")
    dist_reducida = df_reducido['target'].value_counts(normalize=True) * 100
    print(dist_reducida.sort_index())

# ✅ Ejemplo de uso:
reducir_jsonl_estratificado("test_semantico_enriched_en_ver2.jsonl", "mini_test_semantico_enriched_en_ver2.jsonl", 2000)
