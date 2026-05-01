# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 13:03:39 2026

@author: Maxim Picandet
"""

"""
Optischer Weg:
    L = integral_E^S n(s) ds

Brechungsindex n(s):
    n = 1 + [(77.6e-8 p)/(T) + (64.8e-8 + (3.776e-3)/(T))e/T]
"""

"""
Aufgabe a:
    Zusätzlichen optischen Weg (Zenith Delay) für die Modellatmosphären "Tropisch",
    "Subarktisch-Winter" berechnen.
"""

import numpy as np

def optischerWeg(file):
    """
    Parameters
    ----------
    file : str
        PATH to data file, relative or absolute. Must be a csv-file with four
        columns: [0] height, [1] pressure, [2] temperature, [3] vapor pressure.
        Delimiter must be a comma ",". First row will be skipped.

    Returns
    -------
    zenithDelay : float64
    opticPath : float64

    """
    
    data = np.loadtxt(file, delimiter=",", skiprows=1)
    
    n = 1 + (
        77.6e-8 * data[:,1] / data[:,2] +
        (64.8e-8 + (3.776e-3) / data[:,2]) * data[:,3] / data[:,2]
        )
    
    ds = np.empty(data[:,0].size);
    print(data[:,0].size)
    
    ds[1:-1] = (data[2:,0] - data[:-2,0]) / 2
    ds[0] = data[1,0] - data[0,0]
    ds[-1] = data[-1,0] - data[-2,0]
    
    L = n * ds
    L = L.sum()
    
    zenithDelay = L - data[-1,0]
    return zenithDelay, L
    

fileTropisch = "../Übungen/uebung_03_Daten_tropisch.dat"
fileSubarktisch = "../Übungen/uebung_03_Daten_subarktischer-winter.dat"

ZDtropisch, OWtropisch = optischerWeg(fileTropisch)
ZDsubarktisch, OWsubarktisch = optischerWeg(fileSubarktisch)
