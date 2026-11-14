import pygame
pygame.init()
running = True
grid_rows=8
grid_cols=10
cell_size=64

#i used AI to find out help structure the code
def grid(grid_rows,grid_cols,cell_size):

    hud_height=(grid_cols-grid_rows)*cell_size
    
    screen.fill((20,20,20))

    grid_width=grid_rows*cell_size

    for row_no in range(grid_rows):

        for col_no in range (grid_cols):
            
            rect=pygame.Rect(cell_size*col_no,hud_height+cell_size*row_no, cell_size, cell_size)
            pygame.draw.rect(screen,(100,100,100),rect,1)

    pygame.display.flip()

    return rect

def onclick_grid(cell_size,event):
        
    mouse_x,mouse_y=event.pos
    
    mouse_row=mouse_x//cell_size
    mouse_col=mouse_y//cell_size

    return (mouse_col,mouse_row)

#def buildingType():


# i used AI to help me find bugs
screen = pygame.display.set_mode((grid_cols*cell_size,grid_cols*cell_size))
while running:
    screen.fill((20,20,20))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            print(onclick_grid(cell_size,event))

        grid(grid_rows,grid_cols,cell_size)
       
pygame.quit()