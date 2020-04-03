### Report per Table from the data source ###

import COVID19_download
import pandas as pd
import numpy as np

output = r'Downloads'

ref_header = ["doc", "Edad", "Infectados", "Hospitalizados", "UCI", "Fallecidos", "Letalidad"]
df_master = pd.DataFrame(columns=["doc", "Edad", "Infectados", "Hospitalizados", "UCI", "Fallecidos"])

df_master_tot = df_master
df_master_muj = df_master
df_master_hom = df_master

# Interacting with the user:
last = COVID19_download.last
start = COVID19_download.start
end = COVID19_download.end

# Tabla 2. Características demográficas y clínicas de los casos de COVID-19 en España
# df_edad_total: ["Edad", "Infectados", "Hospitalizados", "% Hospitalizados" - eliminate, "UCI", "% UCI" - eliminate, "Fallecidos", "% Fallecidos" - eliminate, "% Letalidad" - eliminate]
# df_edad_mujeres: ["Edad", "Infectados", "Hospitalizados", "% Hospitalizados" - eliminate, "UCI", "% UCI" - eliminate, "Fallecidos", "% Fallecidos" - eliminate, "% Letalidad" - eliminate]
# df_edad_hombres: ["Edad", "Infectados", "Hospitalizados", "% Hospitalizados" - eliminate, "UCI", "% UCI" - eliminate, "Fallecidos", "% Fallecidos" - eliminate, "% Letalidad" - eliminate]
# Data from report 53
first = 53 # fixed to 53
last = end
# Error for 53-57 -> different cleanings
for i in range(first, last+1):
    root = r'Downloads\\' + \
        str(i) + '_Demog.csv'
    
    file = pd.read_csv(root, decimal=',', thousands='.')
    df_raw = pd.DataFrame(file)
  
    # Cleaning the raw dataframe
    df_raw = df_raw.dropna(axis='columns', thresh=1)
    df_raw['doc'] = i

    # Naming & setting the raw df columns
    if (i >= 58) and (i <= 60):
        df_raw.columns = ["Edad", "Infectados", "Hospitalizados", "UCI", "Fallecidos", "Letalidad", "doc"]
        df_raw = df_raw[ref_header]
        df_raw = df_raw.drop("Letalidad", axis=1)
    elif ((i >= 53) and (i <= 56)) or (i >= 61):
        df_raw.columns = ["Edad", "Infectados", "Hospitalizados", "UCI", "% UCI", "Fallecidos", "Letalidad", "doc"]
        df_raw = df_raw[["doc", "Edad", "Infectados", "Hospitalizados", "UCI", "% UCI", "Fallecidos", "Letalidad"]]
        df_raw = df_raw.drop(["% UCI", "Letalidad"], axis=1)
    elif (i == 57):
        df_raw.columns = ["Edad", "Infectados", "Hospitalizados", "UCI", "% UCI", "Fallecidos", "Letalidad", "% Letalidad", "doc"]
        df_raw = df_raw[["doc", "Edad", "Infectados", "Hospitalizados", "UCI", "% UCI", "Fallecidos", "Letalidad", "% Letalidad"]]
        df_raw = df_raw.drop(["% UCI", "Letalidad", "% Letalidad"], axis=1)
    # Defining each of the 3 df from the df_raw: df_dem_tot, df_dem_muj, df_dem_hom
    dem_type = ['tot', 'muj', 'hom']
    if i >= 58:    
        df_dem_tot = df_raw[4:14]
        df_dem_muj = df_raw[22:32]
        df_dem_hom = df_raw[39:49]
    elif (i == 53):
        df_dem_tot = df_raw[2:11]
        df_dem_muj = df_raw[16:25]
        df_dem_hom = df_raw[30:39]
    elif (i >= 54) and (i <= 56):
        df_dem_tot = df_raw[2:11]
        df_dem_muj = df_raw[18:27]
        df_dem_hom = df_raw[34:43]
    elif (i == 56):
        df_dem_tot = df_raw[2:12]
        df_dem_muj = df_raw[18:28]
        df_dem_hom = df_raw[34:44]
    elif (i == 57):
        df_dem_tot = df_raw[6:16]
        df_dem_muj = df_raw[23:33]
        df_dem_hom = df_raw[39:49]

### df_dem_tot ###

    # Manipulating and cleaning data: df['Hospitalizados']
    if (i == 58) or (i == 59):
        aux_hospit = df_dem_tot['Hospitalizados'].str.split(' ', n=2, expand=True)
        df_dem_tot['Hospitalizados'] = aux_hospit[0]
        df_dem_tot['UCI'] = aux_hospit[2]
    elif (i >= 53) and (i <= 57):
        aux_hospit = df_dem_tot['Hospitalizados'].str.split(' ', n=1, expand=True)
        df_dem_tot['Hospitalizados'] = aux_hospit[0]
    elif (i >= 60):
        aux_hospit = df_dem_tot['Hospitalizados'].str.split(' ', n=1, expand=True)
        aux_uci = df_dem_tot['UCI'].str.split(' ', n=1, expand=True)
        df_dem_tot['Hospitalizados'] = aux_hospit[0]
        df_dem_tot['UCI'] = aux_uci[0]      

    # Normalizing data for . and ,
    cols_w_dot = ["Infectados", "Hospitalizados", "UCI", "Fallecidos"]
    for col in cols_w_dot:
        df_dem_tot[col] = df_dem_tot[col].str.replace('.','')

    # Normalizing "Edad" to avoid 'Oct' on Excel
    df_dem_tot["Edad"] = df_dem_tot["Edad"].str.replace('80 y +', '80-89')
    df_dem_tot["Edad"] = df_dem_tot["Edad"].str.replace('+', '')
    df_dem_tot["Edad"] = df_dem_tot["Edad"].str.replace('90 y ', '90-+')
    df_dem_tot["Edad"] = df_dem_tot["Edad"].str.replace('-', '_')

    # Creating a summation of columns
    num_cols = ["Infectados", "Hospitalizados", "UCI", "Fallecidos"]
    df_dem_tot[num_cols] = df_dem_tot[num_cols].apply(pd.to_numeric, downcast='integer', errors='coerce')

    # Visualizing the sliced df
    # print(df_dem_tot)
    # print(df_dem_tot.info())

    # Generating the output
    out_master = output + '\\' + str(i) + '_Demog_tot_data.csv'
    df_dem_tot.to_csv(out_master, index=False)

### df_dem_muj ###

    # Manipulating and cleaning data: df['Hospitalizados']
    if (i == 58) or (i == 59):
        aux_hospit = df_dem_muj['Hospitalizados'].str.split(' ', n=2, expand=True)
        df_dem_muj['Hospitalizados'] = aux_hospit[0]
        df_dem_muj['UCI'] = aux_hospit[2]
    elif (i >= 53) and (i <= 57):
        aux_hospit = df_dem_muj['Hospitalizados'].str.split(' ', n=1, expand=True)
        df_dem_muj['Hospitalizados'] = aux_hospit[0]
    elif (i >= 60):
        aux_hospit = df_dem_muj['Hospitalizados'].str.split(' ', n=1, expand=True)
        aux_uci = df_dem_muj['UCI'].str.split(' ', n=1, expand=True)
        df_dem_muj['Hospitalizados'] = aux_hospit[0]
        df_dem_muj['UCI'] = aux_uci[0]     

    # Normalizing data for . and ,
    cols_w_dot = ["Infectados", "Hospitalizados", "UCI", "Fallecidos"]
    for col in cols_w_dot:
        df_dem_muj[col] = df_dem_muj[col].str.replace('.','')

    # Normalizing "Edad" to avoid 'Oct' on Excel
    df_dem_muj["Edad"] = df_dem_muj["Edad"].str.replace('80 y +', '80-89')
    df_dem_muj["Edad"] = df_dem_muj["Edad"].str.replace('+', '')
    df_dem_muj["Edad"] = df_dem_muj["Edad"].str.replace('90 y ', '90-+')
    df_dem_muj["Edad"] = df_dem_muj["Edad"].str.replace('-', '_')

    # Creating a summation of columns
    num_cols = ["Infectados", "Hospitalizados", "UCI", "Fallecidos"]
    df_dem_muj[num_cols] = df_dem_muj[num_cols].apply(pd.to_numeric, downcast='integer', errors='coerce')

    # Visualizing the sliced df
    # print(df_dem_muj)
    # print(df_dem_muj.info())

    # Generating the output
    out_master = output + '\\' + str(i) + '_Demog_muj_data.csv'
    df_dem_muj.to_csv(out_master, index=False)

### df_dem_hom ###

    # Manipulating and cleaning data: df['Hospitalizados']
    if (i == 58) or (i == 59):
        aux_hospit = df_dem_hom['Hospitalizados'].str.split(' ', n=2, expand=True)
        df_dem_hom['Hospitalizados'] = aux_hospit[0]
        df_dem_hom['UCI'] = aux_hospit[2]
    elif (i >= 53) and (i <= 57):
        aux_hospit = df_dem_hom['Hospitalizados'].str.split(' ', n=1, expand=True)
        df_dem_hom['Hospitalizados'] = aux_hospit[0]  
    elif (i >= 60):
        aux_hospit = df_dem_hom['Hospitalizados'].str.split(' ', n=1, expand=True)
        aux_uci = df_dem_hom['UCI'].str.split(' ', n=1, expand=True)
        df_dem_hom['Hospitalizados'] = aux_hospit[0]
        df_dem_hom['UCI'] = aux_uci[0] 

    # Normalizing data for . and ,
    cols_w_dot = ["Infectados", "Hospitalizados", "UCI", "Fallecidos"]
    for col in cols_w_dot:
        df_dem_hom[col] = df_dem_hom[col].str.replace('.','')

    # Normalizing "Edad" to avoid 'Oct' on Excel
    df_dem_hom["Edad"] = df_dem_hom["Edad"].str.replace('80 y +', '80-89')
    df_dem_hom["Edad"] = df_dem_hom["Edad"].str.replace('+', '')
    df_dem_hom["Edad"] = df_dem_hom["Edad"].str.replace('90 y ', '90-+')
    df_dem_hom["Edad"] = df_dem_hom["Edad"].str.replace('-', '_')

    # Creating a summation of columns
    num_cols = ["Infectados", "Hospitalizados", "UCI", "Fallecidos"]
    df_dem_hom[num_cols] = df_dem_hom[num_cols].apply(pd.to_numeric, downcast='integer', errors='coerce')

    # Visualizing the sliced df
    # print(df_dem_hom)
    # print(df_dem_hom.info())

    # Generating the output
    out_master = output + '\\' + str(i) + '_Demog_hom_data.csv'
    df_dem_hom.to_csv(out_master, index=False)

    # Create the 3 master files: demog_tot_data.csv ; demog_muj_data.csv ; demog_hom_data.csv
    df_master_tot = df_master_tot.append(df_dem_tot, sort=False)
    df_master_muj = df_master_muj.append(df_dem_muj, sort=False)
    df_master_hom = df_master_hom.append(df_dem_hom, sort=False)

    out_master_tot = output + '\demog_tot_data.csv'
    out_master_muj = output + '\demog_muj_data.csv'
    out_master_hom = output + '\demog_hom_data.csv'

    df_master_tot.to_csv(out_master_tot, index=False)
    df_master_muj.to_csv(out_master_muj, index=False)
    df_master_hom.to_csv(out_master_hom, index=False)

print("All demographic files (age, sex) have been generated!")