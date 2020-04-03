# Transform the data in the pdf to a pandas df using camelot

import pandas as pd
import camelot

root = r'C:\@Carlos\Data Science\Projects\COVID-19\isciii_pdf_reports'
file = r"C:\@Carlos\Data Science\Projects\COVID-19\isciii_pdf_reports\\55_COVID-19.pdf"

# Read pdf into list of DataFrame
tables = camelot.read_pdf(file, pages='all')

# print(tables[3].df)

n = 20
try:
    for i in range(n):
        print(tables[i].df)
except Exception as e:
    print("Error {}. No more tables".format(e))
