import os
import pandas as pd

# Especificar la ruta del directorio con los archivos CSV
csv_folder = 'ruta/del/directorio/csv'

# Especificar la ruta del directorio donde se guardarán los archivos de Excel
excel_folder = 'ruta/del/directorio/excel'

# Obtener la lista de archivos CSV en el directorio
csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

# Iterar a través de los archivos CSV y convertirlos a archivos de Excel
for csv_file in csv_files:
    # Obtener el nombre del archivo sin la extensión
    file_name = os.path.splitext(csv_file)[0]
    
    # Cargar el archivo CSV en un DataFrame de pandas
    csv_path = os.path.join(csv_folder, csv_file)
    df = pd.read_csv(csv_path)
    
    # Escribir el DataFrame en un archivo de Excel
    excel_path = os.path.join(excel_folder, f'{file_name}.xlsx')
    df.to_excel(excel_path, index=False)
