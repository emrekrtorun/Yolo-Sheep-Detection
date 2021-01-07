import cv2
from Detector import Detector

if __name__ == '__main__':
    Sheep = Detector(
        pth_weights='Sheep_Detect/yolov3_training.weights', # path to weights file
        pth_cfg='Sheep_Detect/yolov3_testing.cfg', # path to test config file
        pth_classes='Sheep_Detect/classes.txt') # path to classes.txt


    cap = cv2.VideoCapture("")
    #detection = cv2.VideoWriter('Detection.avi',
    #                         cv2.VideoWriter_fourcc(*'MJPG'),
    #                         10, (600,480))


    while(cap.isOpened()):
        ret, frame = cap.read()
        frame = cv2.resize(frame,(600,480))
        Sheep.detect(frame)

        cv2.imshow("Detection",Sheep.image)
    #   detection.write(Sheep.image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    #detection.release()
    cv2.destroyAllWindows()
