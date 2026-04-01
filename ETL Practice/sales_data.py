import pandas as pd
import numpy as np

'''
🧹 Cleaning Challenges
Challenge A — Find & Remove Duplicates
Some rows appear more than once. Find and remove them, keeping only the first occurrence.

✅ Expected: Drop from 215 rows down to 200

Challenge B — Fix Inconsistent Formatting
The Region and Country columns have variants like "north america", "N. America", "EUROPE", "U.S.A". Standardize them all to a consistent format.

✅ Expected: Each region/country should have only one unique value after cleaning

Challenge C — Fix Wrong Data Types
Some values in Revenue and Units_Sold are stored as strings instead of numbers. Find them and convert them to the correct type.

✅ Expected: df.dtypes should show Revenue as float and Units_Sold as int/float after fixing

Challenge D — Handle Missing Values
Some rows have blanks in Salesperson, Customer_Segment, Payment_Method, and Country. Find how many are missing per column, then decide how to handle them — drop or fill.

✅ Expected: df.isnull().sum() shows 0 for all columns after cleaning

Final Boss — Export Clean Data
After all 4 fixes, export the cleaned result to sales_cleaned.xlsx. That file should be Tableau-ready!
Take your time — and as always, share your code when you're ready! 🐍
'''

# df = pd.ExcelFile("sales_dirty_data.xlsx") #Checking to see how many tabs we have in the excel.
# print(df.sheet_names)

df = pd.read_excel("sales_dirty_data.xlsx", sheet_name="Sales_Dirty")
df_cleaned = df.drop_duplicates() #dropped duplicates here.
# print(df_cleaned)

for col in ['Region', 'Country']:
    df_cleaned[col] = df_cleaned[col].replace(r'[^a-zA-Z0-9\s]', '', regex=True) #Remove Unwanted Characters: Eliminate special symbols from text columns.
    df_cleaned[col] = df_cleaned[col].str.lower().str.strip().str.replace(' ', '') #My goal is to uniform them as must as I can so that when I do the dictionary mapping method, I don't have to write too much.

df_cleaned['Region'] = np.where(df_cleaned['Region'].str.contains('eur', case=False, na=False), 'Europe',
                       np.where(df_cleaned['Region'].str.contains('america', case=False, na=False), 'North America',
                       np.where(df_cleaned['Region'].str.contains('asia', case=False, na=False), 'Asia Pacific', df_cleaned['Region'])))

#I had to go with dictionary since there were so many variations.
country_mapping = {
    'japan':'Japan',
    'aus':'Australia',
    'france':'France',
    'us':'United States',
    'canada':'Canada',
    'usa':'United States',
    'singapore':'Singapore',
    'germany':'Germany',
    'uk':'United Kingdom',
    'unitedstates':'United States',
    'unitedkingdom':'United Kingdom',
    'ger':'Germany',
    'sgp':'Singapore',
    'can':'Canada'
}
df_cleaned['Country'] = df_cleaned['Country'].map(country_mapping)

listofregion = df_cleaned['Region'].unique() #Looking to see only the unique values in the column so I know what to fix.
listofcountry = df_cleaned['Country'].unique()

df_cleaned = df_cleaned.fillna('Not Available') #fill empty cells with Not Available.

# print(df_cleaned.isnull().sum())

# print(df_cleaned['Country'].unique())

df_cleaned.to_excel('sales_cleaned.xlsx', index=False)