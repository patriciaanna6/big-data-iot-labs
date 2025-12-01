import pandas as pd

"""
fitness = pd.read_csv("../data/iot_fitness.csv")

df_fitness = pd.DataFrame(fitness)

print(df_fitness.head(), "\n") # ger oss de första fem raderna av data
print(df_fitness.tail(),"\n") # ger oss sista raderna
print(df_fitness.shape, "\n")  # formen på dataframe
print(df_fitness.size, "\n")   # storleken på dataframe
print(df_fitness.columns, "\n")# ger columner i dataframe

# Visar vilka datatyper vår dataframe innehåller
df_fitness.info()

# Visar statistik
df_fitness.describe()

# Sample ger oss random data
df_fitness.sample(10)

# loc ger oss filter data,
df_fitness.loc[1,2]  # visar andra och tredje raden i dataframe
df_fitness.loc[1:5]  # visar rad 1 till 5
df_fitness.loc[1:]   # visar rad 1 och alla rader efter 1
df_fitness.loc[4:20,["Calories_Burned"]] # visar Calories_Burned för rad 4 till 20

df_fitness.head()

# om vi vill ändra value för en specifik kolumn
df_fitness.loc[10,"Calories_Burned"] = 400

# vi kan komma åt datan i en kolumn
df_fitness["Calories_Burned"]

# visa och sortera värden i en kolumn
df_fitness.sort_value("Calories_Burned") # visar värden i ökande order
df_fitness.sort_value("Calories_Burned", ascending =False) # visar värden i fallande order

# visa värden för en kolumn som följer viss regel
selected_rows = df_fitness.loc[df_fitness["Calories_Burned"] < 500]

"""
df_home = pd.read_csv("../data/raw_energydata.csv")
df_home = pd.DataFrame(df_home)

df_home.size
df_home.head()

# datatyper,minne och nullvärden
df_home.info()

# statistik sammanfattning
df_home.describe()


# antal rader och kolumner
df_home.shape

# kolumnnamn
df_home.columns

# tittar på datakvalitet
# Problem 1: Saknade värden
saknade_per_kolumn = df_home.isnull().sum()
saknade_totalt = saknade_per_kolumn.sum()
print(f" SAKNADE VÄRDEN: {saknade_totalt} totalt")
for kolumn, antal in saknade_per_kolumn[saknade_per_kolumn > 0].items():
    print(f"  • {kolumn}: {antal} saknade")

if isinstance(df_home, pd.DataFrame):
    df_home.to_json("raw_iot.data.json", orient="records")
    print("Filer sparade: raw_iot.data.json")

if isinstance(df_home, pd.DataFrame):
    df_home.to_csv("raw_iot.data.csv", index=False)
    print("Filer sparade: raw_iot.data.csv")