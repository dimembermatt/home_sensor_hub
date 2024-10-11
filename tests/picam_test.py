from picamzero import Camera
from time import sleep

cam = Camera()
cam.still_size = (640, 480)
cam.take_photo('./image.jpg')
