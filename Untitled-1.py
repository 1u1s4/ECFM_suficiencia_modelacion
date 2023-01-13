import pandas as pd

def extraer(col_name: str, df: pd.DataFrame, num_hog: list) -> list:
    salida = []
    df[col_name] = df[col_name].fillna(0)
    for nh in num_hog:
        _nh = df.NUMHOG == nh
        i = df[_nh][col_name].mean()
        salida.append(i)
    return salida


#  Numero de hogar (key primaria)


df = pd.read_spss('data/PERSONAS.sav')
completas = df.PPA09 == 'COMPLETA'
df = df[completas]
num_hog = df.NUMHOG
num_hog = num_hog.to_list()
num_hog = tuple(set(num_hog))


# # Donaciones


df = pd.read_spss('data/DONACIONES.sav')


#  Pobreza de cada hogar


pobreza = []
for nh in num_hog:
    _nh = df.NUMHOG == nh
    pobreza_nh = df[_nh]['POBREZA'].iat[0]
    pobreza.append(pobreza_nh)


#  P01F03 (Si tuviera que comprar lo que recibio en los últimos 12 meses en donaciones, ¿cuánto cree que le costaría?)


P01F03 = []
for nh in num_hog:
    _nh = df.NUMHOG == nh
    i = df[_nh]['P01F03'].sum()
    P01F03.append(i)


# # Crédito


df = pd.read_spss('data/Compras al crédito - encabezado-.sav')


#  P15B02 (En los últimos 15 días, ¿cuál fue el monto total de sus compras al crédito en alimentos?)


P15B02 = []
for nh in num_hog:
    _nh = df.NUMHOG == nh
    i = df[_nh]['P15B02'].sum()
    P15B02.append(i)


#  P15B04 (¿Cuál fue el monto de sus compras al crédito de los bienes y artículos del hogar?)


P15B04 = []
for nh in num_hog:
    _nh = df.NUMHOG == nh
    i = df[_nh]['P15B04'].sum()
    P15B04.append(i)


#  P15B06A (Durante los ultimos 12 meses, cuantas compras al credito realizaron? (no. de compras))


P15B06A = []
for nh in num_hog:
    _nh = df.NUMHOG == nh
    i = df[_nh]['P15B06A'].sum()
    P15B06A.append(i)


# # Negocios No Agropecuarios


df = pd.read_spss('data/Negocios No Agropecuarios Encabezado.sav')


#  P13A02A (¿Cuántos comercios, negocios o fábricas tienen en éste hogar?)


P13A02A = []
for nh in num_hog:
    _nh = df.NUMHOG == nh
    i = df[_nh]['P13A02A'].sum()
    P13A02A.append(i)


# # Personas


df = pd.read_spss('data/PERSONAS.sav')


#  P06B01 (Sabe Leer Y Escribir?) total de sis


P06B01 = []
for nh in num_hog:
    _nh = df.NUMHOG == nh
    i = df[_nh]['P06B01']
    i = i.to_list().count('Si')
    P06B01.append(i)


#  P06B10A (Cuánto Tiempo Tarda (...) Para Ir Al Centro Educativo Donde Estudia? (Horas))


P06B10A = extraer('P06B10A', df, num_hog)


#  P06B10B (Cuánto Tiempo Tarda (...) Para Ir Al Centro Educativo Donde Estudia? (Minutos))


P06B10B = extraer('P06B10B', df, num_hog)


#  P09A03B (Horas Que Trabajó Ayer Sin Percibir Ingresos)


P09A03B = extraer('P09A03B', df, num_hog)


#  P09A03C (Minutos Que Trabajó Ayer Sin Percibir Ingresos)


P09A03C = extraer('P09A03C', df, num_hog)


#  P09B02B (Cuantas Horas Pasó En Transporte A Su Lugar De Estudios? (Ayer))


P09B02B = extraer('P09B02B', df, num_hog)


#  P09B02C (Cuantos Minutos Pasó En Transporte A Su Lugar De Estudios? (Ayer))


P09B02C = extraer('P09B02C', df, num_hog)


#  P09F03B (Horas Que Dedico A Trasladarse A Su Lugar De Trabajo Ayer)


P09F03B = extraer('P09F03B', df, num_hog)


#  P09F03C (Minutos Que Dedico A Trasladarse A Su Lugar De Trabajo Ayer)


P09F03C = extraer('P09F03C', df, num_hog)


#  P09F04B (Horas Que Dedicó A Descansar, Relajarse, Etc. Ayer)


P09F04B = extraer('P09F04B', df, num_hog)


#  P09F04B (Minutos Que Dedicó A Descansar, Relajarse, Etc. Ayer)


P09F04C = extraer('P09F04C', df, num_hog)


#  P09F05B (Horas Que Dedico A Actividades Deportivas, Culturales Etc. Fuera Del Hogar Ayer)


P09F05B = extraer('P09F05B', df, num_hog)


#  P09F05C (Minutos Que Dedico A Actividades Deportivas, Culturales Etc. Fuera Del Hogar Ayer) 


P09F05C = extraer('P09F05C', df, num_hog)


#  P09F06B (Horas Que Dedicó A Algún Trabajo Para Otros Hogares De Forma Gratuita Ayer) 


P09F06B = extraer('P09F06B', df, num_hog)


#  P09F06C (Minutos Que Dedicó A Algún Trabajo Para Otros Hogares De Forma Gratuita Ayer)


P09F06C = extraer('P09F06C', df, num_hog)


#  P09F07B (Horas Que Dedicó A Realizar Gestiones Para Mejoras De La Comunidad Etc. Ayer)


P09F07B = extraer('P09F07B', df, num_hog)


#  P09F07C (Minutos Que Dedicó A Realizar Gestiones Para Mejoras De La Comunidad Etc. Ayer)


P09F07C = extraer('P09F07C', df, num_hog)


#  P09F08B (Horas Que Dedicó A Lectura Recreativa De Algún Libro, Revista, Períodico Ayer)


P09F08B = extraer('P09F08B', df, num_hog)


#  P09F08C (Minutos Que Dedicó A Lectura Recreativa De Algún Libro, Revista, Períodico Ayer)


P09F08C = extraer('P09F08C', df, num_hog)


#  P09F09B (Horas Que Dedicó A Ver Tele, Escuchar Música, Utilizar Internet (Entretenimiento) Ayer)


P09F09B = extraer('P09F09B', df, num_hog)


#  P09F09C (Minutos Que Dedicó A Ver Tele, Escuchar Música, Utilizar Internet (Entretenimiento) Ayer)


P09F09C = extraer('P09F09C', df, num_hog)


#  P10B01 (Cuántos Trabajos Tuvo (?.) La Semana Pasada?)


P10B01 = extraer('P10B01', df, num_hog)


#  P10B08 (Cuál Fue El Sueldo O Salario Mensual Sin Descuentos De (...) En Este Trabajo?)


P10B08 = extraer('P10B08', df, num_hog)


#  P10B20B (Cuánto Le Costaría La Vivienda Por Mes Si Tuviera Que Aquilarla?) 


P10B20B = extraer('P10B20B', df, num_hog)


#  P11A05B (Cuanto Recibio (...) De Ayudas O Donaciones De Personas Ubicadas En Guatemala?)


P11A05B = extraer('P11A05B', df, num_hog)


#  P11A06B (Cuanto Recibio (...) Remesas De Personas Que Viven En El Extranjero?)


P11A06B = extraer('P11A06B', df, num_hog)


# # Union de datos


datos = {
    'pobreza':pobreza,
    'P01F03':P01F03,
    'P15B02':P15B02,
    'P15B04':P15B04,
    'P15B06A':P15B06A,
    'P13A02A':P13A02A,
    'P06B01':P06B01,
    'P06B10A':P06B10A,
    'P06B10B':P06B10B,
    'P09A03B':P09A03B,
    'P09A03C':P09A03C,
    'P09B02B':P09B02B,
    'P09B02C':P09B02C,
    'P09F03B':P09F03B,
    'P09F03C':P09F03C,
    'P09F04B':P09F04B,
    'P09F04C':P09F04C,
    'P09F05B':P09F05B,
    'P09F05C':P09F05C,
    'P09F06B':P09F06B,
    'P09F06C':P09F06C,
    'P09F07B':P09F07B, 
    'P09F07C':P09F07C,
    'P09F08B':P09F08B,
    'P09F08C':P09F08C,
    'P09F09B':P09F09B,
    'P09F09C':P09F09C,
    'P10B01':P10B01,
    'P10B08':P10B08,
    'P10B20B':P10B20B,
    'P11A05B':P11A05B,
    'P11A06B':P11A06B
}
df = pd.DataFrame(datos)


df.info()


df.to_csv('data/db.csv')


