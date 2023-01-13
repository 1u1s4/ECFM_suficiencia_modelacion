from boruta import BorutaPy
from sklearn import metrics
import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
 
df = pd.read_csv("data/db.csv")

print(df.describe().T)
print(df.isnull().sum())
df = df.dropna()

# Cambiar el nombre del conjunto de datos a Label para que sea fácil de entender
df = df.rename(columns={'pobreza':'Label'})
print(df.dtypes)

# Reemplazar valores categóricos con números
df['Label'].value_counts()

# Definir la variable dependiente que debe predecirse (Label)
y = df["Label"].values

# Codificación de datos categóricos
labelencoder = LabelEncoder()
Y = labelencoder.fit_transform(y)

# Definir x y normalizar valores
# Definir las variables independientes.
X = df.drop(labels = ["Label"], axis=1) 

feature_names = np.array(X.columns)

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

# Dividir los datos en train and test para verificar la precisión después de ajustar el modelo
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.25, random_state=42)

# Definir el clasificador XGBOOST para ser utilizado por Boruta
model = xgb.XGBClassifier()

"""
Crear funciones de sombra: funciones aleatorias y valores aleatorios en columnas
Entrenar Random Forest / XGBoost y calcular la importancia de la característica a través de la disminución media de la impureza
Comprobar si las características reales tienen mayor importancia en comparación con las características de sombra
Repetir esto para cada iteración
Si la función original funcionó mejor, marcarla como importante
"""

# definir el método de selección de características de Boruta
feat_selector = BorutaPy(model, n_estimators='auto', verbose=2, random_state=1)

# encontrar todas las características relevantes
feat_selector.fit(X_train, y_train)

# comprobar las características seleccionadas
print(feat_selector.support_)

# comprobar la clasificación de características
print(feat_selector.ranking_)

# llamar a transform() en X para filtrarlo a las características seleccionadas
X_filtered = feat_selector.transform(X_train)  # Aplicar selección de características y devolver datos transformados

"""
Revisar las características
"""
# zip nombres de características, rangos y decisiones
feature_ranks = list(zip(feature_names, 
                         feat_selector.ranking_, 
                         feat_selector.support_))

# imprimir los resultados
for feat in feature_ranks:
    print('Feature: {:<30} Rank: {},  Keep: {}'.format(feat[0], feat[1], feat[2]))

# Ahora usar el subconjunto de funciones para ajustar el modelo XGBoost en los datos de entrenamiento
xgb_model = xgb.XGBClassifier()
xgb_model.fit(X_filtered, y_train)

# Ahora predecir con datos de prueba usando el modelo entrenado
# Primero aplicar la transformación del selector de funciones para asegurarse de que se seleccionen las mismas funciones de los datos de prueba
X_test_filtered = feat_selector.transform(X_test)
prediction_xgb = xgb_model.predict(X_test_filtered)

# Imprimir precisión
print("Precisión = ", metrics.accuracy_score(y_test, prediction_xgb))
