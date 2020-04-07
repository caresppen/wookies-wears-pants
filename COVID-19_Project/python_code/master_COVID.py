# master script to run all the code jobs generated in python

import COVID19_download
import CCAA_pdf_to_csv
import Demog_pdf_to_csv
import CCAA_csv_to_df_v2
import Demog_csv_to_df

root = r'Downloads'

# Running all the scripts:
COVID19_download
CCAA_pdf_to_csv
Demog_pdf_to_csv
CCAA_csv_to_df_v2
Demog_csv_to_df

print("All data cleaned & ready 2 plot!")
