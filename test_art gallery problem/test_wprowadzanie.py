import os
from agp_project.pliki_zrodlowe.triangulacja import oblicz_liczbe_straznikow
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import plik_z_okna_dialogowego
from agp_project.main import *


l = oblicz_liczbe_straznikow()
file_name = os.path.basename(plik_z_okna_dialogowego())

class TestWprowadzanie:  
  def Test_plik_kwadrat(self):
    if file_name == "kwadrat.csv":
      assert l == 1
