'''
打开视频:
打开摄像头:
'''
from cv2 import cv2

def open_video(videoname):
    capture = cv2.VideoCapture(videoname)

    print(type(capture))
    # help(capture.read)
    
    while True:
        ret,image = capture.read()
        cv2.imshow("video", image)
        key = cv2.waitKey(50)
        # print('key:', key)

        if key & 0xFF==ord('q'):
            # capture.release()
            # cv2.destroyAllWindows()
            print("key:",key)
            break
        

    capture.release()   
    cv2.destroyAllWindows()

def open_camera():
    capture = cv2.VideoCapture(0)
    
    while(True):
        try:
            ret, frame = capture.read()
            cv2.imshow("camera", frame)
            key = cv2.waitKey(50)

            if key & 0xFF==ord('q'):
                print("key:", key)
                # cv2.destroyAllWindows()
                # capture.release()
                break
            # else:
            #     print("key:",key)
            #     # capture.release()
            #     # cv2.destroyAllWindows()
            #     break
        except Exception as e:
            print("e:",e) 
    
    capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # videoname = r'F:\python\爬虫\视频爬取\hshy\3b1094864ca93404c93517d6eca8de27.mp4'

    # open_video(videoname)

    open_camera()
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()
