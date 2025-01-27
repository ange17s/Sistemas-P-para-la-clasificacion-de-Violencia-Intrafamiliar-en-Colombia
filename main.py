import re
import os
from membrane import Membrane
import chardet

def leer_reglas(archivo):

    try:

        with open(archivo, 'rb') as file:
            raw_data = file.read()
            result = chardet.detect(raw_data)
            encoding = result['encoding']
        
        with open(archivo, 'r', encoding=encoding) as file:
            reglas = file.readlines()
        return [regla.strip() for regla in reglas if regla.strip()]
    except FileNotFoundError:
        print(f"Error: El archivo {archivo} no fue encontrado.")
        return []
    except Exception as e:
        print(f"Error al leer el archivo {archivo}: {e}")
        return []

def transformar_a_membranas(reglas):
    """
    Transforma las reglas leídas a la sintaxis de computación por membranas.
    """
    reglas_membranas = []
    for regla in reglas:
        try:
            if ", entonces la clase es:" in regla:
                condiciones, accion = regla.split(", entonces la clase es:")
                condiciones = condiciones.replace("Si", "").strip()
                regla_membrana = f"[ {condiciones} ] -> [ {accion.strip()} ]"
                reglas_membranas.append(regla_membrana)
            else:
                print(f"Advertencia: Regla no válida: {regla}")
        except Exception as e:
            print(f"Error al transformar la regla: {regla}. Detalle: {e}")
    return reglas_membranas

def generar_escenarios_prueba(reglas_membranas):
    """
    Genera escenarios de prueba a partir de reglas transformadas.
    """
    escenarios = []
    for regla in reglas_membranas:
        try:
            if " -> " in regla:
                condiciones, clase = regla.split(" -> ")
                condiciones = condiciones.strip("[] ").replace("Si ", "")
                clase = clase.strip("[] ").strip()
                escenarios.append((condiciones, clase))
            else:
                print(f"Advertencia: La regla no contiene el formato esperado: {regla}")
        except Exception as e:
            print(f"Error al generar escenario para la regla: {regla}. Detalle: {e}")
    return escenarios

def probar_escenarios(membrana, escenarios, reglas_membranas):
    aciertos = 0

    for condiciones, resultado_esperado in escenarios:
        print(f"Probando escenario: {condiciones} -> {resultado_esperado}")

        condiciones_pares = []
        try:
            condiciones_pares = [cond.strip() for cond in condiciones.split("AND")]
        except Exception as e:
            print(f"Error al procesar las condiciones: {condiciones}. Detalle: {e}")
            continue

        for condicion in condiciones_pares:
            try:
                if ">" in condicion:
                    clave, valor = map(str.strip, condicion.split(">"))
                    membrana.add_object(clave, float(valor))
            except Exception as e:
                print(f"Error al agregar la condición: {condicion}. Detalle: {e}")

        print(membrana)

        resultado_predicho = membrana.get_classification(reglas_membranas)

        if resultado_predicho == resultado_esperado:
            aciertos += 1

        print(f"Resultado esperado: {resultado_esperado}\n")

    return aciertos

def guardar_resultados(nombre_archivo, contenido):
    """
    Guarda el contenido (lista de cadenas o tuplas) en un archivo de texto.
    """
    try:
        with open(nombre_archivo, "w", encoding="utf-8") as file:
            if contenido and isinstance(contenido[0], tuple):
                lineas = [f"{condiciones} -> {clase}" for condiciones, clase in contenido]
            else:
                lineas = contenido
            file.write("\n".join(lineas))
    except Exception as e:
        print(f"Error al guardar resultados en {nombre_archivo}: {e}")

def main():

    directorio = "./reglas_txt"

    todas_las_reglas = []
    for archivo in os.listdir(directorio):
        if archivo.endswith('.txt'):
            reglas = leer_reglas(os.path.join(directorio, archivo))
            todas_las_reglas.extend(reglas)

    # Transformar reglas a computación por membranas
    reglas_membranas = transformar_a_membranas(todas_las_reglas)
    guardar_resultados("reglas_membranas.txt", reglas_membranas)

    membrana_raiz = Membrane(None, "Raíz")

    escenarios = generar_escenarios_prueba(reglas_membranas)
    guardar_resultados("escenarios_prueba.txt", escenarios)

    # Probar escenarios y calcular aciertos
    aciertos = probar_escenarios(membrana_raiz, escenarios, reglas_membranas)

    # Análisis de los resultados (calculamos la exactitud)
    if len(escenarios) > 0:
        exactitud = (aciertos / len(escenarios)) * 100 
        print(f"Exactitud de las predicciones: {exactitud:.2f}%")
    else:
        print("No hay escenarios de prueba para evaluar.")

    print("Reglas transformadas y escenarios de prueba generados.")

if __name__ == "__main__":
    main()
