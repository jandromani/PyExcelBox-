import pandas as pd
import os

# Definir la ruta del directorio que contiene los archivos de Excel
excel_dir = '/path/to/excel/directory/'

# Obtener la lista de archivos de Excel en el directorio
excel_files = [f for f in os.listdir(excel_dir) if f.endswith('.xlsx')]

# Para cada archivo de Excel, leerlo y convertirlo en un archivo JSON
for excel_file in excel_files:
    # Leer el archivo de Excel en un DataFrame de pandas
    df = pd.read_excel(os.path.join(excel_dir, excel_file))

    # Convertir el DataFrame en un archivo JSON y guardarlo en el mismo directorio
    df.to_json(os.path.join(excel_dir, excel_file.replace('.xlsx', '.json')), orient='records')
