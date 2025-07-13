# TFM Dataset Process Pipeline

Este proyecto contiene un pipeline para el tratamiento, balanceo y transformación de datasets de tráfico de red, especialmente orientado al CICIDS2017. El objetivo es preparar los datos para tareas de clasificación y entrenamiento de modelos de machine learning.

## Estructura del pipeline

1. **Balanceo y agrupación de clases (`dataset_balanced.py`)**
   - Carga el dataset original (`cicids2017_clasificado_limpio.csv`).
   - Agrupa ataques muy raros bajo la etiqueta `ATAQUE_RARO`.
   - Separa el dataset en tres grupos: benignos, ataques comunes y ataques raros.
   - Realiza sobremuestreo de ataques raros para equilibrar la distribución.
   - Une todos los grupos y guarda el dataset balanceado como `cicids2017_balanceado.csv`.

2. **Conversión a formato JSONL enriquecido (`dataset_csv_to_jsonl.py`)**
   - Carga el dataset balanceado.
   - Genera una columna de texto descriptivo para cada flujo, combinando semántica y features numéricos clave.
   - Prepara el dataset final con las columnas `text` y `target` (o `label` si no existe `target`).
   - Exporta el resultado en formato JSONL para facilitar el entrenamiento en plataformas como Hugging Face AutoTrain.

## Uso

1. **Balancear el dataset**
   ```bash
   python dataset_balanced.py
   ```
   Esto genera el archivo `cicids2017_balanceado.csv`.

2. **Convertir a JSONL enriquecido**
   ```bash
   python dataset_csv_to_jsonl.py
   ```
   Esto genera el archivo `cicids2017_autotrain_full.jsonl`.

## Requisitos

- Python 3.x
- pandas

Instalación de dependencias:
```bash
pip install pandas
```

## Personalización

- Puedes modificar los scripts para ajustar el número de muestras, los ataques considerados como raros o comunes, y los features numéricos utilizados.
- El pipeline soporta datasets adicionales para aumentar ataques comunes si lo necesitas.

## Licencia

Este proyecto está licenciado bajo la licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contacto

Para dudas o mejoras, abre un issue en este repositorio.
