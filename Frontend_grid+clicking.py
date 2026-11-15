import pygame
import pygamepopup
from pygamepopup.components import Button, InfoBox
from pygamepopup.menu_manager import MenuManager
running = True

pygame.init()
pygamepopup.init()
grid_rows=8
grid_cols=10
cell_size=67.5

screen = pygame.display.set_mode((grid_cols*cell_size,grid_cols*cell_size)) 
menu_manager = MenuManager(screen)
cell_roles={}
tile_options=["Martian Surface", "Habitat","Farm","Solar Panel",
              "Nuclear Reactor","Oxygen","Science", "Launch site"]

#I used AI to help structure this code
def draw_grid(grid_rows,grid_cols,cell_size):

    screen.fill((20,20,20))

    hud_height=(grid_cols-grid_rows)*cell_size
    hud=pygame.Rect(0,0, grid_cols*cell_size, hud_height)
    pygame.draw.rect(screen, (255,255,255), hud, 1)

    grid_width=grid_rows*cell_size
    grid = []
    row = []
    for row_no in range(grid_rows):
        row = []
        for col_no in range (grid_cols):
           grid_square=pygame.Rect(cell_size*col_no,cell_size*row_no, cell_size, cell_size)
           pygame.draw.rect(screen,(100,100,100),grid_square,1)
           row.append(grid_square)
        grid.append(row)
    
    return grid
def onclick_grid(grid_rows,grid_cols,cell_size):

    grid = draw_grid(grid_rows,grid_cols,cell_size)

    mouse = pygame.mouse.get_pos()
    for i in range (grid_rows):
        for j in range (grid_cols):
            if grid[i][j].collidepoint(mouse):
                return i,j
    return 0,0
                
# i used AI to help me find bugs
#ai used here start
popup_open=True
selected_cell=None

while running:
    screen.fill((20,20,20))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_col,mouse_row=onclick_grid(grid_rows,grid_cols,cell_size)
            print(mouse_col,mouse_row)




        draw_grid(grid_rows,grid_cols,cell_size)

       

            
pygame.quit()