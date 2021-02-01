#! /bin/bash
FILE=$1
DATASET=$FILE
if [ ! -f $FILE ]
then
	echo 'This is not a file'
elif [[ $FILE == *.jpg ]]
then
	echo 'This is jpg file'
	cp $FILE /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	DATASET=${FILE%.*}
	if [ ! -d $DATASET ]
	then
		mkdir $DATASET
		cd $DATASET
		mkdir images
		cd images
		mkdir test2017
		cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	fi
	mv $FILE /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/images/test2017
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	sed s/0001/${DATASET}/ dataset.py>/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/dataset.py
	cp -rf __pycache__ /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}
elif [[ $FILE == *.mp4 ]]
then
	echo 'This is a mp4 video'
	cp $FILE /home/tecnimaq/Vídeos
	cd /home/tecnimaq/Vídeos
	DATASET=${FILE##*/}
	DATASET=${DATASET%.*}
	mkdir ${DATASET}-imagenes 
	ffmpeg -i ${FILE} -qscale:v 2 -vf scale=641:-1 -f image2 ${DATASET}-imagenes/%05d.jpg
	DATASET=${DATASET}-imagenes
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	if [ ! -d $DATASET ]
	then
		echo 'Creating the dataset...'
		mkdir $DATASET
		cd $DATASET
		mkdir images
		cd /home/tecnimaq/Vídeos
	fi
	cp -rf $DATASET /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/images
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/images
	mv $DATASET test2017
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	sed s/0001/${DATASET}/ dataset.py>/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/dataset.py
	cp -rf __pycache__ /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}
else
	echo 'The format of this file is not supported'
fi
if [ -d $FILE ]
then
	DATASET=${FILE##*/}
	echo 'This is a directory'
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	if [ ! -d $DATASET ]
	then
		mkdir $DATASET
		cd $DATASET
		mkdir images
		cd /home/tecnimaq/Gabriela
	fi
	cp -rf $FILE /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/images
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/images
	mv $DATASET test2017
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
	sed s/0001/${DATASET}/ dataset.py>/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/dataset.py
	cp -rf __pycache__ /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}
fi
cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data
if [ ! -d $DATASET ]
then
	echo 'This dataset doesnt exist'
else
	echo 'This is an existing dataset'
	cd $DATASET
	if [ ! -d annotations ]
	then
		mkdir annotations
	fi
	if [ ! -d dets ]
	then
		mkdir dets
	fi
	if [ ! -f dataset.py ]
	then
		cd ..
		echo 'Coping dataset.py...'
		sed s/0001/${DATASET}/ dataset.py>/home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/dataset.py
		cd $DATASET
	fi
	if [ ! -d __pycache__ ]
	then
		cd ..
		echo 'Coping pycache...'
		cp -rf __pycache__ /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}
		cd $DATASET
	fi
	cd /home/tecnimaq/Gabriela/Detectron
	echo 'Using Detectron...'
	python3 tools/infer_simple.py --cfg configs/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml --Dataset_name $DATASET --output-dir /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/Detectron_Output --image-ext jpg --output-ext jpg --wts https://dl.fbaipublicfiles.com/detectron/35861858/12_2017_baselines/e2e_mask_rcnn_R-101-FPN_2x.yaml.02_32_51.SgT4y1cO/output/train/coco_2014_train:coco_2014_valminusminival/generalized_rcnn/model_final.pkl  /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/images/test2017
	cd human_detection/${DATASET}
	cp human_detection.json /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/dets
	cd ../..
	cd image_info/${DATASET}
	cp image_info_test2017.json /home/tecnimaq/Gabriela/TF-SimpleHumanPose/data/${DATASET}/annotations
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/output/model_dump
	if [ ! -d $DATASET ]
	then
		mkdir $DATASET
	fi
	cd MyDataset
	cp snapshot_140.ckpt.data-00000-of-00001 snapshot_140.ckpt.index snapshot_140.ckpt.meta /home/tecnimaq/Gabriela/TF-SimpleHumanPose/output/model_dump/${DATASET}
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/main
	rm config.py
	sed s/0001/${DATASET}/ original_config.py>config.py
	python3 test.py --gpu 0-1 --test_epoch 140 --dataset $DATASET
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/output/result
	if [ ! -d $DATASET ]
	then
		echo 'The result file doesnt exists'
	fi
	cd /home/tecnimaq/Gabriela/TF-SimpleHumanPose/main
	python3 Tf_3.py --result /home/tecnimaq/Gabriela/TF-SimpleHumanPose/output/result/${DATASET}/result.json --dataset $DATASET
fi