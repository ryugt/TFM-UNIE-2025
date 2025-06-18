import json

# Diccionario de reemplazos directos
reemplazos = {
    "Flow Bytes/s": "Flow Bytes per second",
    "Flow Packets/s": "Flow Packets per second"
}

def reemplazar_semantico(texto):
    for original, nuevo in reemplazos.items():
        texto = texto.replace(original, nuevo)
    return texto

def procesar_jsonl(entrada, salida):
    with open(entrada, 'r', encoding='utf-8') as fin, \
         open(salida, 'w', encoding='utf-8') as fout:

        for linea in fin:
            registro = json.loads(linea)
            texto = registro.get("text", "")
            texto_limpio = reemplazar_semantico(texto)
            registro["text"] = texto_limpio
            json.dump(registro, fout, ensure_ascii=False)
            fout.write("\n")

    print(f"[OK] Archivo generado: {salida}")

# ✅ Aplicar a los archivos
procesar_jsonl("train.jsonl", "train_semantico.jsonl")
procesar_jsonl("val.jsonl", "val_semantico.jsonl")
#procesar_jsonl("test.jsonl", "test_semantico.jsonl")

