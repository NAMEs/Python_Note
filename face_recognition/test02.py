'''
识别图像中的单个人脸并且在人脸中画框并显示姓名
'''

import face_recognition
import cv2

image_xyjy = cv2.imread('./know/xyjy.jpg')
image_sylm = cv2.imread('./know/sylm.jpg')
image_zyp = cv2.imread('./know/zyp.jpg')
# image_xyjy = face_recognition.load_image_file('./know/xyjy.jpg')
# image_sylm = face_recognition.load_image_file('./know/sylm.jpg')
# image_zyp = face_recognition.load_image_file('./know/zyp.jpg')
# print(type(image_sylm))   # <class 'numpy.ndarray'>

xyjy_face_encodings = face_recognition.face_encodings(image_xyjy)[0]
sylm_face_encodings = face_recognition.face_encodings(image_sylm)[0]
zyp_face_encodings = face_recognition.face_encodings(image_zyp)[0]

know_face_encodings = [xyjy_face_encodings, sylm_face_encodings, zyp_face_encodings]
know_face_name = ['xyjy', 'sylm', 'zyp']

# image1 = face_recognition.load_image_file('./unknow/4.jpg')
# image1 = face_recognition.load_image_file('./know/zyp.jpg')
image1 = cv2.imread('./know/zyp.jpg')
image1_locations = face_recognition.face_locations(image1)
image1_face_encodings = face_recognition.face_encodings(image1, image1_locations)



for (top,right,bottom,left), face_encoding in zip(image1_locations,  image1_face_encodings):

    matches = face_recognition.compare_faces(know_face_encodings, face_encoding,tolerance=0.5)
    print("matches:", matches)
    
    name = 'unknown'
    if True in matches:
        first_match_index = matches.index(True)
        name = know_face_name[first_match_index]

    cv2.rectangle(image1, (left,top), (right,bottom), (0,0,255), 2)

    cv2.rectangle(image1, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    # cv2.putText(img, str(i), (123,456)), font, 2, (0,255,0), 3)
    # 各参数依次是：图片，添加的文字，左上角坐标，字体，字体大小，颜色，字体粗细
    cv2.putText(image1, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow('photo', image1)

cv2.waitKey(0)
       
cv2.destroyAllWindows()