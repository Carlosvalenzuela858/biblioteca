from django.core.management.base import BaseCommand
from libros.models import Libro
from django.db.models import Avg

class Command(BaseCommand):
    help = 'Recomienda los libros mejor calificados por género (interactivo)'

    def handle(self, *args, **kwargs):
        genero_id = input("📥 Ingrese el ID del género: ")

        if not genero_id.isdigit():
            self.stdout.write(self.style.ERROR("❌ El ID del género debe ser un número entero."))
            return

        genero_id = int(genero_id)

        libros = (
            Libro.objects.filter(genero_id=genero_id)
            .annotate(promedio=Avg('calificaciones__calificacion'))
            .order_by('-promedio')[:10]
        )

        if not libros:
            self.stdout.write(self.style.WARNING("⚠️  No se encontraron libros para ese género."))
            return

        self.stdout.write(self.style.SUCCESS(f"\n📚 Top 10 libros mejor valorados del género {genero_id}:\n"))

        for libro in libros:
            promedio = round(libro.promedio or 0, 2)
            self.stdout.write(f"✅ {libro.nombre} — Promedio: {promedio}")
