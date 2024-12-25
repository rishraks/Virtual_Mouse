import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math



cap = cv2.VideoCapture(0)

w_screen, h_screen = pyautogui.size()
# print(w_screen,h_screen)

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    static_image_mode=False,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    else:
        frame = cv2.flip(frame,1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(frame_rgb)

        if results.multi_hand_landmarks:
            for handlms in results.multi_hand_landmarks:
                h,w,c = frame.shape
                frame = cv2.resize(frame,(640,480))
                index_tip = handlms.landmark[8]
                thumb_tip = handlms.landmark[4]
                
                index_pos = int(index_tip.x*w),int(index_tip.y*h)
                thumb_pos = int(thumb_tip.x*w),int(thumb_tip.y*h)
                
                cv2.circle(frame, index_pos,8,(0,255,255),-1)
                cv2.circle(frame, thumb_pos,8,(0,255,255),-1)
                # cv2.line(frame, index_pos,thumb_pos,(255,0,255),2)
                
                
                distance = int(math.hypot(index_pos[0]-thumb_pos[0],index_pos[1]-thumb_pos[1]))
                
                cv2.putText(frame,str(distance),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)
                normalize_dist = int(np.interp(distance,[16,145],[0,100]))
                cv2.putText(frame,str(normalize_dist),(10,60),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),1)

                x1 = np.interp(index_pos[0],(0,640),(0,w_screen))
                y1 = np.interp(index_pos[1],(0,480),(0,h_screen))
                
                pyautogui.moveTo((x1,y1))
                
                
        cv2.imshow("Virtual Mouse", frame)
        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
