from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import AnimalModel
from .serializers import analizarImagenSerializer
from django.http import HttpResponse
from rest_framework.response import Response



import matplotlib
import numpy as np
#import matplotlib.pyplot as plt
import keras
from PIL import Image
import os
import cv2
    
class Animal(APIView):

    def prepare(filepath):
        IMG_SIZE = 224
        img_array = cv2.imread(filepath,cv2.IMREAD_COLOR)
        new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
        return new_array.reshape(-1,IMG_SIZE,IMG_SIZE, 3)

    def post(self, request, *args, **kwargs):
        

        #serializer_class = analizarImagenSerializer
       
        #serializer = analizarImagenSerializer(data=request.data)
        imagenAnimal = request.data.get('idAnimal')

        modelo = keras.models.load_model('./modelo/my_model.h5')

        
        filepath = "./AnimalImagenes/images_40.jpg"
        IMG_SIZE = 224
        img_array = cv2.imread(filepath,cv2.IMREAD_COLOR)
        new_array = cv2.resize(img_array,(IMG_SIZE,IMG_SIZE))
        img = new_array.reshape(-1,IMG_SIZE,IMG_SIZE, 3)

        #test_image = prepare("./AnimalImagenes/images_40.jpg") #plt.imread('./AnimalImagenes/images_40.jpg')

        prediction = modelo.predict(img)
        ind_max = prediction.argmax(axis=1)[0]
        print('indice: ',ind_max)
        # test_image = Image.fromarray(test_image, 'RGB')
        # test_image = test_image.resize((28, 21))


        # test_image = np.array(test_image, dtype=np.uint8)
        # test_image = test_image / 255.0

        # img = (np.expand_dims(test_image,0))
        # predictions_single = modelo.predict(img)

        # indice = np.argmax(predictions_single[0])
        # print(indice)


        
        # print(imagenAnimal)
        idA = 0
        datos = AnimalModel.objects.filter(idAnimal=idA)
        print(datos[0].idAnimal,datos[0].nombreAnimal)

        salida = {'nombrnimal':datos[0].nombreAnimal,'nombreTecnico':datos[0].nombreTecnico}#,'imagenAnimal':datos[0].imagenAnimal}
        return Response(data=salida)

    
    def funcion(imagen):
        return ['hola']

    

    
    
# class DetalleAnimal(RetrieveAPIView):
#     serializer_class = analizarImagenSerializer
#     queryset = AnimalModel.objects.all()



            