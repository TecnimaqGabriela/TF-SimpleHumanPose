import json
import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io
import os
from os import listdir
from os.path import isdir, isfile
import argparse
import sys

def parse_args():
    parser = argparse.ArgumentParser(description='Arguments for TF Visualizations')
    parser.add_argument(
        '--result',
        dest='result',
        help='result.json made by TF-SimpleHumanPose',
        default=None,
        type=str
    )
    parser.add_argument(
        '--dataset',
        dest='dataset_name',
        help='Dataset name',
        default='COCO',
        type=str
    )
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    return parser.parse_args()

def Visualization_TF(result, dataset_name):

    path='/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/'+dataset_name+'/images/test2017'

    with open(result) as openjason:
        results = json.load(openjason)

    def pose_estimation_image(path_image):

        image = io.imread(path_image)
        heigth, width, deph = image.shape
        plt.imshow(image)
        plt.xticks([])
        plt.yticks([])
        s=0
    
        for obj in range(len(results)):
            image_name = os.path.basename(path_image)
            (im_name,ext) = os.path.splitext(image_name)
            id_image_int = int(im_name)
            image = results[obj].get('image_id')
            
            if image == id_image_int:
                if results[obj].get('score') > 0.4:

                    keypoints_1 = results[obj].get('keypoints')
                    keypoint = []
                    s = s+1
                    plt.xlim(0,width)
                    plt.ylim(heigth,0)
                    right=0
                    for i in range(len(keypoints_1)):
                        
                        if i % 3 == 0:
                            x = keypoints_1[i]
                            y = keypoints_1[i+1]
                            #plt.scatter(x,y)
                            if (right==2) or (right==4) or (right==6) or (right==8) or (right==10) or (right==12) or (right==14) or (right==16):
                                plt.scatter(x,y,c='c')
                            else:
                                plt.scatter(x,y,c='m')
                            keypoint.append((x,y))
                            right=right+1

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

        # print('There are {} ppl in this image'.format(s))

        if not os.path.isdir('/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/'+dataset_name+'/TF_Output'):
            os.mkdir('/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/'+dataset_name+'/TF_Output')
    
        return plt.savefig('/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/'+dataset_name+'/TF_Output/'+im_name+'.png')

    def list_files(givenpath):
        print('Objects in this directory: {}'.format(os.listdir(givenpath)))
        fileshere = []
        for obj in os.listdir(givenpath):
            if os.path.isfile:
                fileshere.append(givenpath + '/' + obj)
        return fileshere

    def pose_estimation_directory(ourpath):

        list_ourfiles = list_files(ourpath)
        number_of_files = len(list_ourfiles)
        print('there are {} files'.format(number_of_files))

        for imageindir in list_ourfiles:
            pose_estimation_image(imageindir)
            plt.clf()


    if os.path.isfile(path):
        pose_estimation_image(path)
    elif os.path.isdir(path):
        pose_estimation_directory(path)
    else:
        print('No se encontró el archivo o el directorio')

args=parse_args()
result_file=args.result
dataset=args.dataset_name
Visualization_TF(result_file,dataset)


