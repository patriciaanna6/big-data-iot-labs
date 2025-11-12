# Lab 1 

**Mål:** Hämta eller simulera IoT-data, spara som CSV/JSON, göra första utforskning och förbereda fil för rensning (Lab 2).

## Kör i Colab
```bash
!git clone https://github.com/<ditt-org>/<repo>.git
%cd <repo>/lab1-collection

## Lab1-Datainsamling med Pandas

**Mål:**

- Förstå hur IoT-data kan hämtas (API/syntetisk) och lagras i ett strukturerat format (CSV/JSON).
- Lära grunderna i att läsa/skriva data med **Pandas**.
- Skapa en liten *datainsamlings-pipeline*: hämta → kontrollera → spara → dokumentera.

## Panda - Panel data

Panda är ett öppen källkods-bibliotek i Pyhton som används för datahantering och analys.

Pandas är ett kraftfullt verktyg i Python för att hantera, analysera och bearbeta data i tabellform. Det gör det enkelt att arbeta med stora datamängder, datum, och saknade värden, samt samarbetar väl med andra Pythonbibliotek för dataanalys.

Det bygger på **två huvudstrukturer**:

- **Series** – en endimensionell datastruktur (liknar en lista eller kolumn)
- **DataFrame** – en tvådimensionell datastruktur (liknar en tabell med rader och kolumner)

Vi kommer att jobba med DataFrames

## DataFrame

Inom dataanalys en dataframe är kärnobjektet för att arbeta med data och erbjuder kraffulla funktioner. 

En dataframe är som en excelblad dvs en tabell med rader och kolumner, en 2 dimensionellt 

Om man till exempel har a dataset som  nedan som visar temperatur för 3 olika städer under en dag :

data = { ‘city’:[”Stockholm”,Göteborg”,”Malmö”],’temp’:[10,17,20], ‘date’:[2025-11-10]}

### Man kan visa datat ovan i en dataframe:

|  | **city** | **temp** | **date** |
| --- | --- | --- | --- |
| 0 | Stockholm | 10 | 2024-06-01 |
| 1 | Göteborg | 17 | 2024-06-01 |
| 2 | Malmö | 20 | 2024-06-01 |

Men tänk att man har en stor mängd dataset , Big data exempel från ett företag med kundtransaktioner som innehåller 10 miljoner köp: Då behövs pandas dataframe, för att kunna komma åt datan i en stor dataset lättare och snabbare.

## **Grundläggande dataexploration ( head(), info(), describe() )**

Efter man har läst in datan vill man veta vad man har fått: 

df.head()          # Första raderna
[df.info](http://df.info/)()          # Datatyper, minne, null-värden
df.describe()      # Statistisk sammanfattning
df.shape           # Antal rader och kolumner
df.columns         # Kolumnnamn

## Datakvalitet

df.isnull().sum()           # Hitta saknade värden
df.duplicated().sum()       # Räkna dubbletter
df.dtypes                   # Kontrollera datatyper
df['kolumn'].unique()       # Visa unika värden i kolumn
df['kolumn'].value_counts() # Visa frekvens av värden

## Filtera data och välja kolumner ( loc, iloc, villkor)

df[df['Season'] == 'Winter']
df[df['Energy Consumption (kWh)'] > 2.0]
df[(df['Season'] == 'Winter') & (df['Household Size'] > 3)]

## Välja specifika kolumner

df[['Appliance Type', 'Energy Consumption (kWh)']]

Att filtrera data är avgörande för att extrahera relevanta delmängder baserat på villkor.

## GRUPPERING & AGGREGERING:

> Gruppera efter säsong för smart home data
> 

df.groupby('Season')['Energy Consumption (kWh)'].mean()
df.groupby('Appliance Type').agg({
'Energy Consumption (kWh)': ['mean', 'max', 'count']
})

> Gruppera student data
> 

df_student.groupby('Gender')['Exam_Score'].mean()

## ****SORTING & RANKING:

df.sort_values('Energy Consumption (kWh)', ascending=False)
df.nlargest(10, 'Energy Consumption (kWh)')
df.nsmallest(5, 'Outdoor Temperature (°C)')
