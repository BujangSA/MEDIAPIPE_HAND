import cv2
import mediapipe as mp
from collections import deque

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Kamera tidak terdeteksi")
    exit()

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

#Buffer untuk smoothing (5 frame terakhir)
z_buffer = deque(maxlen=5)

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:

            mp_drawing.draw_landmarks(img,hand_landmarks,mp_hands.HAND_CONNECTIONS)

            #Hitung rata-rata Z dari semua landmark
                total_z = 0
                for Im in hand_landmarks.landmark:
                    total_z += Im.z

                avg_z = total_z/len(hand_landmarks.landmark)

                #Masukkan ke buffer smoothing z_buffer.append(avg_z)

                h, w, c = img.shape
                cx = int(hand_landmarks.landmark[0].x*w)
                cy = int(hand_landmarks.landmark[0].y*h)

                #Theshold (bisa disesuaikan)
if smooth_z < -0.07:
                posisi = "DEPAN"
                warna = (0, 255, 0)
            else:
                posisi = "BELAKANG"
                warna = (0, 0, 255)

            cv2.putText(img, posisi, (cx - 60, cy - 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, warna, 3)

            # Tampilkan nilai Z untuk debugging
            cv2.putText(img, f"Z: {round(smooth_z, 3)}", (10, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

    cv2.imshow("Deteksi Depan & Belakang (Versi Terbaru)", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
