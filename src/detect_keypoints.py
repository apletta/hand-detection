from __future__ import division
import cv2
import time
import numpy as np
import json
import os
import sys
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
# load model info

protoFile = os.path.join(THIS_FOLDER, '../model-param/pose_deploy.prototxt')
weightsFile = os.path.join(THIS_FOLDER, '../../hand-model/pose_iter_102000.caffemodel')
nPoints = 21
POSE_PAIRS = [ [0,1],[1,2],[2,3],[3,4],[0,5],[5,6],[6,7],[7,8],[0,9],[9,10],[10,11],[11,12],[0,13],[13,14],[14,15],[15,16],[0,17],[17,18],[18,19],[19,20] ]
net = cv2.dnn.readNetFromCaffe(protoFile, weightsFile)

# read in images from saved data
data_file_name = os.path.join(THIS_FOLDER, '../data/data.json')
if not os.path.exists(data_file_name): # data file exists, append new data
    print("\nData file {} does not exist, please run take_hand_pics.py to generate data.\n".format(data_file_name))
    sys.exit()
with open(data_file_name) as json_file:
    data = json.load(json_file)
    filepath = os.path.join(THIS_FOLDER, '../images/train/')
    for img_index in range(1,int(data["num_pics"])+1):
        frame = cv2.imread(filepath + data["pics"][str(img_index)]["img_name"])

        frameOriginal = np.copy(frame)
        frameCopy = np.copy(frame)
        frameWidth = frame.shape[1]
        frameHeight = frame.shape[0]
        aspect_ratio = frameWidth/frameHeight

        threshold = 0.1

        t = time.time()
        # input image dimensions for the network
        inHeight = 368
        inWidth = int(((aspect_ratio*inHeight)*8)//8)
        inpBlob = cv2.dnn.blobFromImage(frame, 1.0 / 255, (inWidth, inHeight), (0, 0, 0), swapRB=False, crop=False)

        net.setInput(inpBlob)

        output = net.forward()
        print("time taken by network : {:.3f}".format(time.time() - t))

        # Empty list to store the detected keypoints
        points = []

        for i in range(nPoints):
            # confidence map of corresponding body's part.
            probMap = output[0, i, :, :]
            probMap = cv2.resize(probMap, (frameWidth, frameHeight))

            # Find global maxima of the probMap.
            minVal, prob, minLoc, point = cv2.minMaxLoc(probMap)

            if prob > threshold :
                cv2.circle(frameCopy, (int(point[0]), int(point[1])), 8, (0, 255, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.putText(frameCopy, "{}".format(i), (int(point[0]), int(point[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, lineType=cv2.LINE_AA)

                # Add the point to the list if the probability is greater than the threshold
                points.append((int(point[0]), int(point[1])))
            else :
                points.append(None)

        # store keypoints
        data["pics"][str(img_index)]["keypoints"] = points
        with open(data_file_name, "w") as json_file:
            json.dump(data, json_file)

        # Draw Skeleton
        for pair in POSE_PAIRS:
            partA = pair[0]
            partB = pair[1]

            if points[partA] and points[partB]:
                cv2.line(frame, points[partA], points[partB], (0, 255, 255), 2)
                cv2.circle(frame, points[partA], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)
                cv2.circle(frame, points[partB], 8, (0, 0, 255), thickness=-1, lineType=cv2.FILLED)

        # display images
        cv2.imshow('Output-Keypoints', frameCopy)
        cv2.imshow('Output-Skeleton', frame)
        cv2.imshow('Output-Original', frameOriginal)


        # cv2.imwrite('../images/keypoint-detection/Output-Keypoints.jpg', frameCopy)
        # cv2.imwrite('../images/keypoint-detection/Output-Skeleton.jpg', frame)
        # cv2.imwrite('../images/keypoint-detection/Output-Original.jpg', frameOriginal)

        print("Total time taken : {:.3f}".format(time.time() - t))
        cv2.waitKey(0)

cv2.destroyAllWindows()
