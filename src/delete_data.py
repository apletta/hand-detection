import json
import os

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))

pic_to_delete = int(input("Enter int number of pic to delete\n(ex. to delete data associated with hand_train0003.png, enter '3')\ndelete : "))
data_file_name = os.path.join(THIS_FOLDER, '../data/data.json')
with open(data_file_name) as json_file:
    # read in data
    data = json.load(json_file)

# make sure key exists
if str(pic_to_delete) in data["pics"]:

    # delete pic image file
    num_pics = int(data["num_pics"])
    pic_path = os.path.join(THIS_FOLDER, '../images/train')


    # case for deleting last pic
    if pic_to_delete == num_pics:
        os.remove(pic_path+'/'+data["pics"][str(pic_to_delete)]["img_name"])
    else:
        for i in range(pic_to_delete+1, num_pics+1):

            # decrement pics after deleted pic
            new_label = data["pics"][str(i)]["label"]
            new_img_name = "hand_train{:04d}.png".format(int(data["pics"][str(i)]["img_name"][10:14])-1)
            new_keypoints = data["pics"][str(i)]["keypoints"]
            data["pics"][str(i-1)] = {"label": new_label, "img_name": new_img_name, "keypoints": new_keypoints}

            # decrement pic image files
            os.rename(r'{}/{}'.format(pic_path, data["pics"][str(i)]["img_name"]),r'{}/{}'.format(pic_path, new_img_name))

    # delete last pic data, necessary after decrementing all other pic keys
    del data["pics"][str(num_pics)]

    # decrement num_pics
    data["num_pics"] -= 1

    # overwrite data
    with open(data_file_name, "w") as json_file:
        json.dump(data, json_file)

        print("\nFiles and associated data updated.\n")
else:
    print("\n[ERROR] Specified int not in data.\n")
