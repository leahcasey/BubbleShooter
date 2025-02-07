from adafruit_circuitplayground import cp

class SensorLightDisplay:
    def __init__(self, brightness):
        self.acceleration_peak = 9.81
        self.__lights_off = [0, 0, 0]
        cp.pixels.brightness = brightness
        self.pixels_count = len(cp.pixels)
        cp.pixels.auto_write = False

    def advanced_control_feedback(self, acceleration_x):

        if acceleration_x < 9.81 and acceleration_x > -9.81:
            for pixel in range(self.pixels_count):
                if acceleration_x > 3:
                    # right side
                    last_pixel_location = int(acceleration_x*6/self.acceleration_peak)-1

                    if pixel <= last_pixel_location :
                        cp.pixels[pixel] = [35*last_pixel_location, 0, 200-(last_pixel_location*35)]

                elif acceleration_x < -3:
                    # left side
                    last_pixel_loc = int((acceleration_x * -6)/self.acceleration_peak)+4

                    if pixel <= last_pixel_loc and pixel >= 5:
                        if last_pixel_loc == 6 or last_pixel_loc == 8:
                            last_pixel_loc = last_pixel_loc-1
                        cp.pixels[4-last_pixel_loc] = [255, 0, 255]

                else:
                    cp.pixels[pixel] = self.__lights_off
                cp.pixels.show()