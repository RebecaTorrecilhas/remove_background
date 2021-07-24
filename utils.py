import cv2
import numpy as np

def subtract_background(image, background, treshold):
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    background_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)
    mask = cv2.absdiff(image_gray, background_gray) #Diferença em módulo
    mask[mask <= treshold] = 0
    mask[mask > treshold] = 255
    result = cv2.bitwise_and(image, image, mask=mask.astype(np.uint8))

    return result, mask

def frame_adder_up_to(n):
    frames = []

    def add_frame(frame):
        if len(frames) < n:
            frames.append(frame)
        return frames

    return add_frame
