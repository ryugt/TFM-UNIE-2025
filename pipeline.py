# Guarda este código en un archivo llamado pipeline.py

import subprocess
import os
import time

# --- Nombres de los archivos intermedios y finales ---
# Puedes ajustar estos nombres si tus scripts usan otros por defecto.
FILE_JOINED = 'cicids2017_completo.csv'
FILE_CLEANED_1 = 'cicids2017_reducido.csv'
FILE_CLASSIFIED = 'cicids2017_clasificado.csv'
FILE_CLEANED_2 = 'cicids2017_clasificado_limpio.csv'
FILE_BALANCED = 'cicids2017_balanceado.csv'
FILE_JSONL = 'cicids2017_autotrain_full.jsonl'
BASE_STRATIFIED = ['train', 'val', 'test'] # Prefijos para los 3 archivos de salida

def run_script(script_name, description):
    """Función para ejecutar un script y manejar errores."""
    print(f"--- PASO: {description} ---")
    print(f"Ejecutando '{script_name}'...")
    try:
        # Ejecuta el script. check=True hace que falle si el script da un error.
        subprocess.run(['python', script_name], check=True)
        print(f"'{script_name}' completado con éxito.\n")
        time.sleep(1) # Pequeña pausa
    except FileNotFoundError:
        print(f"Error: No se encontró el script '{script_name}'. Asegúrate de que está en el mismo directorio.")
        exit()
    except subprocess.CalledProcessError:
        print(f"Error: El script '{script_name}' falló durante su ejecución.")
        exit()

def main():
    """Función principal que orquesta todo el pipeline."""
    start_time = time.time()
    print("🚀 Iniciando pipeline de procesamiento de datos...\n")

    # NOTA: Este pipeline asume que cada script ya sabe qué archivo de entrada
    # leer y qué archivo de salida escribir. Por ejemplo, que 'dataset_clean.py'
    # busca y lee el archivo generado por 'datasets_joiner.py'.

    # 1. Unión de CSVs
    run_script('datasets_joiner.py', 'Unión de archivos CSV del dataset')

    # 2. Primera limpieza
    run_script('dataset_clean.py', 'Primera limpieza de datos')

    # 3. Clasificación
    run_script('dataset_classification.py', 'Clasificación de datos')

    # 4. Segunda limpieza
    run_script('dataset_second_cleaning.py', 'Segunda limpieza de datos')

    # 5. Balanceo de datos
    run_script('dataset_balanced.py', 'Balanceo del dataset')

    # 6. Conversión de CSV a JSONL
    run_script('dataset_csv_to_jsonl.py', 'Conversión a formato JSONL')

    # 7. Estratificación (Train/Val/Test)
    run_script('dataset_stratification.py', 'Estratificación en train, val y test')

    # 8. Limpieza Semántica
    run_script('dataset_semantic_clean.py', 'Limpieza semántica de los sets')

    # 9. Enriquecimiento Semántico Final
    run_script('dataset_semantic_enricher_english_v2.py', 'Enriquecimiento semántico final')

    end_time = time.time()
    print(f"✅ Pipeline completado en {end_time - start_time:.2f} segundos.")
    print("Los archivos finales enriquecidos para el entrenamiento están listos.")


if __name__ == '__main__':
    main()