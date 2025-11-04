import pandas as pd
import plotly.express as px

df = pd.read_csv('health_data.csv')
print(df.to_string())

labels = df['Diagnosis'].replace({0:'Sehat', 
                                  1:'Hipertensi ringan', 
                                  2:'Hipertensi', 
                                  3:'Prediabetes', 
                                  4:'Kolestrol tinggi',
                                  5:'Diabetes tipe 2'
                                  
                            }).value_counts(sort=True).index
print(labels)



sizes = df['Diagnosis'].value_counts(sort=True)



fig = px.pie(names = labels, values = sizes, hole=0.3,
             color_discrete_sequence = ['lightblue', 'lightgreen', 'orange', 'red', 'purple', 'darkred'],
             labels = {'names': 'Diagnosis kesehatan'},
             title = 'Distribusi Diagnosis Kesehatan'
             )

fig.update_traces(textposition='inside',
                  textinfo='percent+label+value')

fig.show()