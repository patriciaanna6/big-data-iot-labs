import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '../lab1-datainsamling/raw_iot.data.csv'
df = pd.read_csv(file_path)

df_home_home_home = pd.read_csv(file_path)
df_home_home = pd.read_csv(file_path)

# Visa de första raderna 
df_home_home_home.head()
#print(df_home_home_home.head())

df_home_home.info()
#print(df_home_home.info())

df_home_home.describe()
#print(df_home_home.describe())

#print("Saknade värden per kolumn\n")
#print(df_home_home.isna().sum())# isna().sum() räknar hur många NaN finns det i varje kolumn

print("Antal dubbletter (hela rader som är kopior):"), 
df_home_home.duplicated().sum()
print(df_home_home_home[df_home_home.duplicated()])# Visa dubbletterna



