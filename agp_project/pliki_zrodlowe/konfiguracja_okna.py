# Zmienne dotycz�ce wygl�du interfejsu, u�ywane w innych plikach �r�d�owych

import pygame

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
LIGHT_GREY = (230, 230, 230)
DARK_GREY = (100, 100, 100)
RED = (255, 0, 0)
DARK_RED = (180, 0, 0)
YELLOW = (255, 255, 100)
GREEN = (100, 255, 100)
DARK_BLUE = (0, 0, 180)

# Wymiary element�w okna
canvas_width, canvas_height = 700, 500  # Wymiary p��tna
komunikat_width, komunikat_height = canvas_width, 40  # Wymiary komunikat�w wy�wietlanych na g�rze okna
odstep_gora, odstep_lewa, odstep_dol, odstep_prawa = 10, 40, 80, 200  # Odst�py element�w od kraw�dzi

# Wyliczenia wymiar�w okna
window_width = canvas_width + odstep_lewa + odstep_prawa
window_height = canvas_height + komunikat_height + 2 * odstep_gora + odstep_dol

# Wsp�rz�dne element�w
canvas_rect = pygame.Rect(odstep_lewa, komunikat_height + 2 * odstep_gora, canvas_width, canvas_height)
komunikat_rect = pygame.Rect(odstep_lewa, odstep_gora, komunikat_width, komunikat_height)
wspolrzedne_rect = pygame.Rect(odstep_lewa, window_height - odstep_dol/2, canvas_width, odstep_dol/2)

point_radius = 5  # promie� ko�a oznaczaj�cego wierzcho�ek wprowadzanego wielok�ta
