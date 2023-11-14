# hurdle 4
# this will not work here. 
# open reborgs https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json and run this
def turn_right():
    turn_left()
    turn_left()    
    turn_left()
    
def jump():
    jump_height = 0
    turn_left()
    move()
    while not right_is_clear():
       move()
       jump_height += 1
    else:
        turn_right()
        move()
        turn_right()
        while (jump_height >= 0):
            move()
            jump_height -= 1
        turn_left()

while not at_goal():
    if (front_is_clear()):
        move()
    else:
        jump()

