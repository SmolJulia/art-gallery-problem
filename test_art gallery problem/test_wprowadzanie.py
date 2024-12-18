import os
from agp_project.pliki_zrodlowe.triangulacja import oblicz_liczbe_straznikow
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *
from agp_project.main import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))


l = oblicz_liczbe_straznikow()
file_name = os.path.basename(filepath)

class TestWprowadzanie:  
  def Test_plik_kwadrat(self):
        fake_file_path = os.path.abspath('agp_project/pliki_wielokat/kwadrat.csv')
        mock_askopenfilename.return_value = fake_file_path

        # Simulate the file selection
        file_path = plik_z_okna_dialogowego()
        
        # Extract the file name and check if it's 'kwadrat.csv'
        file_name = os.path.basename(file_path)

        if file_name == "kwadrat.csv":
            # Run the function with the mocked file path (which doesn't exist on disk)
            l = oblicz_liczbe_straznikow(file_path)
            
            # Check that the result is what we expect for 'kwadrat.csv'
            assert l == 1
