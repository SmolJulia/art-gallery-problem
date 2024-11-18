# Plik zawierający funkcje potrzebne do stworzenia okna w Pygame i narysowania jego elementów, wywołane w main().
# Zawiera też zmienne konfigurujące wielkość i położenie poszczególnych elementów interfejsu oraz krotki definiujące podstawowe kolory.

import pygame
from funkcje_pomocnicze import wspol_osiowe, wyswietl_tekst
from typing import List, Union

# ---------------------------- KONFIGURACJA ----------------------------

# Kolory
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
LIGHT_GREY = (230, 230, 230)
DARK_GREY = (100, 100, 100)
RED = (255, 0, 0)
YELLOW = (255, 255, 100)

# Wymiary elementów okna
canvas_width, canvas_height = 700, 500  # Wymiary płótna
komunikat_width, komunikat_height = canvas_width, 40  # Wymiary komunikatów wyświetlanych na górze okna
odstep_gora, odstep_lewa, odstep_dol, odstep_prawa = 10, 40, 80, 200  # Odstępy elementów od krawędzi

# Wyliczenia wymiarów okna
window_width = canvas_width + odstep_lewa + odstep_prawa
window_height = canvas_height + komunikat_height + 2 * odstep_gora + odstep_dol

# Współrzędne elementów
canvas_rect = pygame.Rect(odstep_lewa, komunikat_height + 2 * odstep_gora, canvas_width, canvas_height)
komunikat_rect = pygame.Rect(odstep_lewa, odstep_gora, komunikat_width, komunikat_height)
wspolrzedne_rect = pygame.Rect(odstep_lewa, window_height - odstep_dol/2, canvas_width, odstep_dol/2)


# ---------------------------- FUNKCJE ----------------------------

def init_window():
    """Inicjalizuje pygame i tworzy okno."""
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    screen.fill(GREY)
    return screen


def draw_canvas_area(screen):
    """Rysuje główne płótno na obszarze canvas_rect."""
    pygame.draw.rect(screen, WHITE, canvas_rect)
    return canvas_rect


def draw_komunikat_area(screen):
    """Rysuje obszar na komunikaty na górze okna."""
    pygame.draw.rect(screen, WHITE, komunikat_rect)
    return komunikat_rect


def draw_grid(screen):
    """Rysuje siatkę na płótnie."""
    for x in range(0, canvas_width + 1, 20):  # Linie pionowe siatki
        x_pos = canvas_rect.left + x
        pygame.draw.line(screen, GREY, (x_pos, canvas_rect.bottom), (x_pos, canvas_rect.top), 1, )
    for y in range(0, canvas_height + 1, 20):  # Linie poziome siatki
        y_pos = canvas_rect.bottom - y
        pygame.draw.line(screen, GREY, (canvas_rect.left, y_pos), (canvas_rect.right, y_pos), 1)


def draw_axes(screen):
    """Rysuje osie X i Y oraz etykiety co 100 jednostek."""
    # Rysowanie linii osi
    pygame.draw.line(screen, BLACK, canvas_rect.topleft, canvas_rect.bottomleft, 2)  # Oś Y
    pygame.draw.line(screen, BLACK, canvas_rect.bottomleft, canvas_rect.bottomright, 2)  # Oś X

    font = pygame.font.SysFont(None, 24)

    # Rysowanie etykiet na osi X co 100 jednostek
    for x in range(0, canvas_width + 1, 100):
        x_pos = canvas_rect.left + x
        pygame.draw.line(screen, BLACK, (x_pos, canvas_rect.bottom), (x_pos, canvas_rect.top), 1)
        label = font.render(str(x), True, BLACK)
        screen.blit(label, (x_pos - 10, canvas_rect.bottom + 10))

    # Rysowanie etykiet na osi Y co 100 jednostek
    for y in range(100, canvas_height + 1, 100):
        y_pos = canvas_rect.bottom - y
        pygame.draw.line(screen, BLACK, (canvas_rect.left, y_pos), (canvas_rect.right, y_pos), 1)
        label = font.render(str(y), True, BLACK)
        screen.blit(label, (canvas_rect.left - 35, y_pos - 6))


def wyswietl_wspolrzedne_kursora(screen, mouse_x, mouse_y):
    """Wyświetla współrzędne kursora myszy jeśli znajduje się on w obszarze płótna, w przeciwnym przypadku współrzędne znikają"""

    (x, y) = wspol_osiowe((mouse_x, mouse_y), canvas_rect)
    if canvas_rect.collidepoint(mouse_x, mouse_y):
        wyswietl_tekst(f'x:{x}, y:{y}', screen, wspolrzedne_rect, font_size=15, background_color=GREY)
    else:
        pygame.draw.rect(screen, GREY, wspolrzedne_rect)  # współrzędne znikają, gdy kursor myszy poza obszarem płótna


def wyswietl_wielokat(screen, sciezka_do_pliku:str):
    """Wyświetla na płótnie wielokąt załadowany z pliku"""

    rysunek = pygame.image.load(sciezka_do_pliku)
    rysunek = pygame.transform.scale(rysunek, (canvas_width, canvas_height))
    draw_canvas_area(screen) # wyczyszczenie płótna
    screen.blit(rysunek, canvas_rect.topleft)  # naniesienie striangulowanego wielokąta
    draw_grid(screen)
    draw_axes(screen)
    

def wyswietl_menu(screen, ktory_aktywny:Union[int, None], ktore_mozliwe:List[int]):
    dlugosc_menu = 4
    menu = [None for i in range(dlugosc_menu)]  # prostokąty z elementami menu
    teksty = ["Pokaż wielokąt", "Pokaż triangulację", ["Pokaż obszary,", "które widzą strażnicy"], "Rysuj nowy wielokąt"]  # teksty wyświetlane na elementach menu
    kolory_tekstu = [BLACK if ktore_mozliwe[i] else DARK_GREY for i in range(3)] + [RED]
    kolory_menu = [WHITE if ktore_mozliwe[i] else LIGHT_GREY for i in range(dlugosc_menu)]  # kolory elementów menu, zależne od argumentów ktory_aktywny i ktore_mozliwe
    if ktory_aktywny is not None:
        kolory_tekstu[ktory_aktywny] = BLACK
        kolory_menu[ktory_aktywny] = YELLOW
    
    for i in range(dlugosc_menu):
        menu[i] = pygame.Rect(canvas_rect.right + 20, canvas_rect.top + i * 100, odstep_prawa-40, 80)
        wyswietl_tekst(teksty[i], screen, menu[i], color=kolory_tekstu[i], background_color=kolory_menu[i])

    return menu


def wyczysc_plotno(screen):
    draw_canvas_area(screen)
    draw_grid(screen)
    draw_axes(screen)










