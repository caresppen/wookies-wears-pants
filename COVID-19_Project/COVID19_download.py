# Load COVID-19 data from the spanish government reports
# Download the information from the urls (pdf)

import pandas as pd
import request
import urllib.request

# Official reports format
url_i3 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%203_28febrero2020_ISCIII.pdf'
url_i4 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%204_02marzo2020_ISCIII.pdf'
url_i5 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%205_03marzo2020_ISCIII.pdf'
url_i6 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%206_05marzo2020_ISCIII.pdf'
url_i7 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%207_09marzo2020_ISCIII.pdf'
url_i8 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%208_11marzo2020_ISCIII.pdf'
url_i9 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%209_13marzo2020_ISCIII.pdf'
url_i10 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%2010_16marzo2020_ISCIII.pdf'
url_i11 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%2011_18marzo2020_ISCIII.pdf'
url_i12 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%2012_20marzo2020_ISCIII.pdf'
url_i13 = r'https://www.isciii.es/QueHacemos/Servicios/VigilanciaSaludPublicaRENAVE/EnfermedadesTransmisibles/Documents/INFORMES/Informes%20COVID-19/Informe%20COVID-19.%20N%C2%BA%2013_23marzo2020_ISCIII.pdf'

# Format of Spanish Ministry of Health links
url_ie = r'https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov-China/documentos/Actualizacion_54_COVID-19.pdf'

# Last available report
last = int(input("(Master) Ultimo reporte del Ministerio de Sanidad? "))

# Interacting with the user:
start = int(input("Introduce el primer reporte del Ministerio de Sanidad sobre el COVID-19 que deseas (primero disponible con datos de CCAA = 36): "))
end = int(input("Introduce el ultimo reporte del Ministerio de Sanidad sobre el COVID-19 que deseas (ultimo disponible con datos de CCAA = {}): ".format(last)))

# Defining a function to read all the Spanish COVID-19 Reports
def read_pdf_report(start, end):
    ''' Function to read data from COVID-19 Spanish reports:
        start = n starting report / end = n end report'''

    # Predefined format of the urls
    url_start = 'https://www.mscbs.gob.es/profesionales/saludPublica/ccayes/alertasActual/nCov-China/documentos/Actualizacion_'
    url_end = '_COVID-19.pdf'

    # Dealing with exceptions
    url_end_44 = '_COVID_1200.pdf'
    url_end_45 = '_COVID.pdf'

    print("download start!")

    for i in range(start, end+1):
        if i == 44:
            url = url_start + str(i) + url_end_44
        elif i == 45:
            url = url_start + str(i) + url_end_45
        else:
            url = url_start + str(i) + url_end

        chain = "Downloads\\" + \
            str(i) + "_COVID-19.pdf"

        try:
            urllib.request.urlretrieve(url, filename=chain)
            print(url)
        except Exception as e:
            print("Error {}. {}".format(e, url))

    print("download complete!")

# Using the function to obtain the reports.
# CCAA reported from 35.
# Report available from 30.
read_pdf_report(int(start), int(end))
