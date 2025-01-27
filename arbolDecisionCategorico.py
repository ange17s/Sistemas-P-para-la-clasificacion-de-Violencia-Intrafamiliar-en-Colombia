import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor, export_text
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('datasetViolencia\ViolenciaIntrafamiliarCol2015-2023.csv')

selected_columns = [
    'Año_del_hecho', 'Sexo_de_la_victima', 'CicloVital', 'TipodeDiscapacidad',
    'PertenenciaÉtnica', 'Mesdelhecho', 'Diadelhecho', 'RangodeHoradelHechoX3Horas',
    'ZonadelHecho','CircunstanciadelHecho', 'SexodelPresuntoAgresor', 'Días_de_Incapacidad_Medicolegal'
]

data = data[selected_columns]

data.fillna(data.median(), inplace=True)

#Manejo variables categóricas
label_encoders = {}
for col in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

X = data.drop('Días_de_Incapacidad_Medicolegal', axis=1)
y = data['Días_de_Incapacidad_Medicolegal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

tree = DecisionTreeRegressor(random_state=42, max_depth=5)
tree.fit(X_train, y_train)

# Generar reglas del árbol
tree_rules = export_text(tree, feature_names=list(X.columns))
print("Reglas del Árbol de Decisión:")
print(tree_rules)

def extract_rules(tree, feature_names):
    from sklearn.tree import _tree

    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    rules = []

    def recurse(node, depth, conditions):
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            recurse(tree_.children_left[node], depth + 1, 
                    conditions + [f"{name} <= {threshold:.2f}"])
            recurse(tree_.children_right[node], depth + 1, 
                    conditions + [f"{name} > {threshold:.2f}"])
        else:
            value = tree_.value[node][0][0]
            rules.append(f"Si {' AND '.join(conditions)}, entonces la clase es: {value:.2f}")

    recurse(0, 1, [])
    return rules

rules = extract_rules(tree, list(X.columns))
print("\nReglas en formato legible:")
for rule in rules:
    print(rule)

with open('reglas_arbol_decision.txt', 'w') as f:
    for rule in rules:
        f.write(rule + '\n')

# Evaluación del modelo (opcional)
train_score = tree.score(X_train, y_train)
test_score = tree.score(X_test, y_test)
print(f"Precisión en el conjunto de entrenamiento: {train_score:.2f}")
print(f"Precisión en el conjunto de prueba: {test_score:.2f}")