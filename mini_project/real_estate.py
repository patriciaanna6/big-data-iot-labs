import pandas as pd

df_home = pd.read_csv("Real_estate.csv")
df_home = pd.DataFrame(df_home)

no_rows = df_home.shape[0]
no_columns = df_home.shape[1]
#print(f"Antal rader: {rows}, Antal kolumner: {columns}")
#print(f"No. of rows: {rows}")
#print(f"No. of columns: {columns}")

df_home.head() #Visa de 5 första raderna, default
#print(df_home.head())

columns = list(df_home.columns) #Visa kolumnnamnen
print(columns)

#The data we have shows the pricing of real estate properties in Taiwan and the various factors that influence these prices.
#The X columns(input) in the dataset represents the factors. The Y column(output) represents the price of the property. Which means we are trying to predict the price of the property based on the factors given in the X columns.



