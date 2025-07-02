from rest_framework import serializers
from .models import Libro, Autor, Genero, Calificacion


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'
        
class AutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Autor
        fields = '__all__'
        
class LibroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Libro
        fields = '__all__'
        
class CalificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calificacion
        fields = ['id', 'libro', 'calificacion'] 

    def validate_calificacion(self, value):
        if not 0.0 <= value <= 5.0:
            raise serializers.ValidationError("La calificación debe estar entre 0.0 y 5.0.")
        return value

    def create(self, validated_data):
        validated_data['usuario'] = self.context['request'].user
        return super().create(validated_data)
