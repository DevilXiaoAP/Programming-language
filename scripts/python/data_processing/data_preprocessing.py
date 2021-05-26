import glob
import xml.etree.ElementTree as ET


def main(path):
    wrong_class_lst1, wrong_class_lst2, w_lst = [], [], []
    for xml_file in glob.glob(path + '*.xml'):
        print(xml_file)
        tree = ET.parse(xml_file)
        root = tree.getroot()

        for member in root.findall('object'):
            value = member[0].text
            if value == 'chemical_vehical' or value == 'chemcial_vehicle' or value == 'chemical_vehicel':
                wrong_class_lst1.append(root.find('filename').text)
                member[0].text = 'chemical_vehicle'
            if value == 'chemcial_sign':
                wrong_class_lst2.append(root.find('filename').text)
                member[0].text = 'chemical_sign'
            if value == 'w':
                w_lst.append(root.find('filename').text)
        tree.write(xml_file)
    print('wrong_class_list1:', wrong_class_lst1)
    print('wrong_class_list2:', wrong_class_lst2)
    print('w_list:', w_lst)


if __name__ == "__main__":
    xml_path = 'F:/dataset/VehicleType/xml/'
    main(xml_path)
