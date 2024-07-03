
define a = Character("Neco Arc")

transform flip(x):
    xzoom x

transform fill_screen:
    xanchor 0.5
    yanchor 0.5
    xpos 0.5
    ypos 0.5
    xzoom 10
    yzoom 10

label start:

    scene rizal park at fill_screen

    $ flag = True

    $ count = 1

    $ thingamajig = 10

    jump start2

    return

label start2:

    if flag:
        if (renpy.random.randint(0, 2) == 1): 
            show neco arc at topleft
        else: 
            show neco arc at left
        show neco arc at flip(1)
    else:
        if (renpy.random.randint(0, 2) == 1): 
            show neco arc at topright
        else: 
            show neco arc at right
        show neco arc at flip(-1)

    with move
    with vpunch
    
    $ flag = not flag

    $ say = "BURUNYUU " * count

    a "[say]"

    if count > thingamajig:
        $ count = 1
        $ thingamajig = renpy.random.randint(5, 15)
    else:
        $ count += 1

    jump start2
