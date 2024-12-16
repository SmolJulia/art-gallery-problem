import os
from agp_project.main import * #agp_project.main #agp_project.pliki_zrodlowe.wprowadzanie_pliku
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *

l = liczba_straznikow
file_name = os.path.basename(file_path)

def test_kwadrat():  
  if file_name == "kwadrat.csv":
    assert l == 1

