import os
from agp_project.pliki_zrodlowe.triangulacja import oblicz_liczbe_straznikow
from agp_project.pliki_zrodlowe.wprowadzanie_pliku import *
from agp_project.main import *

os.chdir(os.path.dirname(os.path.abspath(__file__)))


l = oblicz_liczbe_straznikow()
file_name = os.path.basename(filepath)

class TestWprowadzanie:  
  def Test_plik_kwadrat(self):
        # Simulate file selection via filedialog
        file_path = plik_z_okna_dialogowego()  # This will prompt the user to select a file
        
        # Convert the file path to an absolute path
        file_path = os.path.abspath(file_path)
        
        # Extract the file name from the absolute file path
        file_name = os.path.basename(file_path)
        
        # Check if the file name is 'kwadrat.csv'
        if file_name == "kwadrat.csv":
            # Call the function with the selected file path
            l = oblicz_liczbe_straznikow(file_path)
            
            # Assert the expected value
            assert l == 1
