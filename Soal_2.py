import pandas as pd 
from pandas import DataFrame, read_csv
import numpy as np 
dfProfesi = pd.read_csv('profesi.csv', delimiter = '|')

# # # No 1
Profesi= dfProfesi['occupation'].unique()
jumlahProfesi= dfProfesi['occupation'].nunique()
print (f'jumlah profesi : {jumlahProfesi}')
print (Profesi)


# No 2
dfHitung = dfProfesi.groupby([dfProfesi['occupation'],dfProfesi['gender']]).describe()
dfHitung = dfHitung['age'][['max','min','mean']]
dfHitung.rename(columns={'max':'max_usia','min':'min_usia','mean':'rerata_usia'},inplace=True)
print (dfHitung)

# No 3
gender = pd.crosstab(dfProfesi.occupation, dfProfesi.gender).apply(lambda i: i/i.sum(), axis= 1) *100
gender['%total'] = gender['F']+gender['M']
gender.rename(columns={'F':'%female','M':'%male'},inplace=True)
gender = gender[['%male','%female','%total']]
print(gender)

