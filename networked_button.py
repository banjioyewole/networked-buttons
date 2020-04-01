from sense_hat import SenseHat
from time import sleep
import requests
sense = SenseHat()

e = (0, 0, 0)
w = (255, 255, 255)

sense.clear()

base_url = "http://localhost/api/"

pressed_counter = 0
last_direction = ""

def preform_action(direction, press_durration):
    long_press = press_durration >= 2
    if len(last_direction) > 0:
        pass
    else:
        return
    api_path = direction
    api_path = ("double-" if long_press else "") + api_path
    r = requests.get(base_url+api_path, params={})


while True:

  for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      # Check which direction
      last_direction = event.direction
      if event.direction == "up":
        sense.show_letter("U")      # Up arrow
      elif event.direction == "down":
        sense.show_letter("D")      # Down arrow
      elif event.direction == "left":
        sense.show_letter("L")      # Left arrow
      elif event.direction == "right":
        sense.show_letter("R")      # Right arrow
      elif event.direction == "middle":
        sense.show_letter("M")      # Enter key
    else:
        preform_action(last_direction, pressed_counter)
        pressed_counter = 0
      # Wait a while and then clear the screen
    sleep(0.5)
    sense.clear()
