# BubbleShooter
This interactive Pygame-based game integrates the Circuit Playground Express accelerometer to control a paddle, but also supports keyboard controls for accessibility. The goal is to hit a moving bubble with a bullet while preventing it from crossing a boundary line.

Core Gameplay:
The paddle moves based on tilting the board (x/y acceleration) or using the arrow keys if the Circuit Playground is disconnected.
A bubble moves diagonally, bouncing off walls and relocating when reaching the boundary line.
Players can fire a bullet using a button press on the Circuit Playground or by pressing space bar. Only one bullet can be on screen at a time.

NeoPixel lights provide tilt-based visual feedback when using the Circuit Playground.

Features:
Dynamic Bullet & Bubble Behavior: On collision, the bullet changes speed, and the bubble resizes dynamically.
Advanced Light Feedback: A new visual effect responds to paddle movement for improved feedback.
The game remains fully playable with keyboard controls when the Circuit Playground is disconnected, ensuring accessibility and flexibility in gameplay.

Main.py still runs if Adafruit Circuit Playground is not connected. Files to be run in Circuit Playground include code.py and sensordisplay.py
