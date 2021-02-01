import json
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io

with open('/home/tecnimaq/Gabriela/TF-SimpleHumanPose/output/result/COCO/result.json') as openjason:
    results = json.load(openjason)

#print (results[51])
#print(results[1].get('keypoints'))
#print(len(results[1].get('keypoints')))

path_image = input('Path de la imágen (sin /home/tecnimaq)  ')
id_image =  input('id de la imágen  ')
id_image_int = int(id_image)

image = io.imread(path_image)
#image(3) = io.imread("/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/COCO/images/val2017/000000581357.jpg")
#image(51) = io.imread("/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/COCO/images/val2017/000000581317.jpg")
plt.imshow(image)

#keypoints_1 = results[51].get('keypoints')
s=0

for obj in range(len(results)):
    image = results[obj].get('image_id')
#    print(image)
#    print(type(image))
#    print(id_image)
#    print(type(id_image))
    if image == id_image_int:
        #print(id_image)
        if results[obj].get('score') > 0.4:
            #print(results[obj].get(''))
            keypoints_1 = results[obj].get('keypoints')
            keypoint = []
            s = s+1
            for i in range(len(keypoints_1)):
                if i % 3 == 0:
                    x = keypoints_1[i]
                    y = keypoints_1[i+1]
                    plt.scatter(x,y)
                    keypoint.append((x,y))
                    #print('(',x,',',y,')')

            cara_x = [keypoint[3][0],keypoint[1][0],keypoint[0][0],keypoint[2][0],keypoint[4][0]]
            cara_y = [keypoint[3][1],keypoint[1][1],keypoint[0][1],keypoint[2][1],keypoint[4][1]]
            plt.plot(cara_x,cara_y)
    
            torso_x = [keypoint[6][0],keypoint[12][0],keypoint[11][0],keypoint[5][0]]
            torso_y = [keypoint[6][1],keypoint[12][1],keypoint[11][1],keypoint[5][1]]
            plt.plot(torso_x,torso_y)
    
            piernas_x = [keypoint[16][0],keypoint[14][0],keypoint[12][0],keypoint[11][0],keypoint[13][0],keypoint[15][0]]
            piernas_y = [keypoint[16][1],keypoint[14][1],keypoint[12][1],keypoint[11][1],keypoint[13][1],keypoint[15][1]]
            plt.plot(piernas_x,piernas_y)

            upperbody_x = [keypoint[10][0],keypoint[8][0],keypoint[6][0],keypoint[5][0],keypoint[7][0],keypoint[9][0]]
            upperbody_y = [keypoint[10][1],keypoint[8][1],keypoint[6][1],keypoint[5][1],keypoint[7][1],keypoint[9][1]] 
            plt.plot(upperbody_x,upperbody_y)

print('There are {} ppl in this image'.format(s))
print(id_image)

#print(keypoint)

#for i in range(17):
#    print(i+1,': ',keypoint[i])


plt.show()
