import cv2
import numpy as np
import operator

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    proc = cv2.GaussianBlur(gray.copy(), (9,9), 0)
    ## use adaptive threshold using 11 nearest neighbour pixels
    proc = cv2.adaptiveThreshold(proc, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

    proc = cv2.bitwise_not(proc,proc)
    kernel = np.array([[0.,1.,0.],[1.,1.,1.],[0.,1.,0.]], np.uint8)
    ## dilate the image to increase the size of gridline
    proc = cv2.dilate(proc, kernel)

    contours, h = cv2.findContours(gray.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    polygon = contours[0]

    bottom_right, _ = max(enumerate([pt[0][0]+pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
    top_left, _ = min(enumerate([pt[0][0]+pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
    bottom_left, _ = min(enumerate([pt[0][0]-pt[0][1] for pt in polygon]), key=operator.itemgetter(1))
    top_right, _ = max(enumerate([pt[0][0]-pt[0][1] for pt in polygon]), key=operator.itemgetter(1))

    #print([polygon[top_left][0], polygon[top_right][0], polygon[bottom_right][0], polygon[bottom_left][0]])
    print(tuple(polygon[top_left][0]))
    cv2.circle(proc, tuple(polygon[top_left][0]), radius=10, color=(0,0,255), thickness=-1)
    #proc[polygon[top_left][0][0],polygon[top_left][0][1]]=[0,0,255]
    #proc[polygon[top_right][0]]=[0,0,255]
    #proc[polygon[bottom_left][0]]=[0,0,255]
    #proc[polygon[bottom_right][0]]=[0,0,255]
    #print(proc.shape)

    cv2.imshow('frame',proc)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
