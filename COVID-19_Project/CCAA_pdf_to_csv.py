# Transform the data in the pdf to a pandas df

import COVID19_download
import pandas as pd
import tabula

root = r'Downloads'
dest = r'Downloads'

# tabula - convert all PDFs in a directory (.pdf->.csv)
# tabula.convert_into_by_batch(root, output_format='csv', pages='all')

# Read pdf into list of DataFrame
# try:
#     init_list = tabula.read_pdf(file, pages='all', multiple_tables=True)
# except Exception as e:
#     print("Error {}".format(e))

# df = pd.DataFrame(init_list)
# print(init_list[1])

# Interacting with the user:
last = COVID19_download.last
start = COVID19_download.start
end = COVID19_download.end

### Report per Table from the data source ###
### Tables format from Report 53 ###
# Tabla 1. Casos COVID-19, incidencia acumulada (IA) en los últimos 14 días, ingreso en UCI y fallecidos por Comunidades Autónomas en España: df_ccaa
# columns = [CCAA, TOTAL conf. == Infectados, IA (14 d.), Hospitalizados, UCI, Fallecidos, Curados, Nuevos]
first_doc = start # 36
last_doc = end # 60
df_dict = {}
for i in range(first_doc, last_doc + 1):
    try:
        pdf_doc = r'Downloads\\' + str(i) + '_COVID-19.pdf'
        table = tabula.read_pdf(pdf_doc, pages='all', multiple_tables=True)
        if (((i >= 36) and (i <= 43)) or ((i == 46) or (i == 52))):
            n = 1
        elif ((i == 44) or (i == 45)) or (i >= 47 and i <= 51) or (i >= 53):
            n = 0
        df_dict[i] = pd.DataFrame(table[n])
        # print(str(i) + "_COVID-19.pdf")
        # print(n)
        # print(table[n])
        output = dest + '\\' + str(i) + '_CCAA.csv'
        df_dict[i].to_csv(output, index=False, decimal=',')
    except Exception as e:
        print("Error {}".format(e))
    print(str(i) + "_CCAA.csv generated to be explored!")
#print(df_dict[50])
# To be cleaned -> [44, 45]; [51, 52]; [55, 56]

# Tabla 2. Distribución de casos hospitalizados, ingresados en UCI y fallecidos por grupos de edad con datos notificados incluyendo edad y sexo (Total, Mujeres, Hombres), 3 tablas: df_edad_sexo


# Table 3. Casos confirmados de COVID-19 en Europa: df_eu


# Tabla 4. Casos confirmados, IA de los últimos 14 días, nº de fallecidos y letalidad en los países más afectados de Europa: Not_needed


# Tabla 5. Casos confirmados, IA de los últimos 14 días, nº de fallecidos y letalidad en China, , Estados Unidos, Irán , Corea del Sur y a nivel global: df_global
