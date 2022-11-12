# -*- coding: utf-8 -*-
"""
@author: Eugenio Balbi
"""


import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np
register_matplotlib_converters()

# Utiliza Pandas para importar los datos de "fcc-forum-pageviews.csv". 
# Establece el índice de la columna date.

# Importo los datos de la fecha desde el CSV a un DataFrame
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=True)


# Limpiar los datos filtrando los días en que las vistas de la página se encuentran 
# en el 2,5% superior del conjunto de datos o en el 2,5% inferior del conjunto de datos.

df = df[(df['value']>df['value'].quantile(0.025)) &
       ((df['value']<df['value'].quantile(0.975)))]


# Crea una función llamada draw_line_plot que utilice Matplotlib para dibujar 
# un gráfico de línea similar a "examples/Figure_1.png". 
# El título debe ser Daily freeCodeCamp Forum Page Views 5/2016-12/2019. 
# La etiqueta en el eje x debe ser Date y la etiqueta en el eje y debe ser Page Views.

def draw_line_plot():
    
    fig = plt.figure(figsize=(18,6))
    plt.plot(df,color='firebrick')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Guardo la imagen generada
    fig.savefig('line_plot.png')
    return fig
    # fig.show()


# Crea una función llamada draw_bar_plot que dibuje un gráfico de barras similar 
# a "examples/Figure_2.png". Debe mostrar el número promedio de vistas diarias 
# de cada mes, agrupadas por año. La leyenda debe mostrar las etiquetas de los meses 
# y tener un título de Months. En el gráfico, la etiqueta en el eje x debe ser Years 
# y la etiqueta en el eje y debe ser Average Page Views.

def draw_bar_plot():
    
    df_bar = df.copy(deep=True)
    df_bar['year'] = df_bar.index.year
    months = ["January", "February", "March", "April", "May", "June", "July", "August",
              "September", "October", "November", "December"]
    df_bar['month'] = df_bar.index.month_name()
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months)
    df_bar_pivot = pd.pivot_table(
        df_bar,
        values="value",
        index="year",
        columns="month",
        aggfunc=np.mean
    )

    # Dibujo los graficos de barras
    fig = df_bar_pivot.plot(kind='bar').get_figure()
    fig.set_figheight(6)
    fig.set_figwidth(8)
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    # Guardo la imagen generada
    fig.savefig('bar_plot.png')
    return fig


# Crea una función llamada draw_box_plot que utilice Seaborn para dibujar 
# dos diagramas de caja adyacentes similares a "examples/Figure_3.png". 
# Estos diagramas de caja deben mostrar cómo se distribuyen los valores dentro 
# de un año o mes determinado y cómo se compara con el tiempo. 
# El título del primer gráfico debe ser Year-wise Box Plot (Trend) y el 
# título del segundo gráfico debe ser Month-wise Box Plot (Seasonality). 
# Asegúrese de que las etiquetas de los meses en la parte inferior comiencen 
# en Jan y que los ejes x e y estén etiquetados correctamente. 


def draw_box_plot():
    
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug",
              "Sep", "Oct", "Nov", "Dec"]
    df_box['month'] = pd.Categorical(df_box['month'], categories=months)

    
    fig, ax = plt.subplots(1,2,figsize=(18,6))
    plt.subplot(1, 2, 1)
    sns.boxplot(x=df_box['year'], y=df_box['value']).get_figure()
    plt.title('Year-wise Box Plot (Trend)')
    plt.xlabel('Year')
    plt.ylabel('Page Views')
    plt.subplot(1, 2, 2)
    sns.boxplot(x=df_box['month'], y=df_box['value']).get_figure()
    plt.title('Month-wise Box Plot (Seasonality)')
    plt.xlabel('Month')
    plt.ylabel('Page Views')

    # Guardo la imagen generada
    fig.savefig('box_plot.png')
    return fig