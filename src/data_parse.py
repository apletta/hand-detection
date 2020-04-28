import numpy as np
import json
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
data_file_name = os.path.join(THIS_FOLDER, '../data/data.json')
nPoints = 21
with open(data_file_name) as json_file:
    data = json.load(json_file)
    
    # matrix to store distance to keypoint 0, each image stored in row
    # column array to store labels
    distance_feature = np.ndarray((int(data["num_pics"]), nPoints-1))
    label_vector = np.ndarray((int(data["num_pics"]),1))
    
    # loop through json to constuct feature array
    for i in range(1, int(data["num_pics"])+1):
        label = data["pics"][str(i)]["label"] 
        points = np.array(data["pics"][str(i)]["keypoints"] )
        # label array
        label_vector[i-1] = label
        # feature matrix
        pointZero = points[0]
        for j in range(1,nPoints):
            distance_feature[i-1][j-1] = np.sum(np.square(points[j] - pointZero))
            
    print(distance_feature)
    print(label_vector)