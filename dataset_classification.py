import pandas as pd
import ipaddress


puertos_comunes = {
    "20": "FTP",
    "21": "FTP",
    "22": "SSH",
    "23": "TELNET",
    "25": "SMTP",
    "53": "DNS",
    "80": "HTTP",
    "110": "POP3",
    "143": "IMAP",
    "443": "HTTPS",
    "445": "SMB",
    "3306": "MySQL",
    "8080": "HTTP_ALT"
}

protocolos = {
    "6": "TCP",
    "17": "UDP",
    "1": "ICMP"
}

# --- 1. Clasificación de IPs ---
def clasificar_ip(ip_str):
    try:
        ip_str = str(ip_str).strip()
        if ip_str in ["", "nan", "NaN"]:
            return None

        ip = ipaddress.ip_address(ip_str)

        # IPs especiales que se consideran internas públicas
        if ip_str in ["200.174.165.68", "200.174.165.66"]:
            return 'publica interna'
        elif ip_str=="172.16.0.1":
            return 'NAT interna'
        elif ip.is_private:
            return 'privada interna'
        elif ip_str.startswith("0."):
            return None # IP inválida
        else:
            return 'publica'
    except ValueError:
        return None  # IP inválida

# --- 2. Clasificación de puertos ---


def clasificar_puerto(port_str):
    try:
        port = int(port_str)

        # Primero, los puertos conocidos por nombre
        if str(port) in puertos_comunes:
            return puertos_comunes[str(port)]

        # Luego, por rango
        if 0 <= port <= 1023:
            return 'wellknown'
        elif 1024 <= port <= 49151:
            return 'registered'
        elif 49152 <= port <= 65535:
            return 'dynamic'
        else:
            return 'puerto_desconocido'
    except:
        return 'puerto_invalido'

def clasificar_protocolo(proto):
    return protocolos.get(str(proto).strip(), 'OTRO')



archivo_entrada = "cicids2017_reducido.csv"

# Cargar el dataset
df = pd.read_csv(archivo_entrada, encoding='ISO-8859-1', dtype=str, low_memory=False)

df['Source IP Class'] = df['Source IP'].apply(clasificar_ip)
df['Destination IP Class'] = df['Destination IP'].apply(clasificar_ip)

print(df.columns)
input("punto de control")

# Eliminar filas con IPs inválidas
df = df.dropna(subset=['Source IP Class', 'Destination IP Class'])

print(df.columns)
input("punto de control")

df['Source Port Class'] = df['Source Port'].apply(clasificar_puerto)
df['Destination Port Class'] = df['Destination Port'].apply(clasificar_puerto)

# --- 3. Clasificación del protocolo ---


df['Protocol Class'] = df['Protocol'].apply(clasificar_protocolo)

# --- 4. Guardar el resultado ---#

df.to_csv("cicids2017_clasificado.csv", index=False)
print("[OK] Dataset clasificado y guardado como 'cicids2017_clasificado.csv'")
