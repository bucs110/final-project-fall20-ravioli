import random

def randomDirection(count, direction):
    """
    determines if the enemy is finished walking its path and determines new direction
    Args:
    count --> (int) the total number of steps the enemy is in its path
    direction --> (str) direction that the enemy is walking
    Return: (str) direction
    """
    if count == 0:
        direction_generation = random.randrange(0, 8)
        if direction_generation == 0:
            direction = "up"
        if direction_generation == 1:
            direction = "down"
        if direction_generation == 2:
            direction = "right"
        if direction_generation == 3:
            direction = "left"
        if direction_generation >= 4:
            direction = "none"
    else:
        return direction
    return direction

def makeOppositeDirections(direction):
    """
    Takes in a direction and returns the opposite direction
    Args:
    direction --> (str) the direction the object is moving in
    Return --> (str) the opposite direction
    """
    direction = direction
    if direction == "up":
        direction = "down"
    elif direction == "down":
        direction = "up"
    elif direction == "right":
        direction = "left"
    elif direction == "left":
        direction = "right"
    return direction
