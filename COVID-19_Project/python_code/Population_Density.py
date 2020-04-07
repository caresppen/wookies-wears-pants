# Obtaining the population density data from Wikipedia

import pandas as pd
import requests
import lxml.html as lh

url = 'https://es.wikipedia.org/wiki/Anexo:Comunidades_y_ciudades_aut%C3%B3nomas_de_Espa%C3%B1a'
output = r'Downloads'

#Create a handle, page, to handle the contents of the website
page = requests.get(url)

#Store the contents of the website under doc
doc = lh.fromstring(page.content)

#Parse data that are stored between <tr>..</tr> of HTML
tr_elements = doc.xpath('//tr')

#Create empty list
col = []
i = 0
#For each row, store each first element (header) and an empty list
for t in tr_elements[1]:
    i += 1
    name = t.text_content()
    print(i,name)
    col.append((name,[]))

#Since out second row [1] is the header, data is stored on the third row onwards
for j in range(2, len(tr_elements)):
    #T is our j'th row
    T = tr_elements[j]
    #If row is not of size 10, the //tr data is not from our table 
    if len(T)!=10:
        break
    #i is the index of our column
    i = 0
    #Iterate through each element of the row
    for t in T.iterchildren():
        data = t.text_content() 
        #Check if row is empty
        if i > 0:
        #Convert any numerical value to float
            try:
                data = float(data)
            except:
                pass
        #Append the data to the empty list of the i'th column
        col[i][1].append(data)
        #Increment i for the next column
        i+=1

# Defining the dataframe
Dict = {title:column for (title,column) in col}
df = pd.DataFrame(Dict)

# Cleaning the dataset & selecting the necessary dataframe
df = df[['Nombre\n', 'Densidad(hab./km²)\n']]

dens_mapping = {'Nombre\n':'CCAA', 'Densidad(hab./km²)\n':'Densidad_Poblacion(hab./km²)'}
df = df.rename(columns=dens_mapping)

ccaa_mapping = {'Andalucía Andalucía':'Andalucia', 'Aragón Aragón':'Aragon', 'Principado de Asturias Principado de Asturias':'Asturias', 'Islas Baleares Islas Baleares':'Baleares', \
    'Comunidad Valenciana Comunidad Valenciana':'C. Valenciana', 'C. Valenciana':'C. Valenciana', 'Canarias Canarias':'Canarias', 'Cantabria Cantabria':'Cantabria', 'Castilla-La Mancha Castilla-La Mancha':'Castilla La Mancha', \
    'Castilla y León Castilla y León': 'Castilla y Leon', 'Cataluña Cataluña':'Catalunya', 'Ceuta Ceuta':'Ceuta', 'Extremadura Extremadura':'Extremadura', \
    'Galicia Galicia':'Galicia', 'La Rioja La Rioja':'La Rioja', 'Comunidad de Madrid Comunidad de Madrid':'Madrid', 'Melilla Melilla':'Melilla', 'Región de Murcia Región de Murcia':'Murcia', 'Navarra Navarra':'Navarra', 'País Vasco País Vasco':'Pais Vasco'}

ccaa_map = pd.Series(['Andalucia', 'Cataluña', 'Madrid', 'C. Valenciana', 'Galicia', 'Castilla y Leon', 'Pais Vasco', 'Canarias', 'Castilla La Mancha', 'Murcia', 'Aragon', 'Baleares', 'Extremadura', 'Asturias', 'Navarra', 'Cantabria', 'La Rioja', 'Ceuta', 'Melilla'])
df['CCAA'] = ccaa_map
df = df[['CCAA','Densidad_Poblacion(hab./km²)']]

df['Densidad_Poblacion(hab./km²)'] = df['Densidad_Poblacion(hab./km²)'].str.replace(',','.')
df['Densidad_Poblacion(hab./km²)'] = df['Densidad_Poblacion(hab./km²)'].apply(pd.to_numeric, downcast='float', errors='coerce').round(2)

print(df)

# Generating the output to be explored
out_master = output + '\\CCAA_pop_dens.csv'
df.to_csv(out_master, index=False)
print("CCAA_pop_dens.csv scraped from the url!")
