# opencv_RecyclableWastes_Detection

1. Detects aluminum cans and plastic bottles using AlexeyAB-darknet YOLO.

2. yolov4.conv.137 and custom trained weights are removed from the backup folder because they exceeded github's file size limit.

3. You can train your own weights using yolov4-custom.cfg if you'd like to give this project a try, then put the weight files into backup folder.

4. Dataset source: <a href="https://www.kaggle.com/arkadiyhacks/drinking-waste-classification">Drinking Waste Classification - Kaggle</a>and I re-labelled 1239 images myself using labelImg.

Original Image 1: <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_04.JPG" width="600" height="400">

test Image: <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_04_predictions.JPG" width="600" height="400">

Original Image 2: <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_06.JPG" width="600" height="400">

test Image (set 0.60 threshold) : <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_06_predictions_t0-6.JPG" width="600" height="400">
