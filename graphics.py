import pygame
import tiles

pygame.init()

sol = 1
food = "10 tonnes"
power = "100%"
oxygen_level = 10
radiation_exposure = 0.5
time_elapsed = 0
time_since_sol = 0

pause_button_clicked = True
resume_button_clicked = False

clock = pygame.time.Clock()
running = True
active = True

font1 = pygame.font.Font(None, 16)
font2 = pygame.font.Font(None, 18)

screen = pygame.display.set_mode((800, 600))

SOLTIME = 600_000_00


sol_text_display = None
Food_amount_display = None
Power_level_display = None
Oxygen_level_display = None
Radiation_exposure_level_display = None
daily_message = None
pause_message = None


def updateDisplays():
    global sol_text_display
    global Food_amount_display
    global Power_level_display
    global Oxygen_level_display
    global Radiation_exposure_level_display
    global daily_message
    global pause_message
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
    global sol_text_display
    global Food_amount_display
    global Power_level_display
    global Oxygen_level_display
    global Radiation_exposure_level_display
    global daily_message
    global pause_message
    updateDisplays()
    screen.fill((0, 0, 0))
    if pause_button_clicked:
        active = False
        pause_message = font2.render("GAME PAUSED", True, (255, 255, 255))
        play_button = font2.render("RESUME", True, (157, 0, 250))
        screen.blit(play_button, (350, 100))
    else:
        pause_message = font2.render("❚❚ PAUSE", True, (255, 255, 255))
        if sol == 1:
            daily_message = font2.render(
                "You are now on Sol: 1. Please check the events calender for a list of the day's challenges!",
                True,
                (255, 255, 255),
            )
        screen.blit(daily_message, (350, 580))

    screen.blit(sol_text_display, (10, 10))
    screen.blit(Food_amount_display, (50, 10))
    screen.blit(Power_level_display, (160, 10))
    screen.blit(Oxygen_level_display, (250, 10))
    screen.blit(pause_message, (700, 10))
    screen.blit(Radiation_exposure_level_display, (470, 10))
    pygame.display.flip()


while running:
    render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

    if resume_button_clicked:
        active = True
        pause_button_clicked = False
        time_elapsed += pygame.time.get_ticks()
        time_since_sol = time_elapsed - SOLTIME * (sol - 1)
    if time_since_sol >= SOLTIME:
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
