import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_spotify = pd.read_csv('spotify-2023.csv',encoding = 'latin-1')

print(df_spotify.head())

tipos_de_variables = df_spotify.dtypes

conteo_tipos_de_variables = tipos_de_variables.value_counts() # Punto A - Conteo de variables categóricas y numéricas 

canciones_taylor = df_spotify[df_spotify['artist(s)_name'] == 'Taylor Swift'] # Punto B - Canciones de Taylor Swift

def canciones_del_año(df,año) :                             # Punto D - Función que devuelve las canciones del año 
    canciones_año = df[df['released_year'] == año]
    return canciones_año

# Ejemplo practico de la funcion

print(canciones_del_año(df_spotify,2019))

columna_medias = df_spotify.mean(numeric_only = True)   # Punto C - Columna de medias para variables numéricas

box = {}
for i in df_spotify['streams'].unique() :
    box[i] = df_spotify[df_spotify['streams'] == i].artist_count

conteo_canciones = df_spotify['released_year'].value_counts()
año_lanzamiento = conteo_canciones.index.unique()

plt.style.use('ggplot')

fig, [ax1,ax2] = plt.subplots(2,1, figsize = (20,20))   # Punto F - Gráficas Subplot ()

ax1.hist(conteo_canciones.index, bins = 20)
ax1.set_title('Canciones lanzadas por año')
ax1.set_xlabel('Año de lanzamiento')
ax1.set_ylabel('Cantidad de canciones lanzadas')
ax1.set_xticks(año_lanzamiento)

ax2.boxplot([x for x in box.values()],labels = [x for x in box.keys()])
ax2.set_title('Conteo de artistas por streams')
ax2.set_xlabel('Cantidad de Streams')
ax2.set_ylabel('Artistas por cantidad de streams')

plt.show()