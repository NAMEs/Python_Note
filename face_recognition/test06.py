'''
自动放入已知图片
识别摄像头数据
'''

import cv2
import face_recognition
import os

# 存已知信息的图片
def Save_Know_Info():
    filename = r'./know/'
    image_list = os.listdir(filename)

    know_face_encodings = []
    know_face_names = []
    know_infos = {'encodings':know_face_encodings,
                 'names':know_face_names}
 
    for image in image_list:
        imagename = filename + image
        
        image_read = cv2.imread(imagename)
        image_face_encoding = face_recognition.face_encodings(image_read)[0]

        know_face_encodings.append(image_face_encoding)
        face_name = image.split('.')[0]
        know_face_names.append(face_name)
    
    # print(len(know_face_encodings))
    # print(know_face_names)
    return know_infos


# 摄像头读取数据
def Save_Video_face(know_infos):
    capture = cv2.VideoCapture(0)

    know_face_encodings = know_infos['encodings']
    know_face_names = know_infos['names']
    
    while True:
        
        ret, frame = capture.read()
        if not ret:
            break
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        # print("ret:",ret)
        # image = image[:,:,::-1]
        
        unknow_face_locations = face_recognition.face_locations(small_frame)
        unknow_face_encodings = face_recognition.face_encodings(small_frame, unknow_face_locations)

        for face_location,face_encoding in zip(unknow_face_locations, unknow_face_encodings):
            name = 'Unknow'
            top,right,bottom,left = face_location
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            matches = face_recognition.compare_faces(know_face_encodings, face_encoding, tolerance=0.43)
            # print(matches)
            if True in matches:
                first_name_index = matches.index(True)
                name = know_face_names[first_name_index]

            cv2.rectangle(frame, (left, top), (right,bottom), (0,0,255), 2)
            cv2.rectangle(frame, (left,bottom+30), (right,bottom), (0,0,255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_COMPLEX
            cv2.putText(frame, name, (left + 20, bottom + 20), font, 1.0, (255, 255, 255), 1)

        cv2.imshow('video', frame)

        if cv2.waitKey(1) & 0xFF == ('q'):
            break
    
    capture.release()
    cv2.destroyAllWindows()
    return 0


def Know():
    know_list = os.listdir('./know/')
    print("人脸库:",know_list)
    print()


def Unknow():
    unknow_list = os.listdir('./unknow/')
    print("待识别:", unknow_list)
    print()


def Demo():
    while True:
        print('*****' * 20)
        print('*****' * 9 + '1.查看人脸库' + '*****' *9)
        print('*****' * 9 + '2.待识别人脸' + '*****' *9)
        print('*****' * 9 + '3.识别人脸' + '*****' *9)
        print('*****' * 20)
        
        option = input('输入序号:')

        if option == '1':
            Know()
        elif option == '2':
            Unknow()
        elif option == '3':
            know_infos = Save_Know_Info()
            Save_Video_face(know_infos)
        else:
            break
        
if __name__ == '__main__':
    Demo()

    