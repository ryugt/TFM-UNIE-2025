import json

# Diccionario de reemplazo técnico → lenguaje natural en inglés
replacements_en = {
    "Flow Duration es": "the flow duration in microseconds was",
    "Total Fwd Packets es": "the total forwarding packets was",
    "Total Backward Packets es": "the total Backward Packets was",
    "Total Length of Fwd Packets es": "total Length of Forwarding Packets was",
    "Total Length of Bwd Packets es": "the total Length of Bwd Packets was",
    "Fwd Packet Length Max es": "the forwarding Packet Length maximum was",
    "Fwd Packet Length Mean es": "the forwarding Packet Length Mean was",
    "Bwd Packet Length Max es": "The backward Packet Length maximum was",
    "Bwd Packet Length Min es": "The backward Packet Length Minimum was",
    "Bwd Packet Length Std es": "the backward Packet Length standard was",
    "Flow Bytes per second es": "the Flow Bytes per second was",
    "Flow Packets per second es": "the Flow Packets per second was",
    "Flow IAT Mean es": "the Flow Inter-Arrival Time Mean was",
    "Flow IAT Std es": "Flow Inter-Arrival Time standard was",
    "Fwd IAT Mean es": "Fwd Inter-Arrival Time Mean was",
    "Fwd IAT Min es": "Fwd Inter-Arrival Time minimum was",
    "Bwd IAT Mean es": "Bwd Inter-Arrival Time Mean was",
    "Active Mean es": "the Active Mean was",
    "Idle Mean es": "the Idle Mean was",
    "Subflow Fwd Bytes es": "the Subflow Fwd Bytes was",
    "Init_Win_bytes_forward es": "the initial TCP window size was",
    "flujo":"flow",
    "desde":"from",
    "hacia":"to",
    "privada":"private",
    "publica":"public",
    "interna":"internal",
    "externa":"external",
    "en puerto":"on port",
    "usando":"using",
}

# Función para enriquecer el texto con lenguaje natural en inglés
def enrich_text_en(text):
    text = text.strip()
    if not text.startswith("classify a flow with the following characteristics:"):
        text = "classify a flow with the following characteristics: " + text
    for key, value in replacements_en.items():
        text = text.replace(key, value)
    return text

# Función principal para transformar el archivo
def enrich_dataset_jsonl(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as fin, \
         open(output_path, 'w', encoding='utf-8') as fout:
        
        for line in fin:
            record = json.loads(line)
            record["text"] = enrich_text_en(record["text"])
            json.dump(record, fout, ensure_ascii=False)
            fout.write('\n')
    
    print(f"[OK] Enriched English dataset saved to: {output_path}")

# ✅ Ejemplo de uso:
enrich_dataset_jsonl("test_semantico.jsonl", "test_semantico_enriched_en_ver2.jsonl")
