import os
from agp_project.pliki_zrodlowe.triangulacja import oblicz_liczbe_straznikow #agp_project.main #agp_project.pliki_zrodlowe.wprowadzanie_pliku
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *
import csv
from matplotlib.markers import MarkerStyle
from pygame import color
import tripy
import matplotlib.pyplot as plt
from collections import defaultdict
import matplotlib.patches as patches
import matplotlib
matplotlib.use('Agg')
import numpy as np
from pliki_zrodlowe.konfiguracja_okna import canvas_width, canvas_height

l = oblicz_liczbe_straznikow()
file_name = os.path.basename(file_path)

class TestKwadrat:  
  if file_name == "kwadrat.csv":
    assert l == 1

