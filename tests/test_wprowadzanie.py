import os
from agp_project.main import liczba_straznikow #agp_project.main
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import file_path #agp_project.pliki_zrodlowe.wprowadzanie_pliku
def test_kwadrat(self):
  l = liczba_straznikow
  file_name = os.path.basename(file_path)
  
  if file_name == "kwadrat.csv":
    assert l == 1

