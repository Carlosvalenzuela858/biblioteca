from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from libros.models import Libro, Autor, Genero, Calificacion
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from django.db import models


class Command(BaseCommand):
    help = 'Genera 10 reportes con gráficos basados en los datos'

    def handle(self, *args, **kwargs):
        os.makedirs('reportes', exist_ok=True)

        # Reporte 1: Calificaciones promedio por libro
        libros = Libro.objects.all()
        data = []
        for libro in libros:
            calificaciones = libro.calificaciones.all()
            if calificaciones.exists():
                promedio = calificaciones.aggregate(avg=models.Avg('calificacion'))['avg']
                data.append({'libro': libro.nombre, 'promedio': promedio})
        df = pd.DataFrame(data)
        plt.figure(figsize=(22, 8))
        sns.barplot(data=df, x='promedio', y='libro')
        plt.title('Promedio de calificaciones por libro')
        plt.savefig('reportes/1_calificacion_promedio_por_libro.png')
        plt.close()

        # Reporte 2: Cantidad de libros por género
        df = pd.DataFrame(
            Libro.objects.values('genero__nombre').annotate(total=models.Count('id'))
        )
        plt.figure(figsize=(8, 6))
        sns.barplot(data=df, x='total', y='genero__nombre')
        plt.title('Cantidad de libros por género')
        plt.savefig('reportes/2_libros_por_genero.png')
        plt.close()

        # Reporte 3: Libros con más calificaciones
        df = pd.DataFrame(
            Libro.objects.annotate(cant=models.Count('calificaciones')).values('nombre', 'cant')
        )
        plt.figure(figsize=(22, 8))
        sns.barplot(data=df, x='cant', y='nombre')
        plt.title('Libros con más calificaciones')
        plt.savefig('reportes/3_libros_con_mas_calificaciones.png')
        plt.close()

        # Reporte 4: Calificaciones promedio por género
        data = []
        for genero in Genero.objects.all():
            libros = genero.libros.all()
            ratings = []
            for libro in libros:
                ratings += list(libro.calificaciones.values_list('calificacion', flat=True))
            if ratings:
                data.append({'genero': genero.nombre, 'promedio': sum(ratings) / len(ratings)})
        df = pd.DataFrame(data)
        plt.figure(figsize=(8, 6))
        sns.barplot(data=df, x='promedio', y='genero')
        plt.title('Calificaciones promedio por género')
        plt.savefig('reportes/4_calificacion_promedio_genero.png')
        plt.close()

        # Reporte 5: Usuarios que más califican
        df = pd.DataFrame(
            User.objects.annotate(cant=models.Count('calificaciones')).values('username', 'cant')
        )
        plt.figure(figsize=(18, 8))
        sns.barplot(data=df, x='cant', y='username')
        plt.title('Usuarios con más calificaciones')
        plt.savefig('reportes/5_usuarios_con_mas_calificaciones.png')
        plt.close()

        # Reporte 6: Distribución de calificaciones (histograma)
        calificaciones = Calificacion.objects.values_list('calificacion', flat=True)
        df = pd.DataFrame(calificaciones, columns=['calificacion'])
        plt.figure(figsize=(6, 4))
        sns.histplot(df['calificacion'], bins=10, kde=True)
        plt.title('Distribución de calificaciones')
        plt.savefig('reportes/6_distribucion_calificaciones.png')
        plt.close()

        # Reporte 7: Calificaciones por año de lanzamiento
        data = []
        for libro in Libro.objects.all():
            if libro.calificaciones.exists():
                promedio = libro.calificaciones.aggregate(avg=models.Avg('calificacion'))['avg']
                data.append({'año': libro.lanzamiento.year, 'promedio': promedio})
        df = pd.DataFrame(data)
        plt.figure(figsize=(12, 6))
        sns.lineplot(data=df.groupby('año')['promedio'].mean().reset_index(), x='año', y='promedio')
        plt.title('Calificación promedio por año de lanzamiento')
        plt.savefig('reportes/7_promedio_por_año.png')
        plt.close()

        # Reporte 8: Libros por autor
        df = pd.DataFrame(
            Autor.objects.annotate(total=models.Count('libros')).values('nombre', 'total')
        )
        plt.figure(figsize=(20, 8))
        sns.barplot(data=df, x='total', y='nombre')
        plt.title('Cantidad de libros por autor')
        plt.savefig('reportes/8_libros_por_autor.png')
        plt.close()

        # Reporte 9: Top 5 libros mejor calificados (mínimo 3 calificaciones)
        data = []
        for libro in Libro.objects.all():
            calificaciones = libro.calificaciones.all()
            if calificaciones.count() >= 3:
                promedio = calificaciones.aggregate(avg=models.Avg('calificacion'))['avg']
                data.append({'libro': libro.nombre, 'promedio': promedio})
        df = pd.DataFrame(data).sort_values(by='promedio', ascending=False).head(5)
        plt.figure(figsize=(22, 6))
        sns.barplot(data=df, x='promedio', y='libro')
        plt.title('Top 5 libros mejor calificados (3+ ratings)')
        plt.savefig('reportes/9_top5_libros.png')
        plt.close()

        # Reporte 10: Boxplot de calificaciones por género
        data = []
        for genero in Genero.objects.all():
            for libro in genero.libros.all():
                for cal in libro.calificaciones.all():
                    data.append({'genero': genero.nombre, 'calificacion': cal.calificacion})
        df = pd.DataFrame(data)
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='genero', y='calificacion')
        plt.title('Boxplot de calificaciones por género')
        plt.savefig('reportes/10_boxplot_genero.png')
        plt.close()

        self.stdout.write(self.style.SUCCESS('✅ ¡10 reportes generados en la carpeta "reportes"!'))
