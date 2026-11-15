import pygame
import tiles
import pygamepopup
from pygamepopup.components import Button, InfoBox
from pygamepopup.menu_manager import MenuManager

pygame.init()
grid = []
sol = 1
food = "10 tonnes"
power = "100%"
oxygen_level = 10
radiation_exposure = 0.5
time_elapsed = 0
time_since_sol = 0

YOffset = 50

clock = pygame.time.Clock().tick(60)

isPlaying = False

mouseClicked = False

clock = pygame.time.Clock()
running = True

font1 = pygame.font.Font(None, 16)
font2 = pygame.font.Font(None, 18)

screen = pygame.display.set_mode((800, 650))
menu_manager = MenuManager(screen)

SOLTIME = 60_000

change = True

grid_rows = 8
grid_cols = 10
cell_size = 67.5


sol_text_display = None
Food_amount_display = None
Power_level_display = None
Oxygen_level_display = None
Radiation_exposure_level_display = None
daily_message = None
pause_message = None
sol_text_object = None
Food_amount_object = None
Power_level_object = None
Oxygen_level_object = None
Radiation_exposure_level_object = None
daily_message_object = None
pause_message_object = None


def updateDisplays():
    global sol_text_display, Food_amount_display, Power_level_display, Oxygen_level_display
    global Radiation_exposure_level_display, daily_message, pause_message
    if 19.5 <= oxygen_level <= 23.5:
        oxygen_text = " (Safe)"
        Oxygen_level_display = font1.render(
            "Oxygen: " + str(oxygen_level) + oxygen_text, True, (0, 255, 0)
        )
    elif oxygen_level < 19.5:
        oxygen_text = " (Increase oxygen levels)"
        Oxygen_level_display = font1.render(
            "Oxygen: " + str(oxygen_level) + oxygen_text, True, (255, 255, 0)
        )
    else:
        oxygen_text = " (Decrease oxygen levels)"
        Oxygen_level_display = font1.render(
            "Oxygen: " + str(oxygen_level) + oxygen_text, True, (255, 0, 0)
        )

    if radiation_exposure < 0.64:
        radiation_text = " (Safe)"
        Radiation_exposure_level_display = font1.render(
            "Radiation Exposure: "
            + str(radiation_exposure)
            + "mSv/day"
            + radiation_text,
            True,
            (0, 255, 0),
        )
    elif radiation_exposure >= 0.64 and radiation_exposure < 0.9:
        radiation_text = " (Moderate)"
        Radiation_exposure_level_display = font1.render(
            "Radiation Exposure: " + str(radiation_exposure) + "mSv" + radiation_text,
            True,
            (255, 255, 0),
        )
    else:
        radiation_text = " (High)"
        Radiation_exposure_level_display = font1.render(
            "Radiation Exposure: "
            + str(radiation_exposure)
            + "mSv/day"
            + radiation_text,
            True,
            (255, 0, 0),
        )

    sol_text_display = font1.render("Sol:" + str(sol), True, (255, 255, 255))
    Food_amount_display = font1.render("Food: " + food, True, (255, 255, 255))
    Power_level_display = font1.render("Power: " + power, True, (255, 255, 255))


def render():
    global sol_text_display, Food_amount_display, Power_level_display, Oxygen_level_display
    global Radiation_exposure_level_display, daily_message, pause_message
    global sol_text_object, Food_amount_object, Power_level_object, Oxygen_level_object
    global Radiation_exposure_level_object, daily_message_object, pause_message_object, play_button_object
    global grid, change
    if change:
        updateDisplays()
        screen.fill((0, 0, 0))
        if not isPlaying:

            pause_message = font2.render("GAME PAUSED", True, (255, 255, 255))
            play_button = font2.render("RESUME", True, (157, 0, 250))
            play_button_object = screen.blit(play_button, (350, 100))
        else:
            grid = draw_grid(grid_rows, grid_cols, cell_size)
            pause_message = font2.render("❚❚ PAUSE", True, (255, 255, 255))
            if sol == 1:
                daily_message = font2.render(
                    "You are now on Sol: 1. Please check the events calender for a list of the day's challenges!",
                    True,
                    (255, 255, 255),
                )
                daily_message_object = screen.blit(daily_message, (350, 630))

        sol_text_object = screen.blit(sol_text_display, (10, 10))
        Food_amount_object = screen.blit(Food_amount_display, (50, 10))
        Power_level_object = screen.blit(Power_level_display, (160, 10))
        Oxygen_level_display = screen.blit(Oxygen_level_display, (250, 10))
        pause_message_object = screen.blit(pause_message, (700, 10))
        Radiation_exposure_level_object = screen.blit(
            Radiation_exposure_level_display, (470, 10)
        )
        pygame.display.flip()
        change = False


TILETOCOLOUR = {
    "MartianSurface": (150, 100, 75),
    "Habitat": (180, 180, 190),
    "Farm": (80, 180, 70),
    "SolarPanel": (40, 90, 200),
    "NuclearReactor": (220, 100, 40),
    "OxygenScrubber": (100, 220, 255),
    "ScienceSite": (180, 80, 220),
    "LaunchSite": (240, 220, 100),
}

import tiles


def draw_grid(grid_rows, grid_cols, cell_size):
    grid = []
    row = []
    for row_no in range(grid_rows):
        row = []
        for col_no in range(grid_cols):
            grid_square = pygame.Rect(
                cell_size * col_no, cell_size * row_no + YOffset, cell_size, cell_size
            )
            tiles.GameMap.grid
            pygame.draw.rect(
                screen,
                TILETOCOLOUR[tiles.GameMap.grid[row_no][col_no].name],
                grid_square,
            )
            pygame.draw.rect(
                screen,
                (0, 0, 0),
                grid_square,
                width=1,
            )
            row.append(grid_square)
        grid.append(row)
    pygame.display.flip()

    return grid


def processclicks():
    global sol_text_object, Food_amount_object, Power_level_object, Oxygen_level_object
    global Radiation_exposure_level_object, daily_message_object, pause_message_object, play_button_object
    global isPlaying, grid, change
    mouse = pygame.mouse.get_pos()
    if play_button_object.collidepoint(mouse):
        isPlaying = True
        change = True
    if pause_message_object.collidepoint(mouse):
        isPlaying = False
        change = True
    for i in range(grid_rows):
        for j in range(grid_cols):
            try:
                if grid[i][j].collidepoint(mouse):
                    squareCoords = (i, j)
                    print(i, j)
            except:
                pass


def createSolMessage(sol):
    global daily_message, sol_text, sol_message
    if sol < 100:
        sol += 1
        daily_message = font2.render(
            "You are now on Sol:"
            + str(sol)
            + ". Please check the events calender for a list of the day's challenges!",
            True,
            (255, 255, 255),
        )
        sol_text = font1.render("Sol:" + str(sol), True, (255, 255, 255))
    else:
        sol_message = font2.render(
            "You have completed 100 Sol days! Close the game or the Sol days will reset to 1.",
            True,
            (255, 255, 255),
        )
        sol = 1
        daily_message = font2.render(
            "You are now on Sol:"
            + str(sol)
            + ". Please check the events calender for a list of the day's challenges!",
            True,
            (255, 255, 255),
        )
    return sol


while running:
    render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseClicked = True
            processclicks()
        if event.type == pygame.MOUSEBUTTONUP:
            mouseClicked = False
    if isPlaying:
        time_elapsed = pygame.time.get_ticks()
        time_since_sol = time_elapsed - SOLTIME * (sol - 1)
    if time_since_sol >= SOLTIME:
        sol = createSolMessage(sol)
        change = True
