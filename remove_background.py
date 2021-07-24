import argparse
import cv2
import numpy as np

from background_models import factory as background_model_factory
from utils import frame_adder_up_to, subtract_background

parser = argparse.ArgumentParser(description='Background subtraction tool')
parser.add_argument('--model', type=str, help='the background model (default: fixed)',
                    choices=['fixed', 'mean', 'median'], default='fixed')
parser.add_argument('--frames', type=int,
                    help='the number of frames to be considered in obtaining the background model (default: 20)', default=20)
parser.add_argument('--treshold', type=int,
                    help='the mask treshold (default: 20)', default=20)
parser.add_argument('input', metavar='FILE', type=str, help='the input file')

args = parser.parse_args()

treshold = args.treshold
get_background_model = background_model_factory(args.model) #Pega o modelo

add_frame = frame_adder_up_to(args.frames) 

capture = cv2.VideoCapture(args.input)

frames_per_second = capture.get(cv2.CAP_PROP_FPS)
milliseconds_per_frame = int(1000 / frames_per_second)

if not capture.isOpened():
    print(f'Ouve um erro ao abrir o arquivo {args.input}')
    exit(1)

while capture.isOpened():
    ret, frame = capture.read()

    if not ret:
        break

    frames = add_frame(frame) #Adiciona o frame atual

    background = get_background_model(frames) #Obtem o modelo do background

    result, mask = subtract_background(frame, background, treshold) #Recebe duas imgs para comparar

    cv2.imshow('Background', background)
    cv2.imshow('Frame', frame)
    cv2.imshow('Mask', mask)
    cv2.imshow('Result', result)

    key = cv2.waitKey(milliseconds_per_frame)

    if key & 0xff == ord('q'):
        break

cv2.waitKey(0)

capture.release()
cv2.destroyAllWindows()
