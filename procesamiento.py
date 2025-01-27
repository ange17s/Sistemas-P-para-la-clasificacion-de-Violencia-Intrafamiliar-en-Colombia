import pandas as pd

df = pd.read_csv('ViolenciaIntrafamiliarCol2015-2023.csv')

#df.info()

# Contar cuántas veces aparece cada valor único en la columna 'Categoría'
#print(df['Escolaridad'].value_counts())
#print(df['EstadoCivil'].value_counts())
#print(df['MunicipiodelhechoDANE'].value_counts())
#print(df['EscenariodelHecho'].value_counts())
#print(df['ActividadDuranteelHecho'].value_counts())
#print(df['CircunstanciadelHecho'].value_counts())
#print(df['MecanismoCausal'].value_counts())
#print(df['DiagnosticoTopográficodelaLesión'].value_counts())
#print(df['PresuntoAgresor'].value_counts())

#df['CircunstanciadelHecho'] = df['CircunstanciadelHecho'].str.strip().str.replace(',', '')
#df['CircunstanciadelHecho'] = df['CircunstanciadelHecho'].replace({'Violencia a niños niñas y adolescentes':'0', 'Violencia de pareja':'1','Violencia entre otros familiares':'2','Violencia al adulto mayor':'3','Educación media o secundaria alta':'4','Educación técnica profesional y tecnológica':'5','Universitario':'6','Especialización maestría o equivalente':'7','Doctorado o equivalente':'8'})

#print(df['CircunstanciadelHecho'].value_counts())

#df.drop(['Contextodeviolencia','Condición_de_la_Víctima','Medio_de_Desplazamiento_o_Transporte','Servicio_del_Vehículo','Clase_o_Tipo_de_Accidente','Objeto_de_Colisión','Servicio_del_Objeto_de_Colisión'], axis = 'columns', inplace= True)
# Limpiar espacios y caracteres adicionales en la columna 'Escolaridad'
#df['EstadoCivil'] = df['EstadoCivil'].str.strip().str.replace('"', '')
#print(df['EstadoCivil'].value_counts())
#df['Escolaridad'] = df['Escolaridad'].replace({'Sin escolaridad':'0', 'Educación inicial y educación preescolar':'1','Educación básica primaria':'2','Educación básica secundaria o secundaria baja':'3','Educación media o secundaria alta':'4','Educación técnica profesional y tecnológica':'5','Universitario':'6','Especialización maestría o equivalente':'7','Doctorado o equivalente':'8'})
#df['EstadoCivil'] = df['EstadoCivil'].replace({'Soltero (a)': '1', 'Unión libre': '2','Casado (a)':'3','Separado (a) divorciado (a)':'4','Viudo (a)':'5','No aplica':'0'})
#df['TipodeDiscapacidad'] = df['TipodeDiscapacidad'].replace({'Ninguna': '0', 'Física': '1','Mental':'1','Auditiva':'1','Visual':'1','Discapacidad Múltiple':'1','Psíquica':'1'})
#df['PertenenciaÉtnica'] = df['PertenenciaÉtnica'].replace({'Sin pertenencia étnica': '0', 'Negro/Afrodescendiente': '1','Indígena':'1','Raizal':'1','Palenquero':'1','ROM (Gitano)':'1'})

#df['SexodelPresuntoAgresor'] = df['SexodelPresuntoAgresor'].replace({'Hombre': '0', 'HOMBRE': '0','Mujer':'1','MUJER':'1','Transgenero':'2'})
#df['Días_de_Incapacidad_Medicolegal'] = df['Días_de_Incapacidad_Medicolegal'].replace({'1 a 30': '30', 'HOMBRE': '0','31 a 90':'90','Sin días de incapacidad':'0','Más de 90':'91'})
#df['Mesdelhecho'] = df['Mesdelhecho'].replace({'Enero': '01', 'Febrero': '02','Marzo':'03','Abril':'04','Mayo':'05','Junio':'06','Julio':'07','Agosto':'08','Septiembre':'09','Octubre':'10','Noviembre':'11','Diciembre':'12'})
#df['Diadelhecho'] = df['Diadelhecho'].replace({'Miércoles':'3','Sábado':'6'})
#df['RangodeHoradelHechoX3Horas'] = df['RangodeHoradelHechoX3Horas'].replace({'00:00 a 02:59': '259', '03:00 a 05:59': '559','06:00 a 08:59':'856','18:00 a 20:59':'2059','21:00 a 23:59':'2359','09:00 a 11:59':'1159','12:00 a 14:59':'1459','15:00 a 17:59':'1759'})
#df['ZonadelHecho'] = df['ZonadelHecho'].replace({'Cabecera municipal': '1', 'Parte rural (vereda y campo)': '2','Centro poblado(corregimiento, inspección de policía y caserío)':'3'})

#sin_dato_counts = df.select_dtypes(include='object').apply(
#    lambda col: col.str.contains("Colombia", case=False, na=False).sum()
#)

#print("Número de filas con 'sin dato' por columna:")
#print(sin_dato_counts)


#df = df[df != 'Por determinar'].dropna()

#print(df['prob_famil'].unique())  # Reemplaza con el nombre de la columna
#print(df['prob_famil'].dtype)    # Muestra el tipo de datos
#df['prob_famil'] = df['prob_famil'].astype(str)

#df['fecha_hecho'] = pd.to_datetime(df['fecha_hecho']).dt.date

df.to_csv('ViolenciaIntrafamiliarCol2015-2023.csv', index=False)