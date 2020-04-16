# hand-detection
Multi-class hand shape detection using binary classifiers. Final project for CS/ECE/ME 532 at UW-Madison.

Keypoint extraction performed using [OpenCV implementation](https://www.learnopencv.com/hand-keypoint-detection-using-deep-learning-and-opencv/) of [Carnegie Mellon University Paper](https://arxiv.org/pdf/1704.07809.pdf). 

Note: To run keypoint detection, [download the caffe model here](http://posefs1.perception.cs.cmu.edu/OpenPose/models/hand/pose_iter_102000.caffemodel) and put it in a folder named "hand-model" at the same level as this repository. File tree should be:

<img src="https://github.com/apletta/hand-detection/blob/master/images/file_tree.png" alt="images/file_tree.png" width="40%">

### Sample Keypoint Output
#### Original image: &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Keypoints: &ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp; Skeleton: 
<img src="https://github.com/apletta/hand-detection/blob/master/images/sample-keypoint-output/Output-Original.jpg" alt="images/file_tree.png" width="30%"> <img src="https://github.com/apletta/hand-detection/blob/master/images/sample-keypoint-output/Output-Keypoints.jpg" alt="images/file_tree.png" width="30%"> <img src="https://github.com/apletta/hand-detection/blob/master/images/sample-keypoint-output/Output-Skeleton.jpg" alt="images/file_tree.png" width="30%">
