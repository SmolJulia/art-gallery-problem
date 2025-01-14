# Zmienne dotycz鉍e wygl鉅u interfejsu, u篡wane w innych plikach 鏚這wych

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

# Wymiary element闚 okna
canvas_width, canvas_height = 700, 500  # Wymiary p堯tna
komunikat_width, komunikat_height = canvas_width, 40  # Wymiary komunikat闚 wyietlanych na g鏎ze okna
odstep_gora, odstep_lewa, odstep_dol, odstep_prawa = 10, 40, 80, 200  # Odst瘼y element闚 od kraw璠zi

# Wyliczenia wymiar闚 okna
window_width = canvas_width + odstep_lewa + odstep_prawa
window_height = canvas_height + komunikat_height + 2 * odstep_gora + odstep_dol

# Wsp馧rz璠ne element闚
canvas_rect = pygame.Rect(odstep_lewa, komunikat_height + 2 * odstep_gora, canvas_width, canvas_height)
komunikat_rect = pygame.Rect(odstep_lewa, odstep_gora, komunikat_width, komunikat_height)
wspolrzedne_rect = pygame.Rect(odstep_lewa, window_height - odstep_dol/2, canvas_width, odstep_dol/2)

point_radius = 5  # promie� ko豉 oznaczaj鉍ego wierzcho貫k wprowadzanego wielok靖a
