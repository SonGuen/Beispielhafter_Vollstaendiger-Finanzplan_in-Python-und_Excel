'''
Diese Datei sind alle Module, welche für diese Arbeit verwendet worden ist
auf die einzelnen Bibliotheken werden aufgrund der Relevanz nicht eingegangen
da viele typisch verwendete Bibliotheke sind
-###- bezeichnen die einzelnen Kommentare
'''


###für das schnelle rechnen
import numpy as np

###für den aufgriff der Pfade auf dem Rechner
import os

###Für das plotten der Grafiken
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable

###
import scipy.ndimage as ndimage
###Laden und Speichern von Listen bzw. DataFrames und das schnelle bearbeiten von df (DataFrames)
import pandas as pd
### re ist für die Änderung bzw. suche von einzelnen Strings bzw. Satzseichen eines Textes bzw. Arrays
import re

### Zeitladen
import time
###Für die Schleifen zur Messung der Zeit
from tqdm import tqdm
###tieferes eingehen vom computer
import sys
###Abspeichern relativ großer Datensätze in binary
import pickle
###für das Rechnen der Daten (Februar ...)
import datetime

###Gleiches wie oben
import calendar

###gleiches wie Matplotlib nur schöner
import seaborn as sns

###spezifischer Aufruf eines Modules von dateimte
from datetime import datetime, timedelta as delta

###Aufruf von PVLIB pvsystem für die berechnung von solarzellen und die temperaturverhalten
#from pvlib import pvsystem

### für effziente schleifen
import itertools
### standardnormalverteiltungsfunktion zeitkontinuierlich
from scipy.stats import norm
###zufallswahl aus der standardnormalverteilung für den wiener prozess
from numpy.random import randn
###laden lades moduls random (Zufall) als rn
from numpy import random as rn
###Laden der statistischen Funktion
import scipy.stats as si

###Laden der Zeitachse für die illustration des Plots
import matplotlib.dates as mdates


###für die Illustration und der parametrisierung der grafischen Illustration
from matplotlib.font_manager import FontProperties
import locale

locale.setlocale(locale.LC_ALL,"")
import pybamm
from sklearn.linear_model import LinearRegression



from datetime import datetime, timedelta as delta
import pandas as pd
import numpy as np
from tqdm import tqdm

import itertools
import math

from scipy import stats
from scipy.stats import sem


### Damit die Texte aus den Grafiken in Times New Roman mit einer Schriftgröße 12 dargelegt werden
plt.rcParams['text.usetex'] = False
font = FontProperties()
font.set_name('Times New Roman')
font.set_style('normal')
font.set_size(12)
