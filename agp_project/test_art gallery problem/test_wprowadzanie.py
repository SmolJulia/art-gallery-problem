import os
from agp_project.pliki_zrodlowe.triangulacja import oblicz_liczbe_straznikow
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *
from agp_project.main import *
os.chdir('agp_project/pliki_wielokat')

l = oblicz_liczbe_straznikow()
file_name = os.path.basename(file_path)

class TestWprowadzanie:  
  def Test_plik_kwadrat(self):
    if file_name == "kwadrat.csv":
      assert l == 1
