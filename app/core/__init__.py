
import os

from PIL import Image
import cv2
from tensorflow.keras.models import load_model

import mtcnn

import pandas as pd
import numpy as np

# utils


class Classifier:

    def __init__(self, model_path, images_path) -> None:
        # self.__face_net_model = load_model(model_path)
        self.__images_path = images_path

        self.faces_df = pd.DataFrame(
            columns=['Face_idx', 'image_name', 'fx1', 'fy1','fx2', 'fy2']
        )



    def load_images(self):
        self.image_names = list(os.walk(self.__images_path+'\\imgs'))[0][2]


        print(self.image_names)


    @staticmethod
    def extract_faces_from_img(img, face_detector):
        faces_detected = face_detector.detect_faces(img)

                
        faces = []
        boxes = []
        for face in faces_detected:
            x1, y1, width, height = face['box']

            x1,y1 = abs(x1), abs(y1)
            x2, y2 = x1 + width, y1 + height

            face_detected_img = img[y1:y2, x1:x2]
            
            pil_img = Image.fromarray(face_detected_img)
            resized_img = pil_img.resize((160, 160))

            face_img = np.asarray(resized_img)
            mean, std = face_img.mean(), face_img.std()
            face_img =( face_img - mean)/ std # z Scale

            face_img = np.expand_dims(face_img, axis=0)
            
            faces.append(face_img)
            boxes.append((x1, y1, x2, y1))

            
        return faces, boxes


    def detect_faces(self, f_detector):
        face_count = 0 
        for i, image_name in enumerate(self.image_names):
            img = cv2.imread(self.__images_path+'/imgs/'+image_name) 
            # faces,n,boxes  = extract_faces_from_img(img)
            # print(n, boxes)
            faces, boxes = Classifier.extract_faces_from_img(img, f_detector)
            for j, (face, box) in enumerate(zip(faces, boxes)):
                self.faces_df = self.faces_df.add({
                    'Face_idx': image_name+'__*_'+str(j),
                    'image_name': image_name,
                    'fx1':box[0], 'fy1':box[1],'fx2':box[2], 'fy2':box[3]
                })

            face_count = i
        print('Faces detected', face_count)

        



    def process(self):
        self.load_images()
        self.detect_faces(mtcnn.MTCNN())
