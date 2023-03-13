import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Definir los datos de ventas por mes para cada unidad de negocio
sales_data = np.array([
    [20003280, 24781840, 15283846, 15883110, 19382027, 22168441, 18562815, 29487262, 23164947, 27658287, 14819735, 18194791],
    [12000827, 13729130, 8513962, 9321818, 11465971, 13242435, 11043216, 18464923, 14520058, 17417628, 9187397, 11400504],
    [8000273, 10471109, 7288212, 6482677, 8762044, 10173186, 7190324, 12395639, 10239069, 11711005, 6319438, 7782017]
])
# Definir los meses del año
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
# Definir las unidades de negocio
business_units = ['Advertising', 'Hardware', 'Software']

# Crear una figura en 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Definir las posiciones de las barras en el gráfico
xpos = np.arange(len(business_units))
ypos = np.arange(len(months))
xpos, ypos = np.meshgrid(xpos, ypos)

# Aplanar los datos de ventas y convertirlos a una lista
zpos = np.zeros_like(ypos)
dz = sales_data.ravel().tolist()

# Definir el ancho y la profundidad de las barras
dx = 0.5
dy = 0.5

# Crear las barras en el gráfico
ax.bar3d(xpos.ravel(), ypos.ravel(), zpos.ravel(), dx, dy, dz)

# Establecer las etiquetas de los ejes y del gráfico
ax.set_xlabel('Unidad de negocio')
ax.set_xticks(np.arange(len(business_units)))
ax.set_xticklabels(business_units)
ax.set_ylabel('Mes')
ax.set_yticks(np.arange(len(months)))
ax.set_yticklabels(months)
ax.set_zlabel('Ventas')
ax.set_title('Ventas por unidad de negocio y mes')

# Mostrar el gráfico
plt.show()
