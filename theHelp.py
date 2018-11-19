import threading as thread
import cv2
import base64
import Queue
import numpy as np
import os

global finished1
global finished2

def extractFrames(fileName, outputBuffer):
    global finished1; global finished2
    # Initialize frame count
    count = 0

    # open video file
    vidcap = cv2.VideoCapture(fileName)

    # read first image
    success,image = vidcap.read()

    print("Reading frame {} {} ".format(count, success))
    while success:
        # get a jpg encoded frame
        success, jpgImage = cv2.imencode('.jpg', image)

        #encode the frame as base 64 to make debugging easier
        jpgAsText = base64.b64encode(jpgImage)

        # add the frame to the buffer
        outputBuffer.put(jpgAsText)

        success,image = vidcap.read()
        print('Reading frame {} {}'.format(count, success))
        count += 1

    print("Frame extraction complete")
    finished1 = True


def grayScale(inputBuffer, outputBuffer):
    # initialize frame count
    global finished1; global finished2
    while not finished1:
        count = 0

        # go through each frame in the buffer until the buffer is empty
        while not inputBuffer.empty():
            # get the next frame
            frameAsText = inputBuffer.get()

            # decode the frame
            jpgRawImage = base64.b64decode(frameAsText)

            # convert the raw frame to a numpy array
            jpgImage = np.asarray(bytearray(jpgRawImage), dtype=np.uint8)

            # get a jpg encoded frame
            img = cv2.imdecode(jpgImage ,cv2.IMREAD_UNCHANGED)

            grayscaleFrame = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            success, jpgGrayImage = cv2.imencode('.jpg', grayscaleFrame)

            #encode the frame as base 64 to make debugging easier
            jpgGrayAsText = base64.b64encode(jpgGrayImage)

            print("Converting frame {}".format(count))

            # add the frame back to the buffer
            outputBuffer.put(jpgGrayAsText)

            count += 1
    print("Frame Grayscale Conversion Complete")
    finished2 = True

def displayFrames(inputBuffer):
    global finished1; global finished2
    while not finished2:
    # initialize frame count
        count = 0

        # go through each frame in the buffer until the buffer is empty
        while not inputBuffer.empty():
            # get the next frame
            frameAsText = inputBuffer.get()

            # decode the frame
            jpgRawImage = base64.b64decode(frameAsText)

            # convert the raw frame to a numpy array
            jpgImage = np.asarray(bytearray(jpgRawImage), dtype=np.uint8)

            # get a jpg encoded frame
            img = cv2.imdecode( jpgImage ,cv2.IMREAD_UNCHANGED)

            print("Displaying frame {}".format(count))

            # display the image in a window called "video" and wait 42ms
            # before displaying the next frame
            cv2.imshow("Video", img)
            if cv2.waitKey(42) and 0xFF == ord("q"):
                break

            count += 1
    print("Finished Displaying All Frames")
    # cleanup the windows
    cv2.destroyAllWindows()
