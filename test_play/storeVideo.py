import numpy as np
import cv2
import pytesseract


(major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')

shotsPath = './out/%d.avi'
cap = cv2.VideoCapture("goodmorning.mp4")
fps = int(cap.get(cv2.CAP_PROP_FPS))

size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
fourcc = int(cv2.VideoWriter_fourcc('X', 'V', 'I', 'D'))  # XVID codecs

segRange = [(0, fps*60), (fps*60+1, fps*60*2), (fps*60*2+1, fps*60*3)]  # a list of starting/ending frame indices pairs


ret, frame = cap.read()
prev_text = pytesseract.image_to_string(frame, lang='kor+eng')
frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)

while ret:
    writer = cv2.VideoWriter(shotsPath%(frame_number+1), fourcc, fps, size)
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number+1)

    print(prev_text)


    while (cap.isOpened() and ret and writer.isOpened()):
        ret, frame = cap.read()
        cv2.imshow('output', frame)

        if(cv2.waitKey(1) & 0xFF == ord('q')):
            break
        text = pytesseract.image_to_string(frame, lang='eng')

        frame_number = cap.get(cv2.CAP_PROP_POS_FRAMES)
        if text == prev_text:
            writer.write(frame)
        else:
            prev_text = text
            prev_frame_number = frame_number
            break

    writer.release()

cv2.destroyWindow()
