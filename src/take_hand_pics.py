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

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
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
        data_file_name = os.path.join(THIS_FOLDER, '../data/data.json')

        # save data
        if os.path.exists(data_file_name): # data file exists, append new data
            with open(data_file_name) as json_file:
                data = json.load(json_file)
                img_counter = int(data["num_pics"] + 1)
        else: # initialize new dictionary
            data = {"num_pics":img_counter, "pics":{}}
        data["num_pics"] = img_counter

        img_name = "hand_train{:04d}.png".format(img_counter)
        data["pics"][img_counter] = {"label":label, "img_name":img_name, "keypoints":[]}


        with open(data_file_name, "w") as json_file:
            json.dump(data, json_file)

        # filepath = "../images/train/"
        filepath = os.path.join(THIS_FOLDER, '../images/train/')
        cv2.imwrite(filepath+img_name, frame)
        print("    {} written!".format(img_name))
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
