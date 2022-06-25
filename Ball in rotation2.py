import pygame
pygame.init()
screen = pygame.display.set_mode([1000,1000])
clock = pygame.time.Clock()
img=[pygame.image.load('ball.png')]*5
angle=[0]*5
image=[0]*5
rect=[0]*5
X,Y=[500,250,750,750,250],[500,250,250,750,750]
q=[3,8,-6,12,-10]
while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    for i in range(0,5):
        image[i]=pygame.transform.rotate(img[i],angle[i])
        rect[i]=image[i].get_rect(center=(X[i],Y[i]))
    screen.fill('purple')
    for i in range(0,5):
        screen.blit(image[i],rect[i])
        angle[i]=angle[i]+q[i]                          
    clock.tick(120)
    pygame.display.update()
 