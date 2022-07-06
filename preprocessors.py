#''=== Scaling Features ===''
#  

"""
    Autor: Sandy Ajcabul
    Version: 1.0
    Descripcion: Se escalaron todas las funciones en data frame entre 0 y 1 usando MinMaxScaller, todas las caracteristicas estan dentro de esta escala para garantizar una división consistente de los datos de prueba y entrenamiento.
    esto asegura que se mantenga el equilibrio de las clases desde el conjunto de datos original hasta los datos de entrenamiento y testeo.
    """

from sklearn.preprocessing import MinMaxScaler
mm = MinMaxScaler()

X[columns]= mm.fit_transform(x[columns ])


""" 
====================== Data Split ======================
"""

"""
Autor: Preng Biba / Sandy Ajcabul
    Version: 1.0
    Descripcion: Para garantizar una división consistente de los datos de prueba y entreanmiento se usó la división aleatoria estratificada. Esto asegurará que se mantenga el equlibrio de las clases desde el conjunto de datos
    de entrenamiento/prueba.
    """


from sklearn.model_selection import train_test_split


df = pd.read_csv("X.csv")

X = df.drop(['col_name'], axis=1)
y = df['col_name']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, shuffle=True,  random_state=142)

dfSalida = instanciatePipeline(df, 'col_name').fit_transform(X_train, y_train)

dfSalida['col_name'] = pd.get_dummies(y, drop_first=True)



