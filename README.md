# Yolo-Sheep-Detection

*This project aims to detect sheep objects in a picture or video. In order to do that an object detection model is built using Yolo-v3. Training is done in Google Colab. COCO train/val2014 images are used for training*

### Handling Dataset

- *Step1 : Download annotations from :  [COCO Dataset](https://cocodataset.org/)*

- *Step2 : Download images belong to 'Sheep' class. To do that run ``` Dataset/get_coco_images.py ```*

- *Step3 : Get xml files for downloaded images. Run ``` Dataset/get_xml_files.py ```*

- *Step4 : Rename downloaded xml files by executing ``` Dataset/rename.py ```*

- *Step 5 : Convert xml files to Yolo-darknet txt format by running ``` Dataset/convert.py ```. Xml files and ```convert.py``` file must be in the same directory.*

### Object Detection

-  *Run ``` image_detection.py ``` for sheep detection in an image*
-  *Run ``` video_detection.py ``` for sheep detection in an video*
