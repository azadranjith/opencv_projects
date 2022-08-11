import numpy as np
import cv2 as cv

def nothing(x):
    pass
cv.namedWindow('trackbar',flags=cv.WINDOW_NORMAL)

cv.createTrackbar('l_hue','trackbar',0,179,nothing)
cv.createTrackbar('l_sat','trackbar',0,255,nothing)
cv.createTrackbar('l_bri','trackbar',0,255,nothing)

cv.createTrackbar('h_hue','trackbar',0,179,nothing)
cv.createTrackbar('h_sat','trackbar',0,255,nothing)
cv.createTrackbar('h_bri','trackbar',0,255,nothing)

video = cv.VideoCapture(0)

while True:
    
    
    
    _,frame = video.read()

    hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    
    lh = cv.getTrackbarPos('l_hue','trackbar')
    ls = cv.getTrackbarPos('l_sat','trackbar')
    lb = cv.getTrackbarPos('l_bri','trackbar')
    hh = cv.getTrackbarPos('h_hue','trackbar')
    hs = cv.getTrackbarPos('h_sat','trackbar')
    hb = cv.getTrackbarPos('h_bri','trackbar')
    
    
    lb = np.array([lh,ls,lb])
    
    ub = np.array([hh,hs,hb])
    
    mask = cv.inRange(hsv,lb,ub)
    cv.imshow('frame',frame)
    cv.imshow('hsv',hsv)
    cv.imshow('mask',mask)
    
    if cv.waitKey(34) & 0xFF ==ord('q'):
        break
cv.destroyAllWindows()
