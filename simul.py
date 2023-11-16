import cv2
import time


CAM_ID = 0

cap =cv2.VideoCapture(CAM_ID)
cv2.namedWindow('Face')
face_cascade = cv2.CascadeClassifier()

face_cascade.load(r'/Users/hb/miniforge3/envs/lab/lib/python3.9/site-packages/cv2/data/haarcascade_frontalface_default.xml')

drone_x = 440
drone_y = 160
drone_xw = 840
drone_yh = 560


while(True):
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    grayframe = cv2.equalizeHist(grayframe)
    faces = face_cascade.detectMultiScale(grayframe,1.1, 3, 0, (30,30))
    

    for (x,y,w,h) in faces:
        
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3, 4, 0)
    
    cv2.rectangle(frame,(drone_x, drone_y),(drone_xw,drone_yh),(128,128,0),3, 4, 0)

    
    cv2.imshow('Face', frame)
    

    if faces is ():
        print("0")
    else:
        print(x," ", y, " ", x+w ," ", y+h, "      size: " ,frame.shape)
    
    if cv2.waitKey(10) >= 0:
        break;


    if(drone_x > x) :
        drone_x = drone_x - 5
        drone_xw = drone_xw - 5

    elif(drone_xw < x+w) :
        drone_x = drone_x + 5
        drone_xw = drone_xw + 5

    elif(drone_y > y) :
        drone_y = drone_y - 5
        drone_yh = drone_yh - 5

    elif(drone_yh < y+h) :
        drone_y = drone_y + 5
        drone_yh = drone_yh + 5

        

    time.sleep(0.1)

cap.release()
cv2.destroyWindow('Face')