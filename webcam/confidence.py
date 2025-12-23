import cv2
import time

def confidence_check(duration=10):
    cap = cv2.VideoCapture(0)
    start = time.time()
    frames = 0
    face_present = 0

    face_cascade = cv2.CascadeClassifier(
        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    )

    while time.time() - start < duration:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        frames += 1
        if len(faces) > 0:
            face_present += 1

        cv2.imshow("Confidence Check", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

    confidence_score = round((face_present / frames) * 100, 2)
    return confidence_score
