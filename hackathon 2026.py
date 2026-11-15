import pygame

pygame.init()  # starts the pygame modules
sol = 1
food = "10 tonnes"
power = "100%"
oxygen_level = 10
radiation_exposure = 0.5

pause_button_clicked = True ######!!!!!!!!remove this before combining with other code, this is just for testing purposes!!!
resume_button_clicked = False ######!!!!!!!!remove this before combining with other code, this is just for testing purposes!!!


clock = pygame.time.Clock() #creates a clock object to manage time
running = True
active = True

if 19.5 <= oxygen_level <= 23.5:
    oxygen_text = " (Safe)"
elif oxygen_level < 19.5:
    oxygen_text = " (Increase oxygen levels)"
else:
    oxygen_text = " (Decrease oxygen levels)"


if radiation_exposure < 0.64:
    radiation_text = " (Safe)"
elif radiation_exposure >= 0.64 and radiation_exposure < 0.9:
    radiation_text = " (Moderate)"
else:
    radiation_text = " (High)"

font1 = pygame.font.Font(
    None, 16
)  # creates a font object with the default font and size 16
font2 = pygame.font.Font(
    None, 18
)  # creates a font object with the default font and size 12


screen = pygame.display.set_mode(
    (800, 600)
)  ###########!!!!!!remove this before combining with other code, this is just for testing purposes!!!


Sol_text = font1.render(
    "Sol:" + str(sol), True, (255, 255, 255)
)  # 'true' makes the text smoother (it makes the text have smoother edges), (255, 255, 255) makes the text white
Food_amount = font1.render("Food: " + food, True, (255, 255, 255))
Power_level = font1.render("Power: " + power, True, (255, 255, 255))
if oxygen_text == " (Safe)":
    Oxygen_level = font1.render(
        "Oxygen: " + str(oxygen_level) + oxygen_text, True, (0, 255, 0)
    )  # makes the text green if the oxygen level is safe
else:
    Oxygen_level = font1.render(
        "Oxygen: " + str(oxygen_level) + oxygen_text, True, (255, 0, 0)
    )  # makes the text red if the oxygen level is high or low
if radiation_text == " (Safe)":
    Radiation_exposure_level = font1.render(
        "Radiation Exposure: " + str(radiation_exposure) + "mSv/day" + radiation_text,
        True,
        (0, 255, 0),
    )  # green if it is safe
elif radiation_text == " (Moderate)":
    Radiation_exposure_level = font1.render(
        "Radiation Exposure: " + str(radiation_exposure) + "mSv" + radiation_text,
        True,
        (255, 255, 0),
    )  # yellow if it is moderate
else:
    Radiation_exposure_level = font1.render(
        "Radiation Exposure: " + str(radiation_exposure) + "mSv/day" + radiation_text,
        True,
        (255, 0, 0),
    )  # red if it is high

screen.fill((0, 0, 0))  # fills the screen with black color
screen.blit(
    Sol_text, (10, 10)
)  # blits the text to the screen at the coordinates (10, 10) #pixels are in rows and columns
screen.blit(Food_amount, (50, 10))
screen.blit(Power_level, (160, 10))
screen.blit(Oxygen_level, (250, 10))
if oxygen_text != " (Safe)":
    screen.blit(Radiation_exposure_level, (470, 10))
else:
    screen.blit(Radiation_exposure_level, (400, 10))
pygame.display.flip()  # updates the display to show the text




clock = pygame.time.Clock()  # creates a clock object to manage time
running = True

time_elapsed = 0 #initializes the time elapsed variable to 0

if active:
    time_elapsed += pygame.time.get_ticks() / sol #increments the time elapsed variable by the number of milliseconds since the game started
    
    screen.fill((0, 0, 0)) #fills the screen with black color   ############!!!remove this as well
    screen.blit(Sol_text, (10, 10)) #blits the text to the screen at the coordinates (10, 10) #pixels are in x and y coordinates
    screen.blit(Food_amount, (50, 10))
    screen.blit(Power_level, (160, 10))
    screen.blit(Oxygen_level, (250, 10))
    screen.blit(pause_message, (700, 10)) #blits the pause button to the screen at the coordinates (450, 10)
    if oxygen_text != ' (Safe)':
        screen.blit(Radiation_exposure_level, (470, 10))
    else:
        screen.blit(Radiation_exposure_level, (400, 10))
    pygame.display.flip() #updates the display to show the text
else:
    screen.fill((0, 0, 0)) #fills the screen with black color   ############!!!remove this as well
    screen.blit(Sol_text, (10, 10)) #blits the text to the screen at the coordinates (10, 10) #pixels are in rows and columns
    screen.blit(Food_amount, (50, 10))
    screen.blit(Power_level, (160, 10))
    screen.blit(Oxygen_level, (250, 10))
    screen.blit(pause_message, (700, 10)) #blits the pause button to the screen at the coordinates (450, 10)
    if oxygen_text != ' (Safe)':
        screen.blit(Radiation_exposure_level, (470, 10))
    else:
        screen.blit(Radiation_exposure_level, (400, 10))
    play_button = font2.render("RESUME", True, (157, 0, 250)) #creates a play button with the text "Resume" in purple color
    screen.blit(play_button, (350, 100)) #blits the play button to the screen at the coordinates (350, 100)
    pygame.display.flip() #updates the display to show the play button

if resume_button_clicked:
    active = True #sets the active variable to true, which will start the game loop again
    pause_button_clicked = False #sets the pause button clicked variable to false, which will change the pause button text back to "Pause"
    time_elapsed += pygame.time.get_ticks() / sol #increments the time elapsed variable by the number of milliseconds since the game started

while running: #while the game is running, the following code will run
    for event in pygame.event.get():
        if (
            event.type == pygame.QUIT
        ):  # if the user tries to close the window by clicking the X on the top, pygame realises it. pygame.QUIT means the user clicked X to close the window
            running = False
            pygame.quit() #quits the game
        else:
            if (
                pygame.time.get_ticks() == 600000 and sol < 100
            ):  # checks if 600000 milliseconds have elapsed since the game started
                sol += 1  # increments the sol days
                daily_message = font2.render(
                    "You are now on Sol:"
                    + str(sol)
                    + ". Please check the events calender for a list of the day's challenges!",
                    True,
                    (255, 255, 255),
                )
                screen.blit(
                    daily_message, (350, 580)
                )  # blits the daily message to the screen at the coordinates (350,580)
            elif (
                sol == 100 and pygame.time.get_ticks() == 600000
            ):  # checks if the sol days have reached 100 and if 600000 milliseconds have elapsed since the game started
                sol_message = font2.render(
                    "You have completed 100 Sol days! Close the game or the Sol days will reset to 1.",
                    True,
                    (255, 255, 255),
                )  # creates a message to inform the user that they have completed 100 Sol days and that the Sol days will reset to 1 if they do not close the game
                sol = 1  # resets the sol days to 1 if it reaches 100
                daily_message = font2.render(
                    "You are now on Sol:"
                    + str(sol)
                    + ". Please check the events calender for a list of the day's challenges!",
                    True,
                    (255, 255, 255),
                )
                screen.blit(
                    daily_message, (350, 580)
                )  # blits the daily message to the screen at the coordinates (350,580)
