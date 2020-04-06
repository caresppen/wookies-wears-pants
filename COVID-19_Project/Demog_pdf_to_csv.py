# Transform the data in the pdf to a pandas df

# import COVID19_download
import pandas as pd
import tabula

root = r'Downloads'
dest = r'Downloads\root'

# Interacting with the user:
# last = COVID19_download.last
# start = COVID19_download.start
# end = COVID19_download.end

### Report per Table from the data source ###
### Tables format from Report 53 ###

# Tabla 2. Distribución de casos hospitalizados, ingresados en UCI y fallecidos por grupos de edad con datos notificados incluyendo edad y sexo (Total, Mujeres, Hombres), 3 tablas:
# df_edad_total: ["Edad", "Infectados", "Hospitalizados", "% Hospitalizados" - eliminate, "UCI", "% UCI" - eliminate, "Fallecidos", "% Fallecidos" - eliminate, "% Letalidad" - eliminate]
# df_edad_mujeres: ["Edad", "Infectados", "Hospitalizados", "% Hospitalizados" - eliminate, "UCI", "% UCI" - eliminate, "Fallecidos", "% Fallecidos" - eliminate, "% Letalidad" - eliminate]
# df_edad_hombres: ["Edad", "Infectados", "Hospitalizados", "% Hospitalizados" - eliminate, "UCI", "% UCI" - eliminate, "Fallecidos", "% Fallecidos" - eliminate, "% Letalidad" - eliminate]
first_doc = 67 # fixed to 53
last_doc = 67
df_dict = {}
for i in range(first_doc, last_doc + 1):
    try:
        pdf_doc = r'Downloads\\' + str(i) + '_COVID-19.pdf'
        table = tabula.read_pdf(pdf_doc, pages='all', multiple_tables=True)
        if (i == 57) or (i == 65):
            df_dict[i] = pd.DataFrame(table[2])
        else:
            df_dict[i] = pd.DataFrame(table[1])
        output = dest + '\\' + str(i) + '_Demog.csv'
        df_dict[i].to_csv(output, index=False)
    except Exception as e:
        print("Error {}".format(e))
    print(str(i) + "_Demog.csv generated to be explored!")
#print(df_dict[50])

# Table 3. Casos confirmados de COVID-19 en Europa: df_eu


# Tabla 4. Casos confirmados, IA de los últimos 14 días, nº de fallecidos y letalidad en los países más afectados de Europa: Not_needed


# Tabla 5. Casos confirmados, IA de los últimos 14 días, nº de fallecidos y letalidad en China, , Estados Unidos, Irán , Corea del Sur y a nivel global: df_global
