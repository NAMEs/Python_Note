'''
使用网络摄像头识别实时视频中的人脸 - 更快的版本（需要安装OpenCV）
'''

import face_recognition
import cv2

# 调用摄像头
video_capture = cv2.VideoCapture(0)

# 记录xyjy脸部编码
xyjy_image = face_recognition.load_image_file("./know/xyjy.jpg")
xyjy_face_encoding = face_recognition.face_encodings(xyjy_image)[0]

# 记录sylm脸部编码
sylm_image = face_recognition.load_image_file("./know/sylm.jpg")
sylm_face_encoding = face_recognition.face_encodings(sylm_image)[0]

# 记录zyp脸部编码
zyp_image = face_recognition.load_image_file("./know/zyp.jpg")
zyp_face_encoding = face_recognition.face_encodings(zyp_image)[0]

# 创建一个已知脸部编码列表
known_face_encodings = [
    xyjy_face_encoding,
    sylm_face_encoding,
    zyp_face_encoding
]

# 已知姓名
known_face_names = [
    "xyjy",
    "sylm",
    "zyp"
]


face_locations = []
face_encodings = []
face_names = []
process_this_frame = True

while True:
    # 读取摄像头中数据
    ret, frame = video_capture.read()

    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    if not ret:
        break

    rgb_small_frame = small_frame[:, :, ::-1]

    
    if process_this_frame:
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]

            face_names.append(name)

    process_this_frame = not process_this_frame


    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()