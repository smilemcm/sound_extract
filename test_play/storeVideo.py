import numpy as np
import cv2



shotsPath = './out/%d.avi'
cap = cv2.VideoCapture("Lecture3")
fps = int(cap.get(cv2.CAP_PROP_FPS))

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = int(cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'))  # XVID codecs

segRange = [(0, fps*60), (fps*60+1, fps*60*2), (fps*60*2+1, fps*60*3)]  # a list of starting/ending frame indices pairs


for idx, (begFidx, endFidx) in enumerate(segRange):
    writer = cv2.VideoWriter(shotsPath%idx, fourcc, fps, size)
    cap.set(cv2.CAP_PROP_POS_FRAMES, begFidx)
    ret = True  # has frame returned
    while (cap.isOpened() and ret and writer.isOpened()):
        ret, frame = cap.read()
        frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES) - 1
        if frame_number < endFidx:
            writer.write(frame)
        else:
            break
    writer.release()

