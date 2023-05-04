import cv2
import time
import numpy as np
import hant as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
import screen_brightness_control as scb
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import autopy
################################

def Start():
    
    wCam, hCam = 640, 480

    frameR = 100 # Frame Reduction
    smoothening = 7
    #########################
        
    plocX, plocY = 0, 0
    clocX, clocY = 0, 0
    cap=cv2.VideoCapture(0)
    cap.set(3, wCam)
    cap.set(4, hCam)
    pTime=0
    wScr, hScr = autopy.screen.size()

    detector = htm.handDetector(detectionCon= 0.7)


    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    #volume.GetMute()
    #volume.GetMasterVolumeLevel()
    volRange = volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-20.0, None)
    minVol = volRange[0]
    maxVol = volRange[1]
    vol = 0
    volBar = 400
    volPer = 0
    area=0
    colorVol=(255,0,0)
    val = 0
    flag=0
    while True:
        sucess, img = cap.read()
        img = detector.findHands(img)
        lmList, bbox = detector.findPosition(img, draw= True)
        if len(lmList) != 0:
            x1, y1 = lmList[8][1:]
            x2, y2 = lmList[12][1:]
            # Filter based on size
            area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
            #print(area)
            
            if 250 < area < 1000:
        
                fingers = detector.fingersUp(img)
                print(fingers)
                # print(fingers)
                # If pinky is down set volume
                if not fingers[2] and not fingers[3]:
                    flag=0
                    length, img, lineInfo = detector.findDistance(4, 8, img)
                    volBar = np.interp(length, [50, 300], [400, 150])
                    volPer = np.interp(length, [50, 300], [0, 100])
                    smoothness = 10
                    volPer = smoothness * round(volPer / smoothness)
                    volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                    colorVol = (0, 255, 0)
                    # Drawings
                    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
                    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
                    cv2.putText(img, f'{int(volPer)} %', (40, 450), cv2.FONT_HERSHEY_COMPLEX,
                                1, (255, 0, 0), 3)
                    
    
                if  not fingers[3] and not fingers[4] :
                    flag=1
                    length,img,lineInfo = detector.findDistance(lmList[4][0],lmList[8][0],img)          
                    blevel = np.interp(length,[25,145],[0,100])
                    val = np.interp(length, [0, 100],[400,150])
                    blevel = int(blevel)
                    scb.set_brightness(blevel)
                    cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED) 
                    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
                    cv2.rectangle(img, (50, int(val)), (85, 400), (0, 0, 255), -1)
                    cv2.putText(img,str(blevel)+'%',(20,430),cv2.FONT_HERSHEY_COMPLEX,1,
                            (255,0,0),3)
                if   fingers[1] and fingers[2]:
                    flag=2
                    _,img,_ = detector.findDistance(lmList[4][0],lmList[8][0],img)
                    fingers = detector.fingersUp(img)
                    # print(fingers)
                    cv2.rectangle(img, (frameR, frameR), (wCam - frameR, hCam- frameR),(255, 0, 255), 2)
                    if fingers[1] == 1 and fingers[2] == 1:
                        # 5. Convert Coordinates
                        x3 = np.interp(x1, (frameR, wCam - frameR), (0, wScr))
                        y3 = np.interp(y1, (frameR, hCam-frameR-100), (0, hScr))
                        # 6. Smoothen Values
                        clocX = plocX + (x3 - plocX) / smoothening
                        clocY = plocY + (y3 - plocY) / smoothening
                        # 7. Move Mouse
                        autopy.mouse.move(wScr - clocX, clocY)
                        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
                        plocX, plocY = clocX, clocY
                        length, img, lineInfo = detector.findDistance(8, 12, img)
                        #print(length)
                        # 10. Click mouse if distance short
                        if length < 40:
                            cv2.circle(img, (lineInfo[4], lineInfo[5]),
                            15, (0, 255, 0), cv2.FILLED)
                            autopy.mouse.click()
        if flag==0:
            cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
            cv2.putText(img, f'Vol Set: {int(cVol)}', (400, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, colorVol, 3)
        if flag==1:
            Blist = scb.get_brightness()
            cVol= Blist
            colorVol = (0, 255, 0)
            cv2.putText(img, f'Brightness Set: {int(cVol)}', (200, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, colorVol, 3)      
        
        # Frame rate
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (40, 50), cv2.FONT_HERSHEY_COMPLEX,
                    1, (255, 0, 0), 3)
    
        cv2.imshow("Img", img)
        k = cv2.waitKey(1)
        if k == 27:
            break
    cv2.destroyAllWindows()
    cap.release()