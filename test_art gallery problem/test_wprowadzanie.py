import os
from agp_project.pliki_zrodlowe.triangulacja import oblicz_liczbe_straznikow #agp_project.main #agp_project.pliki_zrodlowe.wprowadzanie_pliku
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *

l = oblicz_liczbe_straznikow()
file_name = os.path.basename(file_path)

class TestKwadrat:  
  def Test_plik_kwadrat(self):
    if file_name == "kwadrat.csv":
      assert l == 1

