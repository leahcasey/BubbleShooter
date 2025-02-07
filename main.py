from bubble import *
from paddle import *
from bullet import *
import pygame
# initialising the pygame library
pygame.init()

# pygame window set up
DISPLAY_WIDTH = 500
DISPLAY_HEIGHT = 500
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT) 
display = pygame.display.set_mode(DISPLAY_SIZE)

# this boolean is true while the game is running, the game stops when this is set to false
run_game=True

# set up for the bubble
circle_x=250
circle_y=25
circle_radius=25
circle_coords=[circle_x,circle_y]
circle_color=[255,255,255]

clock=pygame.time.Clock()

# this is the background colour of the pygamne window
bg_color=[0,0,0]

# set up for the line which draws across the middle of the pygame window
line_x1=0
line_y1=DISPLAY_HEIGHT//2
line_x2=DISPLAY_WIDTH
line_y2=DISPLAY_HEIGHT//2
line_start=[line_x1,line_y1]
line_end=[line_x2,line_y2]
line_color=[136,172,250]

# set up for the paddle
rect_width=100
rect_height=20
half_rect_width=rect_width//2
# this places the paddle in the middle of the screen
rect_x=DISPLAY_WIDTH//2-half_rect_width
rect_y=DISPLAY_HEIGHT-rect_height
rect_coordinates=[rect_x,rect_y,rect_width,rect_height]
rect_colour=[200,130,250]

# bullet set up
bullet_width=20
half_bullet_width=bullet_width//2
bullet_height=20
bullet_x=rect_x
# makes the y of the bullet relative to the paddle
bullet_y=rect_y-bullet_height
bullet_colour=[255,255,255]
bullet_speed = 5

# instance of the bubble
bubble_1=Bubble(circle_x,circle_y,circle_radius,circle_color,2,2) 

# instance of the paddle
padd=Paddle(rect_x,rect_y,rect_width,rect_height,rect_colour,7) 
# this prints the string representation of the paddle to the screen
print(padd)

# instance of the bullet
bullet=Bullet(bullet_x,bullet_y,bullet_width,bullet_height,bullet_colour,bullet_speed)

def collision_check(bubble: bubble_1, bullett: bullet, hor_bound: DISPLAY_WIDTH, vert_bound: DISPLAY_HEIGHT//2):
    '''this function checks if the bullet has collided with the bubble'''
    #  variable names explain what these points are
    endofbubble= bubble.get_bubbley() + bubble.get_bubblesize()
    topofbubble = bubble.get_bubbley() - bubble.get_bubblesize()

    endofbullet = bullett.get_bullety() + bullett.get_bulletheight()
    sideofbullet = bullett.get_bulletx() + bullett.get_bulletwidth()

    leftofbubble = bubble.get_bubblex() - bubble.get_bubblesize()
    rightofbubble = bubble.get_bubblex() + bubble.get_bubblesize()
    # this if statement checks if they collided using maths to see if any of their sides have touched/passed each other
    if endofbubble > bullett.get_bullety() and topofbubble < endofbullet and sideofbullet > leftofbubble and bullett.get_bulletx() < rightofbubble:
        
        # this function resets the bullet
        bullet.bubble_collision(bullet_y)
        # this function randomly changes the size of the bubble after it has been hit
        bubble_1.change_size(5, 100)
        # this relocates the bubble randomly in the upper half of the screen
        bubble_1.relocate(hor_bound, vert_bound)
        # this increases the speed of the bullet by 1 each time it is called, speed does not go above 15
        bullet.change_speed(5, 15)

# this booleans are true when the left or right arrows are pressed, and it moves the paddle on the screen
move_left=False
move_right=False

# when the game is running
while run_game:
    display.fill(bg_color)

    # this draws the line in the middle of the screen
    pygame.draw.line(display,line_color,line_start,line_end,3)
    # the bubble is drawn on the screen
    bubble_1.draw(display)
    # and it is always moving while the game is running

    verti_bound = line_y1-bubble_1.get_bubblesize()
    hoz_bound = DISPLAY_WIDTH-bubble_1.get_bubblesize()
    # had to use the getter for the bubbles radius for this function so that the updated 
    # radius value is used instead of the origional value
    bubble_1.move(verti_bound, hoz_bound,bubble_1.get_bubblesize())
    # this draws the paddle on the screen
    padd.draw(display)
    # this draws the paddle on the screen
    bullet.draw(display)

    # when the left arrow key is pressed, this is true
    if move_left==True:
        # and it moves the paddle left (the bullet always moves with the paddle)
        padd.move_left()
        
    # this is true when the right arrow key is pressed
    if move_right==True:
        # the move right function takes a parameter called bounds
        # which ensures the paddle doesn't move off screen
        padd.move_right(DISPLAY_WIDTH)
    
    # this gets the coordinates of the paddle and stores them in a variable
    info=padd.get_coordinates()
    # to ensure the bullet moves with the paddle, only the x coordinate needs to be moved and to ensure it stays in the middle 
    # of the paddle and isn't hardcoded, it moved to the paddle's x coordinate plus half the paddles width, minus half the bullets width
    # this function also moves the bullet if it has been shot/triggered, y value is changed within the function
    bullet.move([info[0]+half_rect_width-half_bullet_width,bullet_y]) #object interaction between bullet and paddle
    # this function checks if the bullet has collided with the top wall of the display screen, and if it has,
    # it is reset to the origional bullet y coordinate
    bullet.wall_collision(bullet_y)

    collision_check(bubble_1, bullet, DISPLAY_WIDTH, DISPLAY_HEIGHT//2)
# this for loop checks for pygamne events and performs actions based on 
# certain events (event driven programming used)
    for event in pygame.event.get():
        # if the users x's out of the pygame window
        if event.type==pygame.QUIT:
            # then the game ends/quits
            run_game=False
        # if a key is pressed down
        if event.type==pygame.KEYDOWN:
            # if the left arrow key is pressed
            if event.key==pygame.K_LEFT:
                # it moves the paddle to the left (and the bullet moves when the paddle does(objects interacting))
                move_left=True
            if event.key==pygame.K_RIGHT:
                # moves the paddle to the left (these are represented by booleans so that the paddle
                # keeps moving so long as the button is held down)
                move_right=True
            # if the space bar is pressed
            if event.key==pygame.K_SPACE:
                # this triggers the bullet
                bullet.set_triggered(True)
                
        if event.type==pygame.KEYUP:
            # once these keys are no longer being held down
            if event.key==pygame.K_LEFT:
                # it stops moving the paddle left
                move_left=False
            if event.key==pygame.K_RIGHT:
                # and stops moving the paddle right
                move_right=False

    clock.tick(60)
    # this updates the pygame display window
    pygame.display.update()
pygame.quit()
quit()