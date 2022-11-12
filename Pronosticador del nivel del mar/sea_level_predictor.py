# -*- coding: utf-8 -*-
"""
@author: Eugenio Balbi
"""
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Utiliza Pandas para importar los datos de epa-sea-level.csv a un dataframe
    df = pd.read_csv('epa-sea-level.csv')


    # Utilice matplotlib para crear un gráfico de dispersión utilizando la 
    # columna Year como eje x y la columna CSIRO Adjusted Sea Level como eje y. 
    # fig = plt.figure()
    plt.scatter(df['Year'],df['CSIRO Adjusted Sea Level'],s=8)


    # Usa la función linregress de scipy.stats para obtener la pendiente e 
    # intersección con el eje y de la línea de mejor encaje. 
    # Dibuja la línea de mejor encaje sobre el diagrama de dispersión. 
    # Haz que la línea pase por el año 2050 para predecir el aumento del nivel 
    # del mar en ese año. 
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x1 = np.arange(df['Year'].min(),2051,1)
    y1 = res1.intercept + res1.slope*x1
    plt.plot(x1,y1,color='firebrick')


    # Traza una nueva línea de mejor encaje utilizando datos del año 2000 
    # hasta el año más reciente del conjunto de datos. Haz que la línea pase 
    # también por el año 2050 para predecir la subida del nivel del mar en 2050 
    # si el ritmo de subida continúa como desde el año 2000. 
    df2 = df[df['Year']>=2000]
    res2 = linregress(df2['Year'], df2['CSIRO Adjusted Sea Level'])
    x2 = np.arange(df2['Year'].min(),2051,1)
    y2 = res2.intercept + res2.slope*x2
    plt.plot(x2,y2,color='mediumseagreen')


    # La etiqueta x debe ser Year, la etiqueta y debe ser Sea Level (pulgadas) 
    # y el título debe ser Rise in Sea Level. 
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Guardo la imagen generada
    plt.savefig('sea_level_plot.png')
    return plt.gca()




