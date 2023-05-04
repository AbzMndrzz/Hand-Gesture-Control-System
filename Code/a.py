import cv2
import numpy as np
import math
import pyautogui
import mediapipe as mp

def volume():

    mp_drawing = mp.solutions.drawing_utils
    mp_hands = mp.solutions.hands
    
    cap = cv2.VideoCapture(0)
    
    # Initialize hand position and EMA parameters
    prev_hand_y = 0
    ema_alpha = 0.5  # Smoothing factor for EMA
    
    with mp_hands.Hands(
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5) as hands:
    
        while cap.isOpened():
            success, image = cap.read()
            if not success:
                break
            
            image = cv2.flip(image, 1)
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False
            results = hands.process(image)
            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
            if results.multi_hand_landmarks:
                hand_landmarks = results.multi_hand_landmarks[0]
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)
    
                # Check if index and thumb fingers are touching
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                distance = math.sqrt(
                    (thumb_tip.x - index_tip.x) ** 2 + (thumb_tip.y - index_tip.y) ** 2 + (thumb_tip.z - index_tip.z) ** 2)
    
                # Get the y-coordinate of the hand
                hand_y = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_MCP].y
    
                # Smooth hand movement using EMA
                smooth_hand_y = (1 - ema_alpha) * \
                    prev_hand_y + ema_alpha * hand_y
    
                # Adjust volume based on smoothed hand movement and finger distance
                if distance < 0.05 and smooth_hand_y < prev_hand_y:
                    pyautogui.press('volumeup')
                elif distance < 0.05 and smooth_hand_y > prev_hand_y:
                    pyautogui.press('volumedown')
    
                # Update previous hand y-coordinate
                prev_hand_y = smooth_hand_y
    
            cv2.imshow('MediaPipe Hands', image)
            if cv2.waitKey(5) & 0xFF == 27:
                break
            
    cap.release()
    cv2.destroyAllWindows()
    