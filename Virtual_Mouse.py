import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import math


pyautogui.FAILSAFE = False
cap = cv2.VideoCapture(0)

w_screen, h_screen = pyautogui.size()
w_cam = 640
h_cam = 480

frame_red = 100

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

click_dist_min = 16
click_dist_max = 145

doubleClick_dist_min = 25
doubleClick_dist_max = 76

norm_min = 0
norm_max = 100


smooth_value = 10

clock_x, clock_y = 0,0
ploc_x,ploc_y = 0,0 


hands = mp_hands.Hands(
    max_num_hands=1,
    static_image_mode=False,
    min_detection_confidence=0.6,
    min_tracking_confidence=0.6,
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
                frame = cv2.resize(frame,(w_cam,h_cam))
                index_tip = handlms.landmark[8]
                thumb_tip = handlms.landmark[4]
                middle_tip = handlms.landmark[12]
                
                
                index_pos = int(index_tip.x*w),int(index_tip.y*h)
                thumb_pos = int(thumb_tip.x*w),int(thumb_tip.y*h)
                middle_pos = int(middle_tip.x*w),int(middle_tip.y*h)
                
                cv2.circle(frame, index_pos,8,(0,255,255),-1)
            
                
                click_distance = int(math.hypot(index_pos[0]-thumb_pos[0],index_pos[1]-thumb_pos[1]))
                
                normalize_click_dist = int(np.interp(click_distance,[click_dist_min,click_dist_max],[norm_min,norm_max]))

                doubleClick_distance = int(math.hypot(index_pos[0]-middle_pos[0],index_pos[1]-middle_pos[1]))
                
                normalize_doubleClick_dist = int(np.interp(doubleClick_distance,[doubleClick_dist_min,doubleClick_dist_max],[norm_min,norm_max]))

                
                
                x_screen = np.interp(index_pos[0],(frame_red,w_cam-frame_red),(0,w_screen))
                y_screen = np.interp(index_pos[1],(frame_red,h_cam-frame_red),(0,h_screen))
                
                clock_x = ploc_x + (x_screen-ploc_x)/smooth_value
                clock_y = ploc_y + (y_screen-ploc_y)/smooth_value
                
                pyautogui.moveTo((clock_x,clock_y))
                ploc_x,ploc_y = clock_x,clock_y
                
                
                
                if normalize_click_dist < 10:
                    cv2.circle(frame, index_pos,8,(0,0,255),-1)
                    cv2.circle(frame, thumb_pos,8,(0,0,255),-1)
                    pyautogui.click()
                
                if normalize_doubleClick_dist < 20:
                    cv2.circle(frame, middle_pos,8,(255,0,255),-1)
                    cv2.circle(frame,index_pos,8,(255,0,255),-1)
                    pyautogui.doubleClick()
                
                
        cv2.rectangle(frame,(frame_red,frame_red),(w_cam-frame_red,h_cam-frame_red),(0,0,255),2)         
        cv2.imshow("Virtual Mouse", frame)
        if cv2.waitKey(1) == ord("q"):
            break

cap.release()
cv2.destroyAllWindows()
