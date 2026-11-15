import pygame
running = True
grid_rows=8
grid_cols=10
cell_size=64
# Class widget or pop-up window
#I used AI to find out help structure the code
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
    
    mouse_row=mouse_y//cell_size
    mouse_col=mouse_x//cell_size

    return (mouse_col,mouse_row)


'''def building(popup_open,selected_cell,cell_roles,tile_options,screen):
    popup_rect=pygame.Rect(0,0,240,420)
    popup_rect.center=screen.get_rect().center

    option_rects=[]
    for i in range(len(tile_options)):
        option_button=pygame.Rect(0,0,200,40)
        option_button.centerx=popup_rect.centerx
        option_button.y=popup_rect.y+40+i*45
        option_rects.append(option_button)
'''


# i used AI to help me find bugs
screen = pygame.display.set_mode((grid_cols*cell_size,grid_cols*cell_size)) 
#ai used here start
popup_open=True
selected_cell=None
cell_roles={}
tile_options=["Martian Surface", "Habitat","Farm","Solar Panel",
              "Nuclear Reactor","Oxygen","Science", "Launch site"]

popup_rect=pygame.Rect(0,0,240,420)
popup_rect.center=screen.get_rect().center
for i in range(len(tile_options)):

    option_rects=[]

    option_button=pygame.Rect(0,0,200,40)
    option_button.centerx=popup_rect.centerx
    option_button.y=popup_rect.y+40+i*45
    option_rects.append(option_button)

    dim_surface = pygame.Surface(screen.get_size())
    dim_surface.set_alpha(150)
    dim_surface.fill((0, 0, 0))
#ai used here end
while running:
    screen.fill((20,20,20))
    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:

            mouse_pos=onclick_grid(cell_size,event)
            print(mouse_pos)
            #written by AI (start)
            
        #written by AI end  

        grid(grid_rows,grid_cols,cell_size)

       

            
pygame.quit()