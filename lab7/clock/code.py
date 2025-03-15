import pygame as p
import datetime as d


p.init()
screen = p.display.set_mode((800,600))
run = True
clock = p.time.Clock()
back = p.image.load("C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\clock\\fon.jpg")
r_hand = p.image.load("C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\clock\\right.png")
l_hand = p.image.load("C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\clock\\left.png")
now = d.datetime.now()
sec = now.second; seconds = -sec * 6
minn = now.minute;minutes = -minn * 6
print(sec)
print(minn)
image_center = (400,300)


while run:
    for i in p.event.get():
        if i.type == p.QUIT:
            run = False


    right_hand = p.transform.rotate(r_hand,minutes)
    minutes -= 1/600
    right = right_hand.get_rect(center = image_center)

    left_hand = p.transform.rotate(l_hand,seconds)
    seconds -= 1/10
    left = left_hand.get_rect(center = image_center)

    screen.blit(back, (0,0))
    screen.blit(right_hand, right)
    screen.blit(left_hand, left)



    p.display.flip()   
    clock.tick(60) 
