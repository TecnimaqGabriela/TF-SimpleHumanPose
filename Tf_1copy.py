import json
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
import os
from os import listdir
from os.path import isdir, isfile

with open('/home/tecnimaq/Gabriela/TF-SimpleHumanPose/output/result/COCO/result.json') as openjason:
    results = json.load(openjason)

path = input('Import path  ')

def pose_estimation_image(path):

    #print (results[51])
    #print(results[1].get('keypoints'))
    #print(len(results[1].get('keypoints')))
    
    path_image = path
    id_image =  input('id de la imágen  ')
    id_image_int = int(id_image)
    
    image = io.imread(path_image)
    #image(3) = io.imread("/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/COCO/images/val2017/000000581357.jpg")
    # #image(51) = io.imread("/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/COCO/images/val2017/000000581317.jpg")
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
    #print(id_image)
    #print(keypoint)
     
    #for i in range(17):
    #    print(i+1,': ',keypoint[i])

    return plt.show()

def list_files(givenpath):
    print('Objects in this directory: {}'.format(os.listdir(givenpath)))
    fileshere = []
    for obj in os.listdir(givenpath):
        if os.path.isfile:
            print('{} is a file'.format(obj))
            fileshere.append(givenpath + obj)
    print('From those {} are files'.format(fileshere))
    return fileshere

def pose_estimation_directory(path):

    list_ourfiles = list_files(path)
    print('The list of files here is {}'.format(list_ourfiles))

    for imageindir in list_ourfiles:
        pose_estimation_image(imageindir)


if os.path.isfile(path):
    print('it is an image')
    pose_estimation_image(path)
elif os.path.isdir(path):
    print('it is a directory')
    pose_estimation_directory(path)
else:
    print('file or directory not supported')




