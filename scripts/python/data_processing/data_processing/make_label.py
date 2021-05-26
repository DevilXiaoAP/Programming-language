import os, re
import xml.etree.ElementTree as ET

class_index = {"car": 0, "truck": 1, "chemical_vehicle": 2, "bus": 3, "chemical_sign": 4}


def getbox(box, w, h):
    xmin = float(box.find("xmin").text) / w
    ymin = float(box.find("ymin").text) / h
    xmax = float(box.find("xmax").text) / w
    ymax = float(box.find("ymax").text) / h

    return ((xmin + xmax) / 2, (ymin + ymax) / 2, xmax - xmin, ymax - ymin)


def convert(inpath, outpath):
    if not os.path.exists(outpath):
        os.makedirs(outpath)
    filelist = os.listdir(inpath)
    regex = re.compile("(.+)\\.xml")
    for file in filelist:
        filename = regex.match(file)
        if filename:
            txtfile = open(outpath + "/" + filename.group(1) + ".txt", "w")
            root = ET.parse(inpath + "/" + file).getroot()
            size = root.find("size")
            width = int(size.find("width").text)
            height = int(size.find("height").text)
            for obj in root.iter("object"):
                name = obj.find("name").text
                index = class_index[name]
                box = getbox(obj.find("bndbox"), width, height)
                txtfile.write("%s %.6f %.6f %.6f %.6f\n" % (index, *box))
            txtfile.close()
        print(file, "converted")


if __name__ == '__main__':
    convert("F:/dataset/VehicleType/xml", "F:/dataset/VehicleType/label")
