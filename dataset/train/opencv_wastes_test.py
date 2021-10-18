# Dataset source: Face Mask Detection from Kagggle
import cv2
import numpy as np
import imutils
import time
from matplotlib import pyplot as plt
net = cv2.dnn.readNetFromDarknet("yolov4-custom-waste.cfg","backup/yolov4-custom-waste_2000.weights")
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
classes = [line.strip() for line in open("obj.names")]
colors = [(0,0,255),(255,0,0),(0,255,0)]

def yolo_detect(frame):
    # forward propogation
    img = cv2.resize(frame, None, fx=0.4, fy=0.4)
    height, width, channels = img.shape 
    blob = cv2.dnn.blobFromImage(img, 1/255.0, (416, 416), (0, 0, 0), True, crop=False)
    net.setInput(blob)
    outs = net.forward(output_layers)

    # get detection boxes
    class_ids = []
    confidences = []
    boxes = []
    
    detection_threshold = 0.7
    
    for out in outs:
        for detection in out:
            global tx, ty, tw, th, confidence, class_id, confidence, label, indexes
            tx, ty, tw, th, confidence = detection[0:5]
            scores = detection[5:]
            class_id = np.argmax(scores)  
            if confidence > detection_threshold:   
                center_x = int(tx * width)
                center_y = int(ty * height)
                w = int(tw * width)
                h = int(th * height)

                # Retreives Bounding boxes coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)
                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)
                
                
    # draw boxes
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.3, 0.4)
    font = cv2.FONT_HERSHEY_PLAIN
    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            # print object names and confidences
            label = str(classes[class_ids[i]]) + "; {:.2f}%".format(confidences[i])
            color = colors[class_ids[i]]
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)    # draw bounding boxes
            # (畫布,文字,座標,字型, 倍率, 顏色, 線條寬度, 類型)
            cv2.putText(img, label, (x, y -5), font, 1, color, 1)   # show text
    return img

# ==========================
# Image Detection
# ==========================
img = cv2.imread("/test_data/wastes.jpg")
image = yolo_detect(img)
# img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cv2.imshow('image', image)

# ==========================
# Real time image detection
# ==========================
# cap = cv2.VideoCapture(1)

# while True:
#     hasFrame, frame = cap.read()
    
#     img = yolo_detect(frame)
#     cv2.imshow("Frame", imutils.resize(img, width=850))

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()