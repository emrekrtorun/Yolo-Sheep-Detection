import os

xml = "annotations_pascalformat/" # xml files dir 
annot_path= "coco_sheep_annot/"	# sheep annots dir 
img_path = "coco_new/" # sheep images dir 

xmls = os.listdir(xml)
imgs = os.listdir(img_path)
img = []
xmls_n  = []
for i in imgs:
    img.append(i[:-4])


for i in xmls:
    d = i.replace("COCO_train2014_","")
    xmls_n.append(d[:-4])


for i in range(len(xmls)):
    if(xmls_n[i] in img):
        with open (xml+xmls[i],'r') as file:
            data = file.read()

        with open(annot_path+xmls_n[i]+".xml",'w') as annot:
            annot.write(data)