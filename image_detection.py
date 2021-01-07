import cv2
from Detector import Detector


if __name__ == '__main__':

    Sheep = Detector(
        pth_weights='Sheep_Detect/yolov3_training.weights', # path to weights file
        pth_cfg='Sheep_Detect/yolov3_testing.cfg', # path to test config file
        pth_classes='Sheep_Detect/classes.txt') # path to classes.txt

    img_name ="Sheep/deneme11.jpg"
    img = cv2.resize(cv2.imread(img_name),(600,480))
    Sheep.detect(img)

    cv2.imshow("Detection",Sheep.image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
