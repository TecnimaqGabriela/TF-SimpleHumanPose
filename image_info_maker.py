import json
import os

with open('/home/tecnimaq/Gabriela/Detectron/json_dump/jsonboxes_Dataset_4.json') as openjason:
    Detectron_boxes = json.load(openjason)

image_info={
    'images': [],
    'categories': [{'supercategory': 'person', 'id': 1, 'name': 'person'}]
}

for m in range(len(Detectron_boxes)):
    per_image_info={'file_name': 0,'id': 0}
    #print('Detectron_boxes: {}'.format(Detectron_boxes[m]['file_name']))
    per_image_info['file_name'] = Detectron_boxes[m]['file_name'] 
    #print('Detectron_boxes: {}, image_info: {}'.format(Detectron_boxes[m]['file_name'], per_image_info['file_name']))
    per_image_info['id'] = Detectron_boxes[m]['image_id']
    image_info['images'].append(per_image_info)
    
def id(elem):
    return elem['id']

#image_info.sort(key=id)
dir = '/home/tecnimaq/Gabriela/Detectron/image_info_from_Detectron'
file_name = 'image_info_test2017.json'
with open(os.path.join(dir,file_name),'w') as thisfile:
    json.dump(image_info, thisfile)
