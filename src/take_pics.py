import cv2
import json
import os

cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

img_counter = 1
print("\nTo take picture,\
       \n    1) Click on video and press 'SPACE' (may lag after pressing)\
       \n    2) Input label in terminal")
print("To quit, press 'ESC'\n")

# get test vs training data
pic_type = int(input("Test (1) or Train (2) : "))
while pic_type not in [1,2]:
    print("\nPlease make valid selection.")
    pic_type = int(input("Test (1) or Train (2) : "))

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
while True:
    ret, frame = cam.read()
    cv2.imshow("Capture", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27: # ESC pressed
        print("\nEscape hit, closing...")
        break

    elif k%256 == 32: # SPACE pressed
        # get label
        label = input("enter label 0,1,2,3,4,5: ")

        # log data info
        if pic_type == 1: # test
            data_file_name = os.path.join(THIS_FOLDER, '../data/data_test.json')
            filepath = os.path.join(THIS_FOLDER, '../images/test/')
            file_label = "test"
        else: # train
            data_file_name = os.path.join(THIS_FOLDER, '../data/data_train.json')
            filepath = os.path.join(THIS_FOLDER, '../images/train/')
            file_label = "train"

        # save data
        if os.path.exists(data_file_name): # data file exists, append new data
            with open(data_file_name) as json_file:
                data = json.load(json_file)
                img_counter = int(data["num_pics"] + 1)
        else: # initialize new dictionary
            data = {"num_pics":img_counter, "pics":{}}
        data["num_pics"] = img_counter

        img_name = "hand_{}{:04d}.png".format(file_label, img_counter)
        data["pics"][img_counter] = {"label":label, "img_name":img_name, "keypoints":[]}


        with open(data_file_name, "w") as json_file:
            json.dump(data, json_file)


        cv2.imwrite(filepath+img_name, frame)
        print("    {} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
