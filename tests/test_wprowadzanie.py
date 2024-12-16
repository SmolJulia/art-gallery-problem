import os
from agp_project.main import * #agp_project.main #agp_project.pliki_zrodlowe.wprowadzanie_pliku
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *

file_name = os.path.basename(file_path)
l = liczba_straznikow

def test_kwadrat():  
  if file_name == "kwadrat.csv":
    assert l == 1

