#!/usr/bin/env python3
import time
import picamera

class OV5647:
    def __init__(self, resolution=(640, 480), framerate=30):
        # Initialize the camera
        self.camera = picamera.PiCamera()
        self.camera.resolution = resolution
        self.camera.framerate = framerate

    def capture_image(self, filename):
        # Capture an image and save it to the specified filename
        self.camera.capture(filename)

# Test script
def main():
    ov5647 = OV5647()  # Initialize the OV5647 camera
    try:
        while True:
            filename = "image_{}.jpg".format(int(time.time()))
            ov5647.capture_image(filename)
            print("Image captured and saved as {}".format(filename))
            time.sleep(5)  # Capture an image every 5 seconds
    except KeyboardInterrupt:
        print("Exiting...")
        ov5647.camera.close()

if __name__ == "__main__":
    main()
