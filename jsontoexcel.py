import pandas as pd
import os

# Directorio que contiene los archivos de Excel
excel_dir = "ruta_del_directorio"

# Directorio donde se guardarán los archivos HTML
html_dir = "ruta_del_directorio_destino"

# Iterar sobre cada archivo de Excel en el directorio
for filename in os.listdir(excel_dir):
    if filename.endswith(".xlsx"):
        # Cargar el archivo de Excel en un DataFrame de pandas
        excel_file = os.path.join(excel_dir, filename)
        df = pd.read_excel(excel_file)
        
        # Generar el archivo HTML y guardarlo en el directorio de destino
        html_file = os.path.splitext(filename)[0] + ".html"
        html_path = os.path.join(html_dir, html_file)
        with open(html_path, "w") as f:
            f.write(df.to_html())
