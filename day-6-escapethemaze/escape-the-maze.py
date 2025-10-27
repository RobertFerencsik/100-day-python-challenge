# Not defined functions are defined in Reeborg's world
def turn_left():
    """
    In Reeborg"s world: turns the robot left
    :return:
    """
    pass

def at_goal():
    """
    In Reeborg's world check's if the robot is at the end or not
    :return: Boolean
    """
    pass

def turn_right():
    turn_left()
    turn_left()
    turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()