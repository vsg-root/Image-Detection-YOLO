
"""# Download dos pesos da rede neural pré-treinada"""

!wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.weights

# https://storage.googleapis.com/openimages/web/index.html
# !wget https://pjreddie.com/media/files/yolov3-openimages.weights

"""# Testes com o detector"""

ls

!./darknet detect cfg/yolov4.cfg yolov4.weights data/person.jpg

import cv2
import matplotlib.pyplot as plt
def mostra_deteccao(path):
  imagem = cv2.imread(path)
  figura = plt.gcf()
  figura.set_size_inches(18,10)
  plt.axis('off')
  plt.imshow(cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB))

mostra_deteccao('predictions.jpg')

"""# Darknet e GPU"""

import tensorflow as tf
tf.test.gpu_device_name()

ls

!sed -i 's/OPENCV=0/OPENCV=1/' Makefile
!sed -i 's/GPU=0/GPU=1/' Makefile
!sed -i 's/CUDNN=0/CUDNN=1/' Makefile

!make

!./darknet detect cfg/yolov4.cfg yolov4.weights data/giraffe.jpg

mostra_deteccao('predictions.jpg')

"""# Parâmetro threshold"""

# Coco dataset: https://cocodataset.org/#home

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg

mostra_deteccao('predictions.jpg')

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg -thresh 0.9

mostra_deteccao('predictions.jpg')

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg -thresh 0.98

mostra_deteccao('predictions.jpg')

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg -thresh 0.0001

mostra_deteccao('predictions.jpg')

"""# Parâmetro ext_output"""

!./darknet detect cfg/yolov4.cfg yolov4.weights data/horses.jpg -ext_output

mostra_deteccao('predictions.jpg')

"""# Detecção de objetos em vídeos"""

from google.colab import drive
drive.mount('/content/drive')

ls

!./darknet detector demo cfg/coco.data cfg/yolov4.cfg yolov4.weights -dont_show /content/drive/MyDrive/Cursos\ -\ recursos/Visão\ Computacional\ Guia\ Completo/Videos/video_street.mp4 -i 0 -out_filename /content/drive/MyDrive/Cursos\ -\ recursos/Visão\ Computacional\ Guia\ Completo/Videos/video_street_result.avi

!./darknet detector demo cfg/coco.data cfg/yolov4.cfg yolov4.weights -dont_show /content/drive/MyDrive/Cursos\ -\ recursos/Visão\ Computacional\ Guia\ Completo/Videos/video_people.mp4 -i 0 -out_filename /content/drive/MyDrive/Cursos\ -\ recursos/Visão\ Computacional\ Guia\ Completo/Videos/video_people_result.avi
