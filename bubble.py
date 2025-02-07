import pygame
import random

class Bubble:

    def __init__(self, x, y, radius, colour, speed_y, speed_x):
        '''this is the constructer which sets up the bubble'''
        self.__x = x
        self.__y = y
        # i chose to make these variables private instance variables so that all variables which contain 
        # details about the bubble are the same type and therefore can be accessed the same way 
        # (ensures consistency,reduces confusion) and so that these variables can be changed in new instances
        self.__radius = radius
        self.__coordinates = [self.__x, self.__y]
        self.__speed_y = speed_y
        self.__speed_x = speed_x
        self.__colour = colour

    def __str__(self):
        '''this string representation prints details about the bubble to the terminal when the game is run'''
        intro = "In this instance of paddle, the starting coordinates are %s, %s, and the rgb of it is %s.\nThe bubbles radius is %s" %(self.__x,self.__y,self.__colour,self.__radius)
        return intro

    def draw(self, display):
        '''this function draws the bubble in the pygame display window when it is called'''
        pygame.draw.circle(display, self.__colour, self.__coordinates, self.__radius)
        
    def relocate(self, horizontal_bound, vertical_bound):
        '''this method is called to relocate the bubble to a random location once it has been hit by the bullet'''
        # the bottom of the area it can relocate in
        bottom = vertical_bound - self.__radius
        # the side bound that the bubble must relocate within
        side = horizontal_bound - self.__radius
        # randomly relocate x and y axis between selected bounds
        self.__y = random.randint(self.__radius, bottom)
        # random.randint(self.__radius, bottom)
        self.__x = random.randint(self.__radius, side)
        # this changes the direction the ball is moving when it relocates
        self.__speed_x=self.__speed_x*-1
        # resetting the coordinates
        self.__coordinates = [self.__x, self.__y]

    def change_size(self, lower_limit:int, upper_limit:int):
        '''this function randomly changes the size of the bubble radius to a random integer between 5 (which is really small)
        and 100 (which bearly fits the screen)'''
        self.__radius = random.randint(lower_limit, upper_limit)
    
    def move(self, vertical_bound, horizontal_bound, bubble_radius):
        '''this function moves the bubble coninuously on the screen, it is always moving downward and either left or right'''
        # this increases the y value of the bubble, moving it lower on the screen
        self.__y=self.__y+self.__speed_y
        # this increases the x value of the bubble, initially moving it right on the screen
        self.__x=self.__x+self.__speed_x
        
        # this if statement ensures that if the bubble touches off either the left or the right wall
        # that it 'bounces' off the wall, by changing the direction it moves
        if self.__x<self.__radius or self.__x>horizontal_bound:
            # it does this by multiplying the x speed by -1, so the x value will be minusing the speed instead of adding
            self.__speed_x=self.__speed_x*-1

        # if the bubble reaches the line (the vertical bound)
        if self.__y>=vertical_bound:
            # this relocates the bubble at a random coordinate along the x axis within the screen
            self.__x=random.randint(bubble_radius,horizontal_bound)
            # this relocates the y axis of the bubble at the top of the screen
            # it does this using the bubble radius so it doesn't restart partly off screen
            self.__y=bubble_radius
        
        self.__coordinates=[self.__x,self.__y]

    def get_bubblex(self):
        '''getter for the x value of the bubble'''
        return self.__x

    def get_bubbley(self):
        '''getter for the y value of the bubble'''
        return self.__y

    def get_bubblesize(self):
        '''getter for the radius of the bubble'''
        return self.__radius


