import os
from agp_project.pliki_zrodlowe.triangulacja import oblicz_liczbe_straznikow #agp_project.main #agp_project.pliki_zrodlowe.wprowadzanie_pliku
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *

l = oblicz_liczbe_straznikow()
file_name = os.path.basename(file_path)

def test_kwadrat():  
  if file_name == "kwadrat.csv":
    assert l == 1

