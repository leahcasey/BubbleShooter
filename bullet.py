import pygame

class Bullet:

    def __init__(self, x, y, width, height, color, speed):
        '''this is the constructer which sets up the bullet'''
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height]
        # i chose to make these variables private instance variables so that all variables which contain 
        # details about the bullet are the same type and therefore can be accessed the same way 
        # (ensures consistency,reduces confusion) and so that these variables can be changed in new instances
        self.__color = color
        self.__speed_y = speed
        self.__is_triggered = False
    
    def __str__(self):
        '''this string representation prints details about the bullet to the terminal when the game is run'''
        intro = "In this instance of bullet, the starting coordinates are %s, %s, and the rgb of it is %s.\nThe bullet's height is %s and its width is %s" %(self.__x,self.__y,self.__color,self.__height,self.__width)
        return intro

    def draw(self, display):
        '''this function draws the bullet in the pygame display window when it is called'''
        pygame.draw.rect(display, self.__color, self.__coordinates)
    
    def change_speed(self, lower_limit, upper_limit):
        '''this method increases the speed of the bullet by 1 each time the bullet and bubble collide'''
        if self.__speed_y >= lower_limit and self.__speed_y <= upper_limit:
            # increases the speed if it is between this range still
            self.__speed_y = self.__speed_y + 1
        else:
            # if bullet has reached max speed it stays the same
            self.__speed_y = self.__speed_y
            

    def move(self, pos):
        '''this method moves the bullet, and the bullet always moves with the paddle
        and it also moves/shoots the bullet when the space bar is pressed by incrementing its y coordinate'''
        
        if self.__is_triggered==True:
            self.__y = self.__y - self.__speed_y

        else:
            # the pos parameter contains the coordinates in which the bullet needs to move
            # and then changes the x and y based on that info
            self.__x = pos[0]
            self.__y = pos[1]
            # and then resets the coordinates
        self.__coordinates = [self.__x, self.__y, self.__width, self.__height]

    def set_triggered(self, triggered:bool):
        '''this function is called when the space bar has been pressed, meaning the bullet has been triggered'''
        if triggered==True:
            # if the function has been called with the parameter 'True' passed in 
            self.__is_triggered=True #then the instance variable is changed to True
            
        if triggered==False:
            # this changes it back to False after the function has been called with 'False' passed in
            self.__is_triggered=False

    def wall_collision(self,reset):
        '''this function checks if the bullet has moved past the top of the screen, so that when it has moved offscreen
        after being shot, it calls set_triggered and sets the instance variable back to False'''
        if self.__y<0:
            self.set_triggered(False)
            # the reset parameter is used to pass in the origional y value of the bullet before being shot
            # and resets its y position
            self.__y=reset
    
    def bubble_collision(self,reset):
        '''this function is only called if the bullet and the bubble have collided'''
        # it stops the bullet from moving
        self.set_triggered(False)
        # and resets its y value so that its back with the paddle
        self.__y=reset

    def get_bulletsize(self):
        '''this method returns the bullets size, which is its width and height'''
        return self.__width, self.__height
    
    def get_bulletwidth(self):
        '''this method returns the bullets size, which is its width and height'''
        return self.__width
    
    def get_bulletheight(self):
        return self.__height

    def get_coordinates(self):
        '''this method returns the bullets coordinates'''
        return self.__coordinates

    def get_bulletx(self):
        '''this method returns the x coordinate of the bullet when called'''
        return self.__x

    def get_bullety(self):
        '''this method returns the y coordinate of the bullet when called'''
        return self.__y
