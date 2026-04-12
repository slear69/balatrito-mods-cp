import pygame as py
py.init()
display = py.display.set_mode((1500, 800))
clock = py.time.Clock()
# Load image ONCE
sky = py.image.load("images/sky.png")
on = True
cordsY = -14200
cordsX = 0

while on:
    clock.tick(60)  
    keys = py.key.get_pressed()
    if keys[py.K_w] and cordsY < 0:
        cordsY += 50
    if keys[py.K_s] and cordsY > -14200:
        cordsY -= 10
    display.fill((0, 0, 0))
    display.blit(sky, (cordsX, cordsY))
    py.display.update()
    for event in py.event.get() :
        if event.type == py.QUIT:
          on = False