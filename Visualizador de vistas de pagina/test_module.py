# -*- coding: utf-8 -*-
"""
@author: Eugenio Balbi
"""


import unittest
import time_series_visualizer
import matplotlib as mpl

class DataCleaningTestCase(unittest.TestCase):
    def test_data_cleaning(self):
        actual = int(time_series_visualizer.df.count(numeric_only=True))
        esperado = 1238
        self.assertEqual(actual, esperado, "Deberian ser 1238 datos en el DataFrame...")

class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_line_plot()
        self.ax = self.fig.axes[0]

    def test_line_plot_title(self):
        actual = self.ax.get_title()
        esperado = "Daily freeCodeCamp Forum Page Views 5/2016-12/2019"
        self.assertEqual(actual, esperado, "Se esperaba ke el titulo del grafico fuera: 'Daily freeCodeCamp Forum Page Views 5/2016-12/2019'")
    
    def test_line_plot_labels(self):
        actual = self.ax.get_xlabel()
        esperado = "Date"
        self.assertEqual(actual, esperado, "Se esperaba kue el xlabel fuera 'Date'")
        actual = self.ax.get_ylabel()
        esperado = "Page Views"
        self.assertEqual(actual, esperado, "Se esperaba kue el ylabel fuera 'Page Views'")

    def test_line_plot_data_quantity(self):
        actual = len(self.ax.lines[0].get_ydata())
        esperado = 1238
        self.assertEqual(actual, esperado, "Se esperaban 1238 datos en el DF.")


class BarPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_bar_plot()
        self.ax = self.fig.axes[0]

    def test_bar_plot_legend_labels(self):
        actual = []
        for label in self.ax.get_legend().get_texts():
          actual.append(label.get_text())
        esperado = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.assertEqual(actual, esperado, "Se esperaba que las etiquetas del diagrama de barras fueran meses del año.")
    
    def test_bar_plot_labels(self):
        actual = self.ax.get_xlabel()
        esperado = "Years"
        self.assertEqual(actual, esperado, "Se esperaba kue el xlabel fuera 'Years'")
        actual = self.ax.get_ylabel()
        esperado = "Average Page Views"
        self.assertEqual(actual, esperado, "Se esperaba kue el ylabel fuera 'Average Page Views'")
        actual = []
        for label in self.ax.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        esperado = ['2016', '2017', '2018', '2019']
        self.assertEqual(actual, esperado, "Se esperaba kue las etikuetas fueran '2016', '2017', '2018', '2019'")

    def test_bar_plot_number_of_bars(self):
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        esperado = 49
        self.assertEqual(actual, esperado, "Se esperaban 49 barras en el gráfico.")


class BoxPlotTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = time_series_visualizer.draw_box_plot()
        self.ax1 = self.fig.axes[0]
        self.ax2 = self.fig.axes[1]

    def test_box_plot_number(self):
        actual = len(self.fig.get_axes())
        esperado = 2
        self.assertEqual(actual, esperado, "Se esperaban dos diagramas de caja en la figura.")
    
    def test_box_plot_labels(self):
        actual = self.ax1.get_xlabel()
        esperado = "Year"
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, xlabel fuera 'Year'")
        actual = self.ax1.get_ylabel()
        esperado = "Page Views"
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, ylabel fuera 'Page Views'")
        actual = self.ax2.get_xlabel()
        esperado = "Month"
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, xlabel fuera 'Month'")
        actual = self.ax2.get_ylabel()
        esperado = "Page Views"
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, ylabel fuera 'Page Views'")
        actual = []
        for label in self.ax1.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        esperado = ['2016', '2017', '2018', '2019']
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, la etiketa secundaria fuera '2016', '2017', '2018', '2019'")
        actual = []
        for label in self.ax2.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        esperado = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 2, la etiketa secundaria fuera 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'")
        actual = []
        for label in self.ax1.get_yaxis().get_majorticklabels():
            actual.append(label.get_text())
        esperado = ['0', '20000', '40000', '60000', '80000', '100000', '120000', '140000', '160000', '180000', '200000']
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, la etiketa secundaria fuera '0', '20000', '40000', '60000', '80000', '100000', '120000', '140000', '160000', '180000', '200000'")

    def test_box_plot_titles(self):
        actual = self.ax1.get_title()
        esperado = "Year-wise Box Plot (Trend)"
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, el titulo fuera 'Year-wise Box Plot (Trend)'")
        actual = self.ax2.get_title()
        esperado = "Month-wise Box Plot (Seasonality)"
        self.assertEqual(actual, esperado, "Se esperaba que el diagrama de caja 1, el titulo fuera 'Month-wise Box Plot (Seasonality)'")

    def test_box_plot_number_of_boxes(self):
        actual = len(self.ax1.lines) / 6 # Every box has 6 lines
        esperado = 4
        self.assertEqual(actual, esperado, "Se esperaban 4 cajas en el Grafico de Cajas 1")
        actual = len(self.ax2.lines) / 6 # Every box has 6 lines
        esperado = 12
        self.assertEqual(actual, esperado, "Se esperaban 12 cajas en el Grafico de Cajas 2")

if __name__ == "__main__":
    unittest.main()
