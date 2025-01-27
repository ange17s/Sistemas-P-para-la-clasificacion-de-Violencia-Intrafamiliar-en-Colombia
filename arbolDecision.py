import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.tree import _tree

suicidios = pd.read_csv('datasetViolencia\intentoSuicidosEne2016Abr2023Santander.csv')

XS = suicidios.iloc[:, np.r_[3:17, 19:39]]

YS = suicidios.iloc[:, 18]

XS_train, XS_test, YS_train, YS_test = train_test_split(XS, YS, train_size=0.95, random_state=0)

arbolS = DecisionTreeClassifier(random_state=0, )

arbolSuicidios = arbolS.fit(XS_train, YS_train)

figS = plt.figure(figsize=(25, 20))
tree.plot_tree(
    arbolS,
    feature_names=list(XS.columns.values),
    class_names=[str(cls) for cls in arbolS.classes_], 
    filled=True
)
#plt.show()
figS.savefig("Arboldecicion.png")

# Predicción sobre el conjunto de prueba
YS_pred = arbolSuicidios.predict(XS_test)

# Matriz de confusión
matriz_de_Confusion = confusion_matrix(YS_test, YS_pred)
print("Matriz de Confusión:")
print(matriz_de_Confusion)

# Cálculo de precisión global
precision_global = np.sum(np.diagonal(matriz_de_Confusion)) / np.sum(matriz_de_Confusion)
print(f"Precisión global: {precision_global:.2f}")

# Cálculo de precisión para la clase "NO"
if np.sum(matriz_de_Confusion[0, :]) > 0:
    precision_no = matriz_de_Confusion[0, 0] / np.sum(matriz_de_Confusion[0, :])
    print(f"Precisión para la clase 'NO': {precision_no:.2f}")
else:
    print("No hay instancias de la clase 'NO' en el conjunto de prueba.")

# Cálculo de precisión para la clase "SI"
if len(matriz_de_Confusion) > 1 and np.sum(matriz_de_Confusion[1, :]) > 0:
    precision_si = matriz_de_Confusion[1, 1] / np.sum(matriz_de_Confusion[1, :])
    print(f"Precisión para la clase 'SI': {precision_si:.2f}")
else:
    print("No hay instancias de la clase 'SI' en el conjunto de prueba.")


def obtener_reglas_correctas(arbol, feature_names, XS_test, YS_test, YS_pred):
    tree_ = arbol.tree_
    reglas_correctas = []


    def recurse(node, rule="", samples_indices=None):
        if samples_indices is None:
            samples_indices = np.arange(len(XS_test))

        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            feature_name = feature_names[tree_.feature[node]]
            threshold = tree_.threshold[node]

            
            left_indices = samples_indices[XS_test.iloc[samples_indices, tree_.feature[node]] <= threshold]
            right_indices = samples_indices[XS_test.iloc[samples_indices, tree_.feature[node]] > threshold]

            left_rule = f"{rule} AND {feature_name} <= {threshold:.2f}" if rule else f"{feature_name} <= {threshold:.2f}"
            right_rule = f"{rule} AND {feature_name} > {threshold:.2f}" if rule else f"{feature_name} > {threshold:.2f}"

            recurse(tree_.children_left[node], left_rule, left_indices)
            recurse(tree_.children_right[node], right_rule, right_indices)
        else:
            class_name = tree_.value[node].argmax()
            class_label = arbol.classes_[class_name]
            node_samples = samples_indices

            # Verificar predicciones correctas
            for idx in node_samples:
                if YS_pred[idx] == YS_test.iloc[idx]:
                    reglas_correctas.append((rule, class_label))

    recurse(0)
    return reglas_correctas


# Obtener y guardar solo las reglas correctas
reglas_correctas = obtener_reglas_correctas(arbolSuicidios, XS.columns, XS_test, YS_test, YS_pred)

def guardar_reglas_en_txt(reglas, archivo="reglas_correctas.txt"):
    with open(archivo, 'w', encoding='utf-8') as f:
        for regla, clase in reglas:
            f.write(f"Si {regla}, entonces la clase es: {clase}\n")


guardar_reglas_en_txt(reglas_correctas, "reglas_correctas.txt")
print("Reglas correctas guardadas en 'reglas_correctas.txt'")