from pygame import*
window = display.set_mod((700,500))
clock = time.clock()
FPS = 60
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    window.fill((100,100,100))
   
    display.update()
    clock.tick(FPS)

