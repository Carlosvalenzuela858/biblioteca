# Api Rest Biblioteca - Carlos Valenzuela
## Versiones de las Herramientas Utilizadas
```text
Package                       Version
----------------------------- -----------
asgiref                       3.8.1
contourpy                     1.3.2
cycler                        0.12.1
Django                        5.2.3
djangorestframework           3.16.0
djangorestframework_simplejwt 5.5.0
fonttools                     4.58.4
kiwisolver                    1.4.8
matplotlib                    3.10.3
numpy                         2.3.1
packaging                     25.0
pandas                        2.3.0
pillow                        11.3.0
pip                           24.3.1
pip-licenses                  5.0.0
prettytable                   3.16.0
psycopg2-binary               2.9.10
PyJWT                         2.9.0
pyparsing                     3.2.3
python-dateutil               2.9.0.post0
pytz                          2025.2
seaborn                       0.13.2
six                           1.17.0
sqlparse                      0.5.3
tomli                         2.2.1
tzdata                        2025.2
wcwidth                       0.2.13
```

## Instalar Python
Asegurate de tener Python instalado. Recomendado: Python 3.10 o superior
Podés verificarlo con:
```bash
python --version
```
## Crear un entorno virtual
Desde la raíz del proyecto:

```bash
python -m venv venv
```
Activar el entorno:

Windows:
```bash
venv\Scripts\activate
```
Linux/Mac:
```bash
source venv/bin/activate
```

## Instalar Django y otras dependencias
Con el entorno virtual activado, ejecutá:
```bash
pip install django djangorestframework djangorestframework-simplejwt psycopg2-binary matplotlib seaborn pandas
```
O desde un archivo requirements.txt:
```bash
pip install -r requirements.txt
```

## Crear un nuevo proyecto Django
```bash
django-admin startproject biblioteca
cd biblioteca
python manage.py startapp libros
```

## Crear la base de datos
En PGAdmin crear la base de datos Biblioteca y se configura la conexion a la base de datos:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'biblioteca',
        'USER': 'postgres',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
# ¿Cómo funciona la aplicación?
La aplicación Biblioteca es una API RESTful que permite a los usuarios gestionar libros, autores y géneros, así como calificar libros y analizar los datos registrados. Está construida con Django y Django REST Framework, utilizando autenticación basada en JWT.

🧩 Componentes principales:
Usuarios registrados pueden:

- Autenticarse (login/registro).
- Calificar libros (una sola vez por libro).
- Consultar libros, autores y géneros.

API protegida: los endpoints principales requieren autenticación JWT para acceder.

📊 Funciones adicionales:
- Generación de reportes gráficos sobre calificaciones, tendencias de lectura y actividad de usuarios usando pandas, seaborn y matplotlib.
- Recomendación interna de libros: por medio de un comando de consola, se pueden listar los libros mejor calificados por género.

## Prueba de la aplicacion
Flujo de uso básico:
- El usuario se registra (/app/registrarse/) e inicia sesión (/app/iniciarsesion/).
- Obtiene un token JWT para autenticarse.
Usa ese token para:
- Consultar libros (GET /app/libros/)
- Calificar un libro (POST /app/calificaciones/)
- Ver calificaciones propias o generales
Desde consola, el administrador puede:
- Generar gráficos: python manage.py reportes
- Obtener recomendaciones: python manage.py libros_por_genero

## Postman
### Registrarse
```http
POST http://127.0.0.1:8000/app/registrarse/
```
Json:
```json
{
  "username": "carlosvalenzuela",
  "email": "Carloavalenzuela@gmail.com",
  "password": "1234"
}
```
![Image](https://github.com/user-attachments/assets/9a66e296-ab94-4083-a883-281ce2631021)

## Iniciar Sesion
```http
POST http://127.0.0.1:8000/app/iniciarsesion/
```
Json:
```json
{
  "username": "carlosvalenzuela",
  "password": "1234"
}
```
![Image](https://github.com/user-attachments/assets/287e0c05-58de-4ca1-a32f-618c520f3c30)

## Libros
### Listar Todos los Libros
```http
GET http://127.0.0.1:8000/app/libros/
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![Image](https://github.com/user-attachments/assets/5ecfbbe7-7772-4c19-bfac-a5ef6b1471ff)

### Obtener por ID
```http
GET http://127.0.0.1:8000/app/libros/1/
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![Image](https://github.com/user-attachments/assets/09635cf6-c552-486b-a4e1-0d3b2d60e24a)

### Insertar
```http
POST http://127.0.0.1:8000/app/libros/
```
Json:
```json
{
  "nombre": "La invención de Morel",
  "autor": 6,
  "genero": 1,
  "lanzamiento": "1940-01-01",
  "isbn": "9789871138766",
  "url_libro": "http://libros.com/La_invencionn_de_Morel"
}
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![Image](https://github.com/user-attachments/assets/c16df321-e11c-431f-a9d0-96e84c11f763)

### Actualizar
```http
PUT http://127.0.0.1:8000/app/libros/31/
```
Se pasa el ID del libro en la URL.
Json:
```json
{
  "nombre": "Ficciones",
  "autor": 6,
  "genero": 3,
  "lanzamiento": "1944-01-01",
  "isbn": "9788491050084",
  "url_libro": "https://libro.com/Ficciones"
}
```
Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![Image](https://github.com/user-attachments/assets/b17d7d48-d5b6-4847-bfba-efafc96b3437)

### Eliminar
```http
DELETE http://127.0.0.1:8000/app/libros/31/
```
Se pasa el ID del libro en la URL.

Para acceder a los endpoints protegidos, enviá el token en el header:
```bash
Authorization: Bearer <token>
```
![Image](https://github.com/user-attachments/assets/4706254c-6446-437e-b2bf-2de44561f1da)

## Codigo del View:
Codigo para Listar todos y Insertar:
```python
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
```

Codigo para obtener por id, actualizar y eliminar.
```python
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
```

# Reportes gráficos automáticos
La aplicación incluye un comando personalizado para generar 10 reportes gráficos sobre libros, calificaciones, géneros y usuarios, utilizando Pandas, Seaborn y Matplotlib.

Cómo ejecutar el script
Desde la terminal, ejecutar:
```bash
python manage.py reportes
```
Esto generará las gráficas en formato .png dentro de una carpeta reportes/ en la raíz del proyecto.

## Reportes generados
### Calificación promedio por libro
Archivo: 1_calificacion_promedio_por_libro.png

Descripción: Muestra el promedio de calificaciones de cada libro con al menos una calificación. Ideal para analizar la recepción general de cada obra.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/8f50018b-3d55-4471-8e57-84d81a5ed2fd)

### Libros por género
Archivo: 2_libros_por_genero.png

Descripción: Representa la cantidad total de libros agrupados por género. Útil para ver qué géneros dominan la colección.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/b5d93f34-71bc-4cff-89cd-c840c54cb5e9)

### Libros con más calificaciones
Archivo: 3_libros_con_mas_calificaciones.png

Descripción: Lista los libros que han recibido más calificaciones. Refleja la popularidad o nivel de interacción de cada obra.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/97834ecc-dfca-47f2-ac3c-4a5475101813)

### Calificación promedio por género
Archivo: 4_calificacion_promedio_genero.png

Descripción: Calcula el promedio general de las calificaciones de libros por género. Ayuda a ver qué géneros son mejor valorados.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/e7ef914f-342b-4813-95bc-f7d97dde95d1)

### Usuarios con más calificaciones
Archivo: 5_usuarios_con_mas_calificaciones.png

Descripción: Muestra los usuarios que han calificado más libros. Permite identificar a los usuarios más activos.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/041acd02-7436-42ff-85aa-3666ad139ac7)

### Distribución de calificaciones
Archivo: 6_distribucion_calificaciones.png

Descripción: Histograma que muestra cómo se distribuyen las calificaciones (bajas, medias, altas).

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/63a1299c-884c-4192-ba79-4700e9436595)

### Promedio por año de publicación
Archivo: 7_promedio_por_año.png

Descripción: Muestra cómo varía el promedio de calificaciones según el año de lanzamiento de los libros.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/eb5f2d53-39ca-4733-beee-3996ee17a0ec)

### Libros por autor
Archivo: 8_libros_por_autor.png

Descripción: Muestra cuántos libros ha publicado cada autor registrado.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/671c4ec8-9008-45a4-9433-bf31e559910d)

### Top 5 libros mejor calificados
Archivo: 9_top5_libros.png

Descripción: Muestra los 5 libros mejor valorados que tienen al menos 3 calificaciones.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/0e73c1c4-42a5-4e1b-85ae-85b9e7fb1ab2)

### Boxplot de calificaciones por género
Archivo: 10_boxplot_genero.png

Descripción: Gráfico tipo caja (boxplot) que representa la dispersión y valores extremos de las calificaciones según el género.

Ejemplo visual:
![Image](https://github.com/user-attachments/assets/d60d965c-8fba-4f79-8dd1-eb10ad5ff9c2)


## Recomendaciones por Género
Este proyecto incluye un comando personalizado que permite obtener una lista de los 10 libros mejor calificados dentro de un género específico.

### Archivo
```bash
libros/management/commands/libros_por_genero.py
```

### ¿Qué hace este script?
- Solicita al usuario un ID de género por consola.
- Filtra los libros que pertenecen a ese género.
- Calcula el promedio de calificaciones de cada libro.
- Ordena los libros de mayor a menor según ese promedio.
- Muestra en consola los 10 libros con mejor valoración.

### Ejecución
Para ejecutarlo, usá el siguiente comando:
```bash
python manage.py libros_por_genero
```
Luego, el sistema te pedirá que ingreses un ID de género:
```bash
📥 Ingrese el ID del género: 3
```
Y el resultado se verá así:

![Image](https://github.com/user-attachments/assets/e1918c98-d6b0-4960-abce-6c009d93553c)

### Validaciones
Si se ingresa un ID que no es un número, muestra un error.

Si no se encuentran libros para ese género, informa al usuario con una advertencia.

# Licencia
Este proyecto está licenciado bajo los términos de la Licencia MIT.

### Licencias de terceros
Este proyecto utiliza varias bibliotecas de terceros. A continuación, se listan junto con sus respectivas licencias:
```html
 Name                           Version      License
 Django                         5.2.3        BSD License
 PyJWT                          2.9.0        MIT License
 asgiref                        3.8.1        BSD License
 contourpy                      1.3.2        BSD License
 cycler                         0.12.1       BSD License
 djangorestframework            3.16.0       BSD License
 fonttools                      4.58.4       MIT
 kiwisolver                     1.4.8        BSD License
 matplotlib                     3.10.3       Python Software Foundation License
 numpy                          2.3.1        BSD License
 packaging                      25.0         Apache Software License; BSD License
 pandas                         2.3.0        BSD License
 pillow                         11.3.0       UNKNOWN
 psycopg2-binary                2.9.10       GNU Library or Lesser General Public License (LGPL)
 pyparsing                      3.2.3        MIT License
 python-dateutil                2.9.0.post0  Apache Software License; BSD License
 pytz                           2025.2       MIT License
 seaborn                        0.13.2       BSD License
 six                            1.17.0       MIT License
 sqlparse                       0.5.3        BSD License
 tzdata                         2025.2       Apache Software License
```
