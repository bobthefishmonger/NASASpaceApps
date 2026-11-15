import pygame
import tiles


pygame.init()

sol = 1
food = "10 tonnes"
power = "100%"
oxygen_level = 10
radiation_exposure = 0.5
Definitions = "DEFINITIONS"
time_elapsed = 0
time_since_sol = 0

pause_button_clicked = False 
resume_button_clicked = True
Definitions_button_clicked = False

mouseClicked = False

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
Definitions_display = None
daily_message = None
pause_message = None
sol_text_object = None
Food_amount_object = None
Power_level_object = None
Oxygen_level_object = None
Radiation_exposure_level_object = None
daily_message_object = None
pause_message_object = None
Definitions_object = None
play_button_object = None

def updateDisplays():
    global sol_text_display, Food_amount_display, Power_level_display, Oxygen_level_display, Definitions_display
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
    Definitions_display = font1.render(Definitions, True, (65, 105, 225))


def render():
    global sol_text_display, Food_amount_display, Power_level_display, Oxygen_level_display
    global Radiation_exposure_level_display, daily_message, pause_message
    global sol_text_object, Food_amount_object, Power_level_object, Oxygen_level_object
    global Radiation_exposure_level_object, daily_message_object, pause_message_object, play_button_object, Definitions_object
    updateDisplays()
    screen.fill((0, 0, 0))
    if pause_button_clicked:
        active = False
        pause_message = font2.render("GAME PAUSED", True, (255, 255, 255))
        play_button = font2.render("RESUME", True, (157, 0, 250))
        play_button_object = screen.blit(play_button, (350, 100))
    else:
        pause_message = font2.render("❚❚ PAUSE", True, (255, 255, 255))
        if sol == 1:
            daily_message = font2.render(
                "You are now on Sol: 1. Please check the events calender for a list of the day's challenges!",
                True,
                (255, 255, 255),
            )
            daily_message_object = screen.blit(daily_message, (350, 580))

    sol_text_object = screen.blit(sol_text_display, (10, 10))
    Food_amount_object = screen.blit(Food_amount_display, (50, 10))
    Power_level_object = screen.blit(Power_level_display, (160, 10))
    Oxygen_level_display = screen.blit(Oxygen_level_display, (250, 10))
    pause_message_object = screen.blit(pause_message, (700, 10))
    Definitions_object = screen.blit(Definitions_display, (10, 30))
    Radiation_exposure_level_object = screen.blit(Radiation_exposure_level_display, (470, 10))
    pygame.display.flip()


def processclicks():
    global sol_text_object, Food_amount_object, Power_level_object, Oxygen_level_object
    global Radiation_exposure_level_object, daily_message_object, pause_message_object, play_button_object
    global resume_button_clicked, pause_button_clicked, Definitions_button_clicked
    mouse = pygame.mouse.get_pos()
    if pause_message_object.collidepoint(mouse):
        resume_button_clicked = not resume_button_clicked
        pause_button_clicked = not pause_button_clicked
    if Definitions_object.collidepoint(mouse):
        Definitions_button_clicked = True
    try:
        if play_button_object.collidepoint(mouse):
                    resume_button_clicked = True
                    pause_button_clicked = False
    except:
        pass
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

text = "DEFINITIONS:  " + "                       Radiation Exposure -> This is invisible energy from the Sun and Stars that can harm astronauts if they get too much exposure." +  "                           Oxygen Level -> The amount of oxygen in the colony's air that astronauts need to breathe safely, it can be dangerous if too low or too high!" + "               Sol -> One day on Mars, it lasts about 24 hours and 39 minutes." +"                         Sun Flare -> A sudden burst of energy from the Sun that can send harmful radiation into space and affect astronauts. They also affect spacecraft equipment." + "                        Dust Storm -> Strong winds that blow lots of tiny dust particles into the air. On Mars, dust storms can cover huge areas, block sunlight, and cover solar panels."

if Definitions_button_clicked:
    from tkinter import *
    from tkinter import messagebox
    messagebox.showinfo("Definitions", text)


