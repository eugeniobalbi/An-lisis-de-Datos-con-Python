# -*- coding: utf-8 -*-
"""
@author: Eugenio Balbi
"""

import unittest
import medical_data_visualizer
import matplotlib as mpl


# the test case
class GraficoCategoriasTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.GraficoCategorias()
        self.ax = self.fig.axes[0]
    
    def test_plot_labels(self):
        actual = self.ax.get_xlabel()
        esperado = "variable"
        self.assertEqual(actual, esperado, "El xlabel deberia ser 'variable'")
        actual = self.ax.get_ylabel()
        esperado = "total"
        self.assertEqual(actual, esperado, "El ylabel deberia ser 'total'")
        actual = []
        for label in self.ax.get_xaxis().get_majorticklabels():
            actual.append(label.get_text())
        esperado = ['active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke']
        self.assertEqual(actual, esperado, "Las etiketas del barplot en el eje x deberian ser 'active', 'alco', 'cholesterol', 'gluc', 'overweight', 'smoke'")

    def test_barplot_cantidad_barras(self):
        actual = len([rect for rect in self.ax.get_children() if isinstance(rect, mpl.patches.Rectangle)])
        esperado = 13
        self.assertEqual(actual, esperado, "Se esperaba una cantidad diferente de graficos de barra")


class MapaCalorTestCase(unittest.TestCase):
    def setUp(self):
        self.fig = medical_data_visualizer.MapaCalor()
        self.ax = self.fig.axes[0]
        # self.maxDiff = None

    def test_mapa_calor_labels(self):
        actual = []
        for label in self.ax.get_xticklabels():
          actual.append(label.get_text())
        esperado = ['id', 'age', 'sex', 'height', 'weight', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'smoke', 'alco', 'active', 'cardio', 'overweight']
        self.assertEqual(actual, esperado)
    
    def test_mapa_calor_valores(self):
        actual = [text.get_text() for text in self.ax.get_default_bbox_extra_artists() if isinstance(text, mpl.text.Text)]
        # print(actual)
        esperado = ['0.0', '0.0', '-0.0', '0.0', '-0.1', '0.5', '0.0', '0.1', '0.1', '0.3', '0.0', '0.0', '0.0', '0.0', '0.0', '0.0', '0.2', '0.1', '0.0', '0.2', '0.1', '0.0', '0.1', '-0.0', '-0.1', '0.1', '0.0', '0.2', '0.0', '0.1', '-0.0', '-0.0', '0.1', '0.0', '0.1', '0.4', '-0.0', '-0.0', '0.3', '0.2', '0.1', '-0.0', '0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.2', '0.1', '0.1', '0.0', '0.0', '0.0', '0.0', '0.3', '0.0', '-0.0', '0.0', '-0.0', '-0.0', '-0.0', '0.0', '0.0', '-0.0', '0.0', '0.0', '0.0', '0.2', '0.0', '-0.0', '0.2', '0.1', '0.3', '0.2', '0.1', '-0.0', '-0.0', '-0.0', '-0.0', '0.1', '-0.1', '-0.1', '0.7', '0.0', '0.2', '0.1', '0.1', '-0.0', '0.0', '-0.0', '0.1']
        self.assertEqual(actual, esperado, "No son los valores esperados para el mapa de calor")

if __name__ == "__main__":
    unittest.main()