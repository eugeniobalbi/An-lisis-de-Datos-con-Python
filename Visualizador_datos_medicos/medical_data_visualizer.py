# -*- coding: utf-8 -*-
"""
@author: Eugenio Balbi
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Importo los datos del CSV
df = pd.read_csv('medical_examination.csv')


# Altura
altura = df['height'] / 100 

# Indice de masa corporal
IMC = df['weight'] / (altura**2)

# Agrego columna "Sobrepeso" = overweight al dataframe
df['overweight'] = np.where(IMC > 25, 1, 0)


# Normalizo los datos, haciendo que 0 sea BUENO y 1 MALO
# Si el valor del colesterol o glucusa es 1, corresponde valor 0 
# Si el valor es mayor que 1 corresponde un 1

df['cholesterol'] = np.where(df['cholesterol'] > 1, 1, 0)
df['gluc'] = np.where(df['gluc'] > 1, 1, 0)


# Grafico por categorias

def GraficoCategorias():
  
    # Creo un DataFrame para cada "categoria" y haciendo uso de Melt, voy saltando a cada
    # valor de colesterol, glucosa, fumar, alcohol, .... 
    df_cat = pd.melt(df,id_vars=['cardio'],value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active','overweight'])

    # Agrupo los datos en base al valor de CARDIO
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False).count()

    # Grafico  con sns.catplot()
    fig = sns.catplot(x='variable',y='total',hue='value',col='cardio',data=df_cat,kind='bar').fig

    # Guardo la imagen
    fig.savefig('catplot.png')
    return fig

  
# Mapa de Calor
def MapaCalor():
    # Limpieza de datos segun la consigna
    
    df_mapa_calor = df[
                (df['ap_lo'] <= df['ap_hi']) & 
                (df['height'] >= df['height'].quantile(0.025)) &
                (df['height'] <= df['height'].quantile(0.975)) &
                (df['weight'] >= df['weight'].quantile(0.025)) &
                (df['weight'] <= df['weight'].quantile(0.975))]

    # Matriz de correlacion
    corr = df_mapa_calor.corr(method='pearson')

    # Genero una mascara para tener el triángulo superior
    mascara = np.triu(corr)    

    fig, ax = plt.subplots(figsize=(12,10))  

    # Dibujo el mapa de calor con 'sns.heatmap()'
    sns.heatmap(corr, linewidths=1, annot=True, square=True, mask=mascara, fmt='.1f', center=0.08, cbar_kws = {'shrink':0.5})

    fig.savefig('heatmap.png')
    return fig