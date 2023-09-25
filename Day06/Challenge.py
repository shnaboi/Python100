# Day 06 challenge was reeborg's world (the maze level)
# http://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def find_exit():
    while not at_goal():
        if wall_on_right():
            while wall_in_front():
                turn_left()
            move()
        
        else:
            turn_right()
            move()

find_exit()