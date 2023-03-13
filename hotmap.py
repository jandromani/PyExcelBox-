import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Definir los datos de ventas por mes para cada unidad de negocio
sales_data = {
    'Unit': ['Advertising', 'Hardware', 'Software'],
    'Jan': [20003280, 12000827, 8000273],
    'Feb': [24781840, 13729130, 10471109],
    'Mar': [15283846, 8513962, 7288212],
    'Apr': [15883110, 9321818, 6482677],
    'May': [19382027, 11465971, 8762044],
    'Jun': [22168441, 13242435, 10173186],
    'Jul': [18562815, 11043216, 7190324],
    'Aug': [29487262, 18464923, 12395639],
    'Sep': [23164947, 14520058, 10239069],
    'Oct': [27658287, 17417628, 11711005],
    'Nov': [14819735, 9187397, 6319438],
    'Dec': [18194791, 11400504, 7782017]
}

# Convertir los datos a un DataFrame de pandas
df_sales = pd.DataFrame(sales_data)

# Establecer el índice del DataFrame como la unidad de negocio
df_sales = df_sales.set_index('Unit')

# Crear un mapa de calor de las ventas por mes para cada unidad de negocio
sns.heatmap(df_sales, cmap='coolwarm', annot=True, fmt='d')

# Mostrar el mapa de calor
plt.show()
