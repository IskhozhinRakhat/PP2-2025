import pygame as p

p.init()
screen = p.display.set_mode((800,600))
x, y = 400,300
run = True
clock = p.time.Clock()
while run:
    for i in p.event.get():
        if i.type == p.QUIT:
            run = False

    pressed = p.key.get_pressed()
    if pressed[p.K_UP] and y >= 25: y -= 20
    if pressed[p.K_DOWN]and y <= 575: y += 20
    if pressed[p.K_LEFT] and x >= 25: x -= 20
    if pressed[p.K_RIGHT] and x <= 775: x += 20

    screen.fill((255,255,255))
    p.draw.circle(screen, (200,0,0), (x,y), 25)
    p.display.flip()
    clock.tick(60)
p.quit()
    