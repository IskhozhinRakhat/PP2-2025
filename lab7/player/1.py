import pygame as p

sen = "C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\player\\Айкын Толепберген - Жалгыз сен.mp3"
pah = "C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\player\\Айкын Толепберген - Пах пах.mp3"
tun = "C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\player\\Кайрат Нуртас - Алматының Түндер-Ай.mp3"
senemes = "C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\player\\Кайрат Нуртас - Ол Сен Емес.mp3"
songs = [sen,pah,tun,senemes]

screen = p.display.set_mode((800,600))
p.init()
idx = 0; run = True; igraet = False

image = p.image.load("C:\\Users\\Рахат\\Desktop\\PP2-2025\\lab7\\player\\unnamed.png")
image = p.transform.scale(image, (800,520))

color_button1 = (255,255,255)
color_button2 = (255,255,255)

clock = p.time.Clock()
t = 0

while run:
    for i in p.event.get():
        if i.type == p.QUIT:
            run = False
        if i.type == p.KEYDOWN:
            if i.key == p.K_RIGHT:
                idx = (idx + 1) % len(songs)
                p.mixer.music.load(songs[idx])
                p.mixer.music.play()
                igraet = True
                color_button1 = (0,123,167)
            if i.key == p.K_LEFT:
                idx = (idx - 1) % len(songs)
                p.mixer.music.load(songs[idx])
                p.mixer.music.play()
                igraet = True
                color_button2 = (0,123,167)
            if i.key == p.K_SPACE:
                if igraet == True:
                    p.mixer.music.pause()
                    igraet = False
                else:
                    p.mixer.music.load(songs[idx])
                    p.mixer.music.play()
                    igraet = True

    if igraet and not p.mixer.music.get_busy():
        idx = (idx + 1) % len(songs)
        p.mixer.music.load(songs[idx])
        p.mixer.music.play()
        igraet = True
    screen.blit(image,(0,0))
    t += 1
    if t == 10:
        color_button1 = (255,255,255)
        color_button2 = (255,255,255)
        t = 0
    p.draw.rect(screen, (0,0,0), (0,520,800,80))
    p.draw.circle(screen, (255,255,255), (400,560),40)
    if not igraet:
        p.draw.polygon(screen, (0,0,0),((388,540),(388,580),(420,560)))
    else:
        p.draw.line(screen,(0,0,0), (387,540),(387,580),10)
        p.draw.line(screen,(0,0,0), (410,540),(410,580),10)

    p.draw.polygon(screen, color_button1,((488,540),(488,580),(520,560)))
    p.draw.polygon(screen, color_button2,((312,540),(312,580),(280,560)))
    p.draw.line(screen, color_button1, (520,540), (520,580), 5)
    p.draw.line(screen, color_button2, (280,540), (280,580), 5)
    

    p.display.flip()
    clock.tick(60)

p.quit()