# -*- coding:utf-8 -*-
import xml.etree.cElementTree as ET
import shutil, os

def parseXML(xml_file):
    
    tree = ET.ElementTree(file=xml_file)
#    print(tree.getroot())
    root = tree.getroot()
#    print("tag=%s, attrib=%s" % (root.tag, root.attrib))

    for child in root:
        print(child.tag, child.attrib)
        for file in child.iter('file'):
            source_path = file.get('source_path')
            destination_path = child.get('destination_path')
            file_name = child.get('file_name')
            copyfrompath = source_path + os.sep + file_name
            copytopath = destination_path + os.sep + file_name
            if os.path.isfile(copyfrompath) == True:
                print ("Copying...")
                print ("copy file %s ftom %s to %s" % (file_name, copyfrompath, copytopath))
                shutil.copyfile(copyfrompath, copytopath)

#            print(file.attrib)


if __name__ == "__main__":
    parseXML("config.xml")