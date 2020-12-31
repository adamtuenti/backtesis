from animalGalapagos import *
from rest_framework import routers

animalRouter = routers.DefaultRouter()
animalRouter.register(r'animal', AnimalViewSet)