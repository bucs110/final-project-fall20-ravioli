import random
import os
import pygame
import bin.enemy

def randomDirection(count, direction):
    """
    determines if the enemy is finished walking its path and determines new direction
    Args:
    count --> (int) keeps count the total number of steps the enemy is in its path
    direction --> (str) the direction that the enemy is walking
    Return: (str) direction
    """
    if count == 0:
        direction_generation = random.randrange(0, 6)
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


def animate(folder, animation_rate, current_iteration, frame, animation_frame):
    """
    Animates different aspects of the game
    Args:
    folder --> (str) folder with the files needed for the animation
    animation_rate --> (int) number of frames needed to change the photo
    current_iteration --> (int) --> the current photo being accessed
    frame --> (int) the number of the current frame in the loop
    return: (touple) --> animation_frame (str), current_iteration (int), and frame (int)
    """
    animation_list = os.listdir(folder)
    if frame % animation_rate == 0:
        current_iteration += 1
        if current_iteration == len(animation_list):
            current_iteration = 0
        #print(current_iteration)
    animation_frame = animation_list[current_iteration]
    frame += 1
    if frame == animation_rate * (len(animation_list) - 1):
        frame = 0
    #print(animation_frame)
    return (animation_frame, current_iteration, frame)

def currentIterationChecker(current_iteration, folder):
    """
    checks if the current iteration is more than the number of pictures within the animation folder
    args:
    current_iteration --> (int) --> the current photo being accessed
    folder --> (str) folder with the files needed for the animation
    return current_iteration
    """
    if current_iteration > (len(os.listdir(folder)) - 1):
        current_iteration = 0
    return current_iteration

def spawnEnemy(filename, boundaries, enemy_number):
    """
    Takes the wave values from a file a saves them into variables
    Args:
    filename --> (str) the name of the text file with the wave information
    boundaries --> (touple) pixel limitations for the enemy movement
    enemy_number --> (int) the enemy's place in the wave lineup
    Return: (obj) --> the enemy object
    """
    with open(filename, 'r') as file:
        wave_information = file.readlines()

    type_line = (enemy_number * 6) + 1
    coordinateX_line = (enemy_number * 6) + 2
    coordinateY_line = (enemy_number * 6) + 3
    health_line = (enemy_number * 6) + 4
    png_line = (enemy_number * 6) + 5

    type = wave_information[type_line].rstrip("\n").split(' : ')
    coordinateX = wave_information[coordinateX_line].rstrip("\n").split(' : ')
    coordinateY = wave_information[coordinateY_line].rstrip("\n").split(' : ')
    health = wave_information[health_line].rstrip("\n").split(' : ')
    png = wave_information[png_line].rstrip("\n").split(' : ')

    enemy = bin.enemy.Enemy(type[1], int(coordinateX[1]), int(coordinateY[1]), int(health[1]), png[1], boundaries)
    return enemy
