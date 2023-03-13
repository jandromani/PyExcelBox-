import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# Leer el archivo de Excel y seleccionar columnas necesarias
df = pd.read_excel('Financials Sample Data.xlsx', usecols=['Account', 'Businees Unit', 'Year', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

# Obtener la lista de cuentas, unidades de negocio y años únicos
accounts = df['Account'].unique()
business_units = df['Businees Unit'].unique()
years = df['Year'].unique()

# Iterar sobre cada cuenta, unidad de negocio y año, y generar un PDF para cada uno
for account in accounts:
    for business_unit in business_units:
        for year in years:
            # Seleccionar los datos correspondientes a la cuenta, unidad de negocio y año
            data = df[(df['Account'] == account) & (df['Businees Unit'] == business_unit) & (df['Year'] == year)]

            # Si no hay datos para la combinación cuenta/unidad de negocio/año, saltar a la siguiente combinación
            if data.empty:
                continue

            # Crear un gráfico de barras para los datos
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            sales_data = [data[month].sum() for month in months]

            fig, ax = plt.subplots()
            ax.bar(range(1, 13), sales_data)
            ax.set_xticks(range(1, 13))
            ax.set_xticklabels(months)
            ax.set_xlabel('Mes')
            ax.set_ylabel('Ventas')
            ax.set_title(f'Cuenta: {account}, Unidad de Negocio: {business_unit}, Año: {year}')

            # Guardar el gráfico en un archivo PDF
            with PdfPages(f'{account} - {business_unit} - {year}.pdf') as pdf:
                pdf.savefig()

            # Cerrar el gráfico
            plt.close()
