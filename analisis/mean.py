from numpy import int64
import pandas as pd

df = pd.read_csv('objek.csv')
print(df.to_string())

df['Umur'] = df['Umur'].fillna(round (df['Umur'].mean(), 1))   
df['Umur'] = df['Umur'].astype(int64)
# print(df.to_string())

df['Tinggi_Badan'] = df['Tinggi_Badan'].fillna(round (df['Tinggi_Badan'].median(), 1)).astype(int64)

df['Berat_Badan'] = df['Berat_Badan'].fillna(round (df['Berat_Badan'].mode()[0], 1))
print(df.to_string())
