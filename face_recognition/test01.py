'''
人脸画框
'''

import cv2
import face_recognition


image1 = cv2.imread('./unknow/7.jpg')

face_locations = face_recognition.face_locations(image1)


# print(face_locations)
print(len(face_locations))
for location in face_locations: 

    top,right,bottom,left = location
    
    cv2.rectangle(image1, (left,top), (right,bottom), (0,0,0), 2)
    # cv2.rectangle(image1, (left, bottom-35), (right, bottom), (0,0,0),cv2.FILLED)
    # font = cv2.FONT_HERSHEY_DUPLEX
    # cv2.putText(image1, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

cv2.imshow('photo', image1)

cv2.waitKey(0)

cv2.destroyAllWindows()