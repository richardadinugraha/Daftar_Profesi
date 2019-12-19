import pandas as pd 
from pandas import DataFrame, read_csv
import numpy as np 
dfProfesi = pd.read_csv('profesi.csv', delimiter = '|')

# # # No 1
# Profesi= dfProfesi['occupation'].unique()
# jumlahProfesi= dfProfesi['occupation'].nunique()
# print (f'jumlah profesi : {jumlahProfesi}')
# print (Profesi)


# No 2
ageTech=[]
for i in dfProfesi.loc[['technician'], ['occupation']] :
        age.append(dfProfesi.loc([i],['age']))
print(age)