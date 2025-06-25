import json

# Diccionario de reemplazo técnico → lenguaje natural en inglés
replacements_en = {
    "Flow Duration es": "the total duration of the flow in microseconds was",
    "Total Fwd Packets es": "a total number of packets sent from source to destination was",
    "Total Backward Packets es": "the destination responded with a total number of packets of",
    "Total Length of Fwd Packets es": "the total bytes sent from source to destination was",
    "Total Length of Bwd Packets es": "the total bytes sent from destination back to source was",
    "Fwd Packet Length Max es": "the maximum size of packets sent from source was",
    "Fwd Packet Length Mean es": "the average size of forward packets in bytes was",
    "Bwd Packet Length Max es": "the maximum packet size received from destination in bytes was",
    "Bwd Packet Length Min es": "the smallest packet received in bytes was",
    "Bwd Packet Length Std es": "the standard deviation in packet sizes received was",
    "Flow Bytes per second es": "the byte transfer rate was",
    "Flow Packets per second es": "the number of packets transferred per second was approximately",
    "Flow IAT Mean es": "the average inter-arrival time between packets in microseconds was",
    "Flow IAT Std es": "the variation in inter-arrival time between packets was",
    "Fwd IAT Mean es": "the average inter-arrival time of packets sent from source was",
    "Fwd IAT Min es": "the shortest interval between packets sent from source was",
    "Bwd IAT Mean es": "the average inter-arrival time of packets from destination was",
    "Active Mean es": "the flow remained active for an average time of",
    "Idle Mean es": "the flow remained idle between transmissions for",
    "Subflow Fwd Bytes es": "in a single burst, the number of bytes sent was",
    "Init_Win_bytes_forward es": "the initial TCP window size in bytes was",
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
enrich_dataset_jsonl("train_semantico.jsonl", "train_semantico_enriched_en.jsonl")
