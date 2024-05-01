from pygame import *

window = display.set_mode((600,600))
display.set_caption('Лабиринт')
BG = transform.scale(image.load('ping.png'),(600,600))
clock = time.Clock()
player1 = transform.scale(image.load('pingg.jpg'),(80,80))
x1,y1 = 120,400
player2 = transform.scale(image.load('images.jpg'),(90,85))
x2,y2 = 400,500
run = True
while run:
    window.blit(BG, (0,0))
    for e in event.get():
        if e .type ==QUIT:
            run = Falsew
    key_pressed = key.get_pressed()
    if key_pressed[K_w] and y1> 0: 
        y1 -= 5
    if key_pressed[K_s]and y1 < 520:
        y1 += 5
    if key_pressed[K_UP] and y2 > 0:
        y2-= 5
    if key_pressed[K_DOWN]and y2 < 520:
        y2 += 5
    window.blit(player1, (x1,y1))
    window.blit(player2, (x2,y2))
    display.update()
    clock.tick(60)