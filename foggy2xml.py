# 将cityscpe_xml转化为fog_cityscapes_xml:
import os
import xml.etree.ElementTree as ET
source_path = "E:/gtFine_trainvaltest/gtFine/train/"
city_names =os.listdir(source_path)
for city in city_names:
    cityscape_xml_path = "E:/gtFine_trainvaltest/gtFine/csxml/"
    foggy_xml_path = "E:/gtFine_trainvaltest/gtFine/csfgxml/"
    betas = [0.01, 0.02, 0.005]
    city_xml_list = os.listdir(cityscape_xml_path)
    for file in city_xml_list:
        if file.endswith('.xml') or file.endswith('XML'):
            city_xml = file
            print(city_xml)
            tree = ET.parse(cityscape_xml_path + city_xml)
            root = tree.getroot()
            filename = root.find('filename').text  # 获取xml中的filename
            for beta in betas:
                filename = filename.split(".png")[0] + "_foggy_beta_" + str(beta) + ".png"
                root.find('filename').text = filename
                foggy_city_xml = city_xml.split(".xml")[0] + "_foggy_beta_" + str(beta) + ".xml"
                tree.write(foggy_xml_path + foggy_city_xml)
