import os
from agp_project import * #agp_project.main #agp_project.pliki_zrodlowe.wprowadzanie_pliku

def test_kwadrat():
  l = liczba_straznikow
  file_name = os.path.basename(file_path)
  
  if file_name == "kwadrat.csv":
    assert l == 1

