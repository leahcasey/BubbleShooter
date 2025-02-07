import pygame

class Paddle:

    def __init__(self, x, y, width, height, colour, speed):
        '''this is the constructer which sets up the paddle'''
        self.__x = x
        self.__y = y
        self.__colour = colour
        self.__speed=speed
        # i chose to make these variables private instance variables so that all variables which contain 
        # details about the paddle are the same type and therefore can be accessed the same way 
        # (ensures consistency,reduces confusion) and so that these variables can be changed in new instances
        self.__width = width
        self.__height = height
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height]

    def __str__(self):
        '''this string representation prints details about the paddle to the terminal when the game is run'''
        intro = "In this instance of paddle, the starting coordinates are %s, %s, and the rgb of it is %s.\nThe paddle's height is %s and its width is %s" %(self.__x,self.__y,self.__colour,self.__height,self.__width)
        return intro

    def draw(self, display):
        '''this function draws the paddle to the pygame display window when called'''
        pygame.draw.rect(display, self.__colour, self.__coordinates)
    
    def move_left(self):
        '''this method moves the paddle to the left side of the screen by decreasing the x value (by however much the speed is)
        and the method is called when the left arrow is pressed on the keyboard'''
        self.__x=self.__x-self.__speed
        # this ensures that the paddle stays within the bounds of the pygame display window
        # by ensuring the x doesn't become less than 0
        if self.__x<0:
            self.__x=0
        # this updates the coordinates each time the method is run
        self.__coordinates=[self.__x,self.__y,self.__width,self.__height]
    
    def move_right(self, bounds):
        '''this method moves the paddle to the right side of the screen by increasing the x value
        and the method is called when the right arrow is pressed on the keyboard'''
        self.__x=self.__x+self.__speed
        # this ensures the paddle doesn't go past the right wall of the screen by using the parameter called bounds
        if self.__x>bounds-self.__width:
            self.__x=bounds-self.__width
        self.__coordinates=[self.__x,self.__y,self.__width,self.__height]
    
    def get_colour(self):
        '''this methods returns the paddle colour'''
        return self.__colour

    def get_height(self):
        '''this methods returns the paddle height'''
        return self.__height

    def get_width(self):
        '''this methods returns the paddle width'''
        return self.__width

    def get_paddlex(self):
        '''this methods returns the paddle's x coordinate'''
        return self.__x

    def get_paddley(self):
        '''this methods returns the paddle's y coordinate'''
        return self.__y

    def get_paddlesize(self):
        '''this methods returns the paddle's size (its width and height)'''
        return self.__width,self.__height

    def get_coordinates(self):
        '''this methods returns the paddle's full coordinates'''
        return self.__coordinates