'''import cv2
import math
import mediapipe as mp

mp_drawing=mp.solutions.drawing_utils
mp_drawing_styles=mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
cam=cv2.VideoCapture(0)

with mp_hands.Hands(
    static_image_mode=False,model_complexity=0,max_num_hands=1, min_detection_confidence=0.5,
    min_tracking_confidence=0.5 ) as hands:

    while cam.isOpened():
        success, image=cam.read()
        if not success:
            print("failure to capture")
            continue

        image.flags.writeable=False
        image=cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        result=hands.process(image)


        image.flags.writeable=True
        image=cv2.cvtColor(image, cv2.COLOR_RGB2BGR)


        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:

                mp_drawing.draw_landmarks(image, hand_landmarks,
                  mp_hands.HAND_CONNECTIONS,
                  mp_drawing_styles.get_default_hand_landmarks_style(),
                  mp_drawing_styles.get_default_hand_connections_style())

        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
cam.release()

'''