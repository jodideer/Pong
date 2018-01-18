import pygame
pygame.init()

white=(255,255,255)#256th element of red, green and blue
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)

gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('PONG')


gameExit=False

lead_x=300
lead_y=300
lead_x_change=0
lead_y_change=0


clock=pygame.time.Clock()


while not gameExit:
    for event in pygame.event.get():
        #quit current game
        if event.type==pygame.QUIT:
            gameExit=True

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0
            elif event.key==pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0
                
            elif event.key==pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0
            elif event.key==pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0
                
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                lead_x_change=0


    lead_x+=lead_x_change
    lead_y+=lead_y_change
    
    gameDisplay.fill(black)
    pygame.draw.rect(gameDisplay,blue,[50,30,10,80])#co-ordinates,width,height
    #gameDisplay.fill(green,rect=[725,30,10,80])

    pygame.display.update()
    clock.tick(15)
    
            
        

#quit and close entire game
pygame.quit()
quit()
