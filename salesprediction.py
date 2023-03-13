import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Ridge
from sklearn.metrics import r2_score

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

# Definir las variables independientes (ventas pasadas)
X = df_sales.iloc[:, 1:].values

# Definir la variable dependiente (ventas futuras)
y = df_sales.iloc[:, 1].values

# Dividir los datos en conjuntos de entrenamiento y de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

# Crear un modelo de regresión ridge
regressor = Ridge(alpha=1.0)

# Entrenar el modelo con los datos de entrenamiento
regressor.fit(X_train, y_train)

# Predecir las ventas futuras utilizando los datos de prueba
y_pred = regressor.predict(X_test)

# Calcular el coeficiente de determinación (R^2) para evaluar el rendimiento del modelo
r2 = r2_score(y_test, y_pred)

# Mostrar el coeficiente de determinación
print('Coeficiente de determinación:', r2)
