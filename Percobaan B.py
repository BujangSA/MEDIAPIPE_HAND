import cv2
import mediapipe

capture = cv2.VideoCapture(10)
mediapipe = mediapipe.solutions.hands
tangan = mediapipehand.Hands(max_num_hands=1)
mpdraw =
mediapipe.solutions.drawing_utils

while True:
    success, image = capture.read()
    imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = tangan.process(imgRGB)
    if results.multi_hand_landmarks:
        for titiktangan in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(image,titiktangan,mediapipehand.HAND_CONNECTIONS)

            for id, titik in enumerate(titiktangan):
                print (id)
                print (titik.x)
                print (titik.y)

    cv2.imshow('image',image)
    cv2.waitKey(10)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
