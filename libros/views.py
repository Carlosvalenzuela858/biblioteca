from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Libro, Autor, Genero, Calificacion
from .serializers import LibroSerializer, AutorSerializer, GeneroSerializer, CalificacionSerializer

#Libro
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def libro_list_create(request):
    if request.method == 'GET':
        libros = Libro.objects.all()
        serializer = LibroSerializer(libros, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = LibroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def libro_detail(request, pk):
    try:
        libro = Libro.objects.get(pk=pk)
    except Libro.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = LibroSerializer(libro)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = LibroSerializer(libro, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        libro.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#Autor
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def autor_list_create(request):
    if request.method == 'GET':
        autores = Autor.objects.all()
        serializer = AutorSerializer(autores, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = AutorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def autor_detail(request, pk):
    try:
        autor = Autor.objects.get(pk=pk)
    except Autor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = AutorSerializer(autor)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = AutorSerializer(autor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        autor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Genero
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def genero_list_create(request):
    if request.method == 'GET':
        generos = Genero.objects.all()
        serializer = GeneroSerializer(generos, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = GeneroSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def genero_detail(request, pk):
    try:
        genero = Genero.objects.get(pk=pk)
    except Genero.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = GeneroSerializer(genero)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = GeneroSerializer(genero, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        genero.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
#Calificacion
@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def calificacion_list_create(request):
    if request.method == 'GET':
        calificaciones = Calificacion.objects.all()
        serializer = CalificacionSerializer(calificaciones, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CalificacionSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # usuario se asigna en el serializer
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def calificacion_detail(request, pk):
    try:
        calificacion = Calificacion.objects.get(pk=pk)
    except Calificacion.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CalificacionSerializer(calificacion)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Validamos que el usuario autenticado sea el mismo que hizo la calificación
        if calificacion.usuario != request.user:
            return Response({'detail': 'No autorizado para editar esta calificación.'}, status=status.HTTP_403_FORBIDDEN)

        serializer = CalificacionSerializer(calificacion, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()  # mantiene el mismo usuario
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if calificacion.usuario != request.user:
            return Response({'detail': 'No autorizado para eliminar esta calificación.'}, status=status.HTTP_403_FORBIDDEN)
        calificacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)