### Report per Table from the data source ###
import pandas as pd
import numpy as np

output = r'C:\@Carlos\Data Science\Projects\COVID-19\csv_report_tables'

ref_header = ['CCAA', 'Infectados', 'IA (14 d.)', 'Hospitalizados', 'UCI', 'Fallecidos', 'Curados', 'Nuevos']
df_master = pd.DataFrame(columns=['doc', 'CCAA', 'Infectados', 'Hospitalizados', 'UCI', 'Fallecidos', 'Curados', 'Nuevos'])
ccaa_mapping = {'Andalucía':'Andalucia', 'Aragón':'Aragon', 'Asturias':'Asturias', 'Baleares':'Baleares', \
    'C Valenciana':'C. Valenciana', 'C. Valenciana':'C. Valenciana', 'Canarias':'Canarias', 'Cantabria':'Cantabria', 'Castilla-La Mancha':'Castilla La Mancha', \
    'Castilla La Mancha':'Castilla La Mancha', 'Castilla y León': 'Castilla y Leon', 'Cataluña':'Catalunya', 'Ceuta':'Ceuta', 'Extremadura':'Extremadura', \
    'Galicia':'Galicia', 'La Rioja':'La Rioja', 'Madrid':'Madrid', 'Melilla':'Melilla', 'Murcia':'Murcia', 'Navarra':'Navarra', 'País Vasco':'Pais Vasco'}

# Tabla 1. Distribución de casos notificados de COVID-19 en España por CCAA
# To be cleaned -> [44, 45]; [51, 52]; [55, 56]
first = 36
last = 58
for e in range(first, last + 1):
    root = r'C:\@Carlos\Data Science\Projects\COVID-19\csv_report_tables\root\\' + \
        str(e) + '_CCAA.csv'
    
    file = pd.read_csv(root)
    df = pd.DataFrame(file)

    if (e == 44) or (e == 45):
        df = df.dropna(axis='columns', thresh=3)
        header = df.iloc[3]
        new_header = ['CCAA', 'Infectados', 'Fallecidos']
        df = df[4:]
        df = df.rename(columns = header)
        df = df.rename(columns = dict(zip(header, new_header)))
    elif ((e >= 36) and (e <= 50)):
        header = df.columns
        new_header = ['CCAA', 'Infectados', 'IA (14 d.)', 'UCI', 'Fallecidos']
        df = df.rename(columns= dict(zip(header, new_header)))
    if (e == 51) or (e == 52):
        header = df.iloc[0]
        new_header = ['CCAA', 'Infectados', 'IA (14 d.)', 'Hospitalizados', 'UCI', 'Fallecidos', 'Nuevos']
        df = df[2:]
        df = df.rename(columns = header)
        df = df.rename(columns = dict(zip(header, new_header)))
    elif ((e == 53) or (e == 54)):
        header = df.columns
        df = df.rename(columns = dict(zip(header, ref_header)))
    elif e >= 55:
        new_header = ['CCAA', 'Infectados', 'IA (14 d.)', 'Hospitalizados', 'UCI', 'Fallecidos', 'Curados', 'Nuevos']
        dict_header = dict(zip(df.columns,new_header))
        df = df[4:]
        df = df.rename(columns = dict_header)
    
    # Disregard '.' as commas for number formating
    try:
        num_cols = df.columns.drop(['CCAA', 'IA (14 d.)'])
        df[num_cols] = df[num_cols].apply(pd.to_numeric, downcast='integer', errors='coerce')
    except:
        num_cols = df.columns.drop('CCAA')
        df[num_cols] = df[num_cols].apply(pd.to_numeric, downcast='integer', errors='coerce')

    if (df.iloc[-1, 0] == 'ESPAÑA') or (df.iloc[-1, 0] == 'Total'):
        df = df.drop(df.tail(1).index)
    
    df = df.fillna(0)
    pv = pd.pivot_table(df, index=['CCAA'], margins=True, margins_name='Total', aggfunc=sum)
    # print(e)
    # print(pv)
    out = output + '\\' + str(e) + '_CCAA_cleaned.csv'
    pv.to_csv(out)

    # Add new column for a master file
    df['doc'] = e
    df_master = df_master.append(df, sort=False)

# Cleansing of the output dataset
df_master = df_master[['doc', 'CCAA', 'Infectados', 'Hospitalizados', 'UCI', 'Fallecidos', 'Curados', 'Nuevos']]
df_master['CCAA'] = df_master.CCAA.map(ccaa_mapping)

# Generating the output
out_master = output + '\CCAA_data.csv'
df_master.to_csv(out_master, index=False)

# Tabla 2. Características demográficas y clínicas de los casos de COVID-19 en España


# Table 3.  Casos de COVID-19 por grupos de edad y situación : N-casos, Hospitalizados, UCI, Defunciones, Letalidad


# Tabla 4. Antecedentes epidemiológicos de riesgo de los casos de COVID-19 en España


# Tabla 5. Características de los casos de COVID-19 en España, según presencia de neumonía


# Tabla 6. Características de los casos de COVID-19 en España, según nivel de gravedad
