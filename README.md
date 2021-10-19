# opencv_RecyclableWastes_Detection

1. An object detection model that detects aluminum cans and plastic bottles using AlexeyAB-darknet YOLO.

2. yolov4.conv.137 and custom weights are removed from the backup folder because they exceeded github's file size limit.

3. You can train your own model if you'd like to give this project a try, then put the weight files into the backup folder.

4. Dataset source: <a href="https://www.kaggle.com/arkadiyhacks/drinking-waste-classification">Drinking Waste Classification - Kaggle</a>and I re-labelled 1239 images myself using labelImg.

Original Image 1: <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_04.JPG" width="600" height="400">

test Image: <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_04_predictions.JPG" width="600" height="400">

Original Image 2: <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_02.JPG" width="600" height="400">

test Image : <br/>
<img src="https://github.com/PDooDP/opencv_RecyclableWastes_Detection/blob/master/test_data/my_02_predictions.JPG" width="600" height="400">

test video 1 : <br/>

https://user-images.githubusercontent.com/87317691/137854898-47cc561b-2106-4da9-b62b-30523102d079.mp4

test video 2 : <br/>

https://user-images.githubusercontent.com/87317691/137854942-7cf12df8-3ab1-4a86-b946-1d105be4e57a.mp4

<br/>
I stopped training this model after 2000 iterations, so the outputs don't look so good.
