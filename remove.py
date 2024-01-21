import os
import re
from PIL import Image
import shutil
import xml.etree.ElementTree as ET

folder_holding_yolo_files = r'C:/Users/abokh/OneDrive/Desktop/testobject'


def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False


os.chdir(folder_holding_yolo_files)

for each_yolo_file in os.listdir(folder_holding_yolo_files):
    if each_yolo_file.endswith("xml"):
        the_file = open(each_yolo_file, 'r')
        all_lines = the_file.readlines()
        image_name = each_yolo_file
        # print ()

        # Check to see if there is an image that matches the txt file
        if os.path.exists(each_yolo_file.replace('xml', 'jpeg')):
            image_name = each_yolo_file.replace('xml', 'jpeg')
        if os.path.exists(each_yolo_file.replace('xml', 'jpg')):
            image_name = each_yolo_file.replace('xml', 'jpg')
        if os.path.exists(each_yolo_file.replace('xml', 'png')):
            image_name = each_yolo_file.replace('xml', 'png')
        # print (image_name)
        # print (each_yolo_file)

        if not image_name == each_yolo_file:
            mytree = ET.parse(each_yolo_file)
            myroot = mytree.getroot()
            for x in myroot.findall('object'):
                item = x.find('name').text
                if item == "chair" or item == 'stairs':
                    # org1 = os.path.join('I:/GPOpjectDetection/Tensorflow/testobject', each_yolo_file)
                    # target1 = os.path.join('I:/GPOpjectDetection/Tensorflow/new', each_yolo_file)
                    # # print (org)
                    # shutil.copyfile(org1, target1)
                    #
                    # org2 = os.path.join('I:/GPOpjectDetection/Tensorflow/testobject', image_name)
                    # target2 = os.path.join('I:/GPOpjectDetection/Tensorflow/new', image_name)
                    #
                    # shutil.copyfile(org2, target2)
                    # print(item)
                    # print(folder_holding_yolo_files)
                    # os.remove(each_yolo_file)
                    print(folder_holding_yolo_files+'/'+each_yolo_file)
                    print(folder_holding_yolo_files+'/'+image_name)


