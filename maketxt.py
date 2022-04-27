# 制作cityscape数据集的：/ImageSets/Main/train.txt
# 批量读取文件名（不带后缀）(加入前缀train/city_name/pic_name)

import os
file_path = "E:/leftImg8bit_trainvaltest/leftImg8bit/train/"
citys = os.listdir(file_path)
for city in citys:
    pic_path = file_path + city + "/"
    pic_path_list = os.listdir(pic_path)
    for file_list in pic_path_list:
        if file_list.endswith('png') or file_list.endswith('PNG'):
            with open("E:/leftImg8bit_trainvaltest/leftImg8bit/ImageSets/Main/train.txt", "a") as f:
                f.write(file_list.split("_leftImg8bit.png")[0] + "\n")
