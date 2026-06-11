import pygame as py 
py.init()
display = py.display.set_mode((1000,700))
on = True
cordsY = -3000
cordsX  = 0

while on :
    keys = py.key.get_pressed()
    if keys[py.K_w]:
        cordsY += 10
    if keys[py.K_s]:
        cordsY -= 10
    py.display.update()
    display.blit(py.image.load("Project.py\Earth-Moon.png"),(cordsX,cordsY))
    for event in py.event.get() :
        if event.type == py.QUIT:
          on = False