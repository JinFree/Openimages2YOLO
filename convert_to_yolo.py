import os
import cv2
import numpy as np

dataset_root = os.path.join("./", "data")

csv_list = [
    "sub-train-annotations-bbox.csv",
    "sub-validation-annotations-bbox.csv",
    "sub-test-annotations-bbox.csv"
    ]
folder_list = [
    "train",
    "validation",
    "test"
]
classes = [
    "Person",
    "Car"
]

class_txt = open(os.path.join(dataset_root, "class.txt"), 'w')
for class_name in classes:
    class_txt.write(class_name + "\n")
class_txt.close()

def line2data(line_list):
    filename = line_list[0]
    xmin = float(line_list[4])
    xmax = float(line_list[5])
    ymin = float(line_list[6])
    ymax = float(line_list[7])
    class_number = classes.index(line_list[-1][:-1])
    cx = (xmin+xmax)*0.5
    cy = (ymin+ymax)*0.5
    width = xmax-xmin
    height = ymax-ymin
    
    line_to_write = "{} {} {} {} {}\n".format(class_number, cx, cy, width, height )
    return line_to_write
    

for idx in range(len(folder_list)):
    csv_path = os.path.join(dataset_root, csv_list[idx])
    img_root = os.path.join(dataset_root, folder_list[idx])
    images_txt = os.path.join(dataset_root, folder_list[idx] + ".txt")
    images_f = open(images_txt, 'w')
    f = open(csv_path, 'r')
    filename = "ImageID"
    lines_to_write = []
    label_path = os.path.join(img_root, filename + ".txt")     
    first = True
    line = f.readline()
    line = f.readline()
    line_list = line.split(',')
    line_to_write = line2data(line_list)
    filename = line_list[0]

    while True:
        line = f.readline()
        if not line: 
            break
        line_list = line.split(',')
        line_to_write = line2data(line_list)

        if filename == line_list[0]:
            lines_to_write.append(line_to_write)

        elif filename != line_list[0]:
            label_path = os.path.join(img_root, filename + ".txt")      
            ff = open(label_path,'w')
            ff.writelines(lines_to_write)
            ff.close()
            image_path = os.path.join(img_root, filename + ".jpg")
            image_path = os.path.abspath(image_path)
            images_f.write(image_path + "\n")

            filename = line_list[0]
            lines_to_write = []
            lines_to_write.append(line_to_write)


    label_path = os.path.join(img_root, filename + ".txt")      
    ff = open(label_path,'w')
    ff.writelines(lines_to_write)
    ff.close()
    image_path = os.path.join(img_root, filename + ".jpg")
    image_path = os.path.abspath(image_path)
    images_f.write(image_path + "\n")

    images_f.close()
    f.close()



