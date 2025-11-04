import pandas as pd

df = pd.read_csv('objek.csv')

df['Umur'] = df['Umur'].fillna(round(df['Umur'].mean(), 0))
df['Tinggi_Badan'] = df['Tinggi_Badan'].fillna(round(df['Tinggi_Badan'].mean(), 1)).astype('int64')
df['Berat_Badan'] = df['Berat_Badan'].fillna(round(df['Berat_Badan'].mean(), 1)).astype(int)



df['Umur'] = pd.cut(df['Umur'], bins=[0,12,17,25,30],
                                labels=['Anak-anak','Remaja','Dewasa','Muda'])

df['Tinggi_Badan'] = pd.cut(df['Tinggi_Badan'], bins = [0,130,155,170,200],
                                                labels = ['Kurcaci','Pendek','Sedang','Tinggi'])

df['Berat_Badan'] = pd.cut(df['Berat_Badan'], bins = [0,20,65,150],
                                                labels = ['Enteng', 'Normal', 'Gemuk'])



print(df.to_string())