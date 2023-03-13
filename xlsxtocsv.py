import pandas as pd
import os

# Ruta del directorio con los archivos Excel
excel_dir = 'ruta/a/directorio'

# Ruta del directorio donde se guardarán los archivos CSV
csv_dir = 'ruta/a/directorio/csv'

# Crear el directorio si no existe
if not os.path.exists(csv_dir):
    os.makedirs(csv_dir)

# Iterar sobre todos los archivos en el directorio
for filename in os.listdir(excel_dir):
    # Verificar que el archivo es de tipo Excel
    if filename.endswith('.xlsx') or filename.endswith('.xls'):
        # Cargar el archivo Excel en un DataFrame de Pandas
        excel_file = pd.read_excel(os.path.join(excel_dir, filename))
        # Escribir el DataFrame en un archivo CSV en el directorio de salida
        csv_filename = filename[:-5] + '.csv'  # Reemplazar la extensión del archivo
        csv_path = os.path.join(csv_dir, csv_filename)
        excel_file.to_csv(csv_path, index=False)  # Omitir la columna del índice
