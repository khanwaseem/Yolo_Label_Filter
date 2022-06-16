import glob
import cv2
import os
import numpy as np
import re

# Minimum width to consider
min_w = 40
# Minimum height to consider
min_h = 40

#Path to the input text files
input_dir_path = "E:/Annotation_Data/Seq03/00_YOLO_Annotations/image.*.txt"

#Path to the out directory to write new text files
output_dir_path = "E:/Annotation_Data/Seq03/00_YOLO_Annotations_Filtered"

for img in glob.glob(input_dir_path):
    print(img)
    file_name = img.split("\\")[-1]
    #print(file_name)
    if not os.path.exists(output_dir_path):
        os.makedirs(output_dir_path)
    try:
        with open(img, "r") as file:
            for line in file:
                class_id,x,y,w,h = line.split(" ")
                x,y,w,h = float(x),float(y),float(w),float(h)
                if w-x>=min_w and h-y>min_h:
                    with open(output_dir_path+"/"+file_name, "a+") as file2:
                        file2.write(line)
    except Exception as e:
        print(e)
    
