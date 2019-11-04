'''
识别图像中的所有人脸，并且在画框中显示姓名
识别肖央和王太利合照
'''
import cv2
import face_recognition

image1 = cv2.imread('./unknow/kzxd2.jpg')
xy_image = cv2.imread('./know/xy.jpg')
wtl_image = cv2.imread('./know/wtl.jpg')

xy_face_encoding = face_recognition.face_encodings(xy_image)[0]
wtl_face_encoding = face_recognition.face_encodings(wtl_image)[0]
know_face_encoding = [xy_face_encoding, wtl_face_encoding]
know_names = ['xy', 'wtl']

face_locations = face_recognition.face_locations(image1)
# print(len(face_locations))      # 2
# print(type(face_locations))     # list
# print(face_locations)           # [(68, 414, 175, 306), (36, 195, 126, 106)]
# face_encodings = face_recognition.face_encodings(image1)    # 第一种
# print(len(face_encodings))      # 2
# print(type(face_encodings))     # list
# print(face_encodings)         # array

face_encodings = face_recognition.face_encodings(image1, face_locations)     #第二种
# print(len(face_encoding))     # 2
# print(type(face_encoding))    # list
# print(face_encoding)          # array
# 证明两种以上两种方式得到的数据为一样的
# print(face_encoding[0] == face_encodings[0])  # true
# print(face_encoding[1] == face_encodings[1])  # true

for face_location,face_encoding in zip(face_locations, face_encodings):
    # print(type(face_location))
    top,right,bottom,left = face_location
    matches = face_recognition.compare_faces(know_face_encoding, face_encoding, tolerance=0.43)
    print("matches_type:", type(matches))
    print("matches:", matches)
    name = 'Unknow'
    if True in matches:
        name_index = matches.index(True)
        name = know_names[name_index]

    cv2.rectangle(image1, (left, top), (right, bottom), (255,255,255), 2)
    cv2.rectangle(image1, (left, bottom + 35), (right, bottom), (0,0,255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    print(name)
    cv2.putText(image1, name, (left + 20, bottom + 20), font, 1.0, (255, 255, 255), 1)

cv2.imshow('face', image1)
cv2.waitKey(0)
cv2.destroyAllWindows()