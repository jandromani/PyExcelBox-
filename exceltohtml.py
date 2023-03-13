import xlrd
import xml.etree.ElementTree as ET
import os

# Directorio con los archivos Excel
excel_dir = "path/to/excel/files"

# Directorio donde se guardarán los archivos XML
xml_dir = "path/to/xml/files"

# Función para convertir un archivo Excel a XML
def excel_to_xml(excel_file, xml_file):
    # Abrir el archivo Excel
    workbook = xlrd.open_workbook(excel_file)
    # Seleccionar la primera hoja del archivo
    worksheet = workbook.sheet_by_index(0)
    # Crear el elemento raíz del archivo XML
    root = ET.Element("data")
    # Recorrer todas las filas de la hoja
    for row_index in range(0, worksheet.nrows):
        # Crear un elemento para la fila
        row = ET.SubElement(root, "row")
        # Recorrer todas las celdas de la fila
        for col_index in range(0, worksheet.ncols):
            # Obtener el valor de la celda
            cell_value = worksheet.cell_value(row_index, col_index)
            # Crear un elemento para la celda y agregarlo a la fila
            cell = ET.SubElement(row, "cell")
            cell.text = str(cell_value)
    # Guardar el archivo XML
    tree = ET.ElementTree(root)
    tree.write(xml_file)

# Recorrer todos los archivos Excel en el directorio y convertirlos a XML
for filename in os.listdir(excel_dir):
    if filename.endswith(".xlsx") or filename.endswith(".xls"):
        excel_file = os.path.join(excel_dir, filename)
        xml_file = os.path.join(xml_dir, os.path.splitext(filename)[0] + ".xml")
        excel_to_xml(excel_file, xml_file)
