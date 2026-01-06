def turn_right():
    for i in range(3):
        turn_left()
        
while front_is_clear():
    move()
turn_left() 

while not at_goal():
    if not wall_on_right():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
        if front_is_clear():
            move()
