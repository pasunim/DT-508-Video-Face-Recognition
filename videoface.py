import cv2
import face_recognition
import numpy as np
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
video_path = BASE_DIR / "videos" / "WIN_20220925_13_54_04_Pro.mp4"
image_path = BASE_DIR / "content" / "banyapon.jpg"
window_name = "Video"

cap = cv2.VideoCapture(str(video_path), 0)
database_image = face_recognition.load_image_file(str(image_path))
data_base_encoding = face_recognition.face_encodings(database_image)[0]
face_locations = []
person_face_encodings = [data_base_encoding]
person_face_names = ["BANYAPON POOLSAWAS"]
data_locations = []
data_encodings = []
data_names = []
frameProcess = True
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 960, 540)

while True:
    ret, frame = cap.read()
    if not ret or frame is None:
        break
    rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])
    data_locations = face_recognition.face_locations(rgb_frame)
    for top, right, bottom, left in data_locations:
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 4)
        data_encodings = face_recognition.face_encodings(rgb_frame, data_locations)
        data_names = []
        for dc in data_encodings:
            matches = face_recognition.compare_faces(person_face_encodings, dc)
            name = "UNKNOWN"
            if True in matches:
                first_match_index = matches.index(True)
                name = person_face_names[first_match_index]
            data_names.append(name)
            cv2.rectangle(
                frame, (left, bottom - 35), (right, bottom), (26, 174, 10), cv2.FILLED
            )
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(
                frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1
            )
    frame = cv2.resize(frame, (960, 540))
    cv2.imshow(window_name, frame)
    if cv2.waitKey(25) == 13:
        break

cap.release()
cv2.destroyAllWindows()
