import cv2
import numpy as np
from fontTools.misc.cython import returns


def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Kamera tidak terdeteksi!")returns

        #Inisialisasi Mediapipe
        mp_hands = mp.solutions.hands
        mp_drawing = mp.solutions.drawing_utils
        hands = mp_hands.Hands(
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.7
        )
        while True:
            success, frame = cap.read()
            if not success:
                print("Gagal membaca frame kamera")
                break

             #Mirror effect
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            #Proses deteksi
            results = hands.process(rgb)

            if results.multi_hand_landmarks and results.multi_handedness:
                for idx, hand in enumerate(results.multi_hand_landmarks.landmark):

                    label = results.multi_hand_handedness[idx].classifications[0].label

                    h, w, c = frame.shape
                    cx = int(hand_landmarks.landmarks[0].x*w)
                    cy =  int(hand_landmarks.landmarks[0].x*h)

                    if label == 'Right':
                        text = "KANAN"
                        color = (255, 0, 0)
                    else:
                        text = "KIRI"
                        color = (0, 0, 255)

                    cv2.putText(frame, text, (cx -50, cy-30),

                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)

                            mp_drawing.draw_landmarks(
                                frame,
                                hand.landmark,

                    mp_hands.Hands_CONNECTIONS
                            )
                        cv2.imshow("Deteksi Tangan Kanan & kiri", frame)
                            #Tekan q untuk keluar
                            if cv2.waitKey(1) & 0xFF == ord('q'):
                                break
                        cap.release()
                        cv2.destroyAllWindows()
            if_name_ == "_main_":
                main()



