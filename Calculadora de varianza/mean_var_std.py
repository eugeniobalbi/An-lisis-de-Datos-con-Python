# -*- coding: utf-8 -*-
"""
@author: eugen
"""

import numpy as np

def calculate(list):
# Generar una excepción si el tamaño de la lista no es 9
  if len(list) != 9:
    raise ValueError("La lista debe contener nueve números!")
  
  # Crear matriz de 3x3
  matrix = np.array(list).reshape((3,3))

  # crear diccionario
  calculations = {}

  # Calculo la Media
  calculations['Media'] = [matrix.mean(axis=0).tolist(), 
                        matrix.mean(axis=1).tolist(),
                        matrix.mean()]
  
  # Calculo la Varianza
  calculations['Varianza'] = [matrix.var(axis=0).tolist(), 
                          matrix.var(axis=1).tolist(),
                          matrix.var()]

  # Calculo el Desvio Estandar 
  calculations['Desvio Estandar'] = [matrix.std(axis=0).tolist(), 
                        matrix.std(axis=1).tolist(),
                        matrix.std()]

  # Calculo el Maximo
  calculations['Maximo'] = [matrix.max(axis=0).tolist(), 
                        matrix.max(axis=1).tolist(),
                        matrix.max()]

  # Calculo el Minimo
  calculations['Minimo'] = [matrix.min(axis=0).tolist(), 
                        matrix.min(axis=1).tolist(),
                        matrix.min()]

  # Sumo...
  calculations['Suma Total'] = [matrix.sum(axis=0).tolist(), 
                        matrix.sum(axis=1).tolist(),
                        matrix.sum()]

  return (calculations)