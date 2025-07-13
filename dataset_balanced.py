import pandas as pd

archivo_entrada = "cicids2017_clasificado_limpio.csv"
# 1. Cargar el dataset original
df = pd.read_csv(archivo_entrada, encoding='ISO-8859-1', dtype=str)

# --- 2. Agrupar ataques muy raros como 'ATAQUE_RARO' ---
ataques_raros = [
    'Heartbleed',
    'Web Attack ÃÂÃÂÃÂÃÂ Sql Injection',
    'Web Attack ÃÂÃÂÃÂÃÂ XSS',
    'Infiltration'
]

df['Label Agrupado'] = df['Label'].replace({ataque: 'ATAQUE_RARO' for ataque in ataques_raros})

# --- 3. Separar el dataset por grupos ---
try:
    df_benign = df[df['Label Agrupado'] == 'BENIGN'].sample(n=300000, random_state=42)
except ValueError:
    print("[ADVERTENCIA] Menos de 300 filas BENIGN, usando todas las disponibles.")
    df_benign = df[df['Label Agrupado'] == 'BENIGN']

df_comunes = df[df['Label Agrupado'].isin([
    'DoS Hulk',
    'PortScan',
    'DDoS',
    'DoS GoldenEye',
    'FTP-Patator',
    'SSH-Patator',
    'DoS slowloris',
    'DoS Slowhttptest',
    'Bot',
    'Web Attack ÃÂÃÂÃÂÃÂ Brute Force',
    'Fuzzers',
    'Reconnaissance',
    'Shellcode',
    'Analysis',
    'Backdoors',
    'DoS',
    'Exploits'
])]
df_raros = df[df['Label Agrupado'] == 'ATAQUE_RARO']

# --- 4. Sobremuestrear ataques raros (opcional, aquí se multiplica x50) ---
df_raros = pd.concat([df_raros]*50, ignore_index=True)

# --- 5. Concatenar todo ---
df_balanceado = pd.concat([df_benign, df_comunes, df_raros], ignore_index=True)

# --- 6. Mostrar distribución final ---
print("Distribución balanceada:\n", df_balanceado['Label Agrupado'].value_counts())

if 'Label' in df_balanceado.columns:
    df_balanceado = df_balanceado.drop(columns=['Label'])

# 2. Renombrar 'Label Agrupado' → 'label'
df_balanceado = df_balanceado.rename(columns={'Label Agrupado': 'label'})

# --- 7. Guardar el nuevo dataset balanceado ---
df_balanceado.to_csv("cicids2017_balanceado.csv", index=False)
print("[OK] Dataset balanceado guardado como 'cicids2017_balanceado.csv'")
