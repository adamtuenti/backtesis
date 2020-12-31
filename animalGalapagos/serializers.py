from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import AnimalModel

class analizarImagenSerializer(serializers.ModelSerializer):
	#nombreIntegrante = serializers.ReadOnlyField()
	#apellidoIntegrante= serializers.ReadOnlyField()
    imagenAnimal = serializers.SerializerMethodField()
    class Meta:
        model = AnimalModel
        fields = '_all_'

# class AgregarIntegranteSerializer(serializers.ModelSerializer):
# 	nombreIntegrante = serializers.ReadOnlyField()
# 	apellidoIntegrante= serializers.ReadOnlyField()
# 	idUsuario= serializers.ReadOnlyField()
# 	class Meta:
# 		model = Integrante
# 		fields = ('idIntegrante','correoIntegrante','nombreIntegrante','apellidoIntegrante','idUsuario','idEquipo')


# #class EliminarIntegranteEquipoSerializer(serializers.ModelSerializer):
# #	class Meta:
# #		model = Equipo
# #		fields = ('idEquipo','correoIntegrante')

# class MostrarEquipoSerializer(serializers.ModelSerializer):
# 	integrantes = serializers.StringRelatedField(many=True)
# 	class Meta:
# 		model = Equipo
# 		fields = ('idEquipo','Administrador','integrantes')


# class EliminarIntegranteSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model = Integrante
# 		fields = ('correoIntegrante','idEquipo')


# class MostrarIntegrantesSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model=Integrante
# 		fields=('idIntegrante','correoIntegrante','nombreIntegrante','apellidoIntegrante','idUsuario','idEquipo')


# class ActualizarIntegranteSerializer(serializers.ModelSerializer):
# 	class Meta:
# 		model= Integrante
# 		fields=('idUsuario','idEquipo')