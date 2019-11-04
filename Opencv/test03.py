'''
图片类型:numpy.ndarray

'''

import cv2
import numpy

def get_img_info(photo):
    
    print(type(photo))
    # print("photo:\n",photo)

    print("photo.shape:", photo.shape)
    # a = numpy.shape(photo)
    # print("a:",a)
    print("photo.size:", photo.size)
    print("photo.dtype:", photo.dtype)

if __name__ == "__main__":
    img = cv2.imread("1.jpg")
    # cv2.namedWindow('1.jpg')
    cv2.imshow('1.jpg', img)
    while(1):
        c = cv2.waitKey(0)
        if c == '27':
            print("c:", c)
            cv2.destroyWindow('1.jpg')
            break
        else:
            print("c:", c)
            cv2.destroyAllWindows()
            break
        # print(img)
    get_img_info(img)
    cv2.imwrite("2.jpg", img)