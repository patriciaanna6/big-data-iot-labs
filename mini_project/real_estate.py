import pandas as pd


#STEG 1 DATAINSAMLING

df_home = pd.read_csv("Real_estate.csv") 
df_home = pd.DataFrame(df_home)

no_rows = df_home.shape[0]
no_columns = df_home.shape[1]
#print(f"No. of rows: {rows}") 
#print(f"No. of columns: {columns}")

df_home.head() #Show the first rows (5 rows by default)
#print(df_home.head())

columns = list(df_home.columns) #show the column names
print(columns)

#The data we have shows the pricing of real estate properties in Taiwan and the various factors that influence these prices.
#The X columns(input) in the dataset represents the factors. The Y column(output) represents the price of the property. Which means we are trying to predict the price of the property based on the factors given in the X columns.


#STEG 2 DATARENSNING

#Checks for missing values per column 
print("Missing values per column:")
print(df_home.isna().sum())

#Checks for duplicates
print("Number of duplicates (entire rows that are copies):")
print(df_home.duplicated().sum())


#Show statistics for numerical columns
print("Statistics for numerical columns:")
print(df_home.describe())

# TODO: Kolla efter outliers (extremvärden)

