import cv2 as cv
import numpy as np
import screen_brightness_control as scb
import hant as htm
import time
def brightness():

    wCam, hCam = 640, 480
    pTime=0   
    cap = cv.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    detector = htm.handDetector(detectionCon= 0.7)
    val = 0
    while True:
        success,img = cap.read()
        if not success:
                print('NOt ready')
                break
        img = detector.findHands(img)
        lm, bbox = detector.findPosition(img, draw= True)
        blevel=0
        
        if len(lm) != 0:
            # Filter based on size
            area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
                #print(area)  
            if 250 < area < 1000:
                length,img,info = detector.findDistance(lm[4][0],lm[8][0],img)
                    # print(lenght)
                blevel = np.interp(length,[50,200],[0,100])
                val = np.interp(length, [0, 100],[400,150])
                blevel = int(blevel)
                    # print(blevel)
                fingers = detector.fingersUp(img)
                    #print(fingers)
                if  not fingers[3] and not fingers[4]:
                    scb.set_brightness(blevel)
                    cv.circle(img, (info[4], info[5]), 15, (0, 255, 0), cv.FILLED)
        cv.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
        cv.rectangle(img, (50, int(val)), (85, 400), (0, 0, 255), -1)
        cv.putText(img,str(blevel)+'%',(20,430),cv.FONT_HERSHEY_COMPLEX,1,
                    (255,0,0),3)
        Blist = scb.get_brightness()
        cVol= Blist
        colorVol = (0, 255, 0)
        cv.putText(img, f'Brightness Set: {int(cVol)}', (200, 50), cv.FONT_HERSHEY_COMPLEX,
                        1, colorVol, 3)
            # Frame rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv.putText(img, f'FPS: {int(fps)}', (40, 50), cv.FONT_HERSHEY_COMPLEX,
                            1, (255, 0, 0), 3)
        cv.imshow('frame',img)
        k = cv.waitKey(1)
        if k == 27:
            break
    cv.destroyAllWindows()
    cap.release()
