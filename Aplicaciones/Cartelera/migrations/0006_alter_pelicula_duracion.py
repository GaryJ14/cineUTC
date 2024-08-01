from django.db import migrations, models

def convert_numeric_to_time(apps, schema_editor):
    # Usa el nombre real de tu tabla y columna si son diferentes
    with schema_editor.connection.cursor() as cursor:
        # Primero, convierte la columna a tipo VARCHAR para evitar problemas durante la conversión
        cursor.execute("""
            ALTER TABLE "Cartelera_pelicula"
            ALTER COLUMN "duracion" TYPE VARCHAR(255)
            USING "duracion"::VARCHAR(255)
        """)
        # Luego, convierte la columna a tipo TIME
        cursor.execute("""
            ALTER TABLE "Cartelera_pelicula"
            ALTER COLUMN "duracion" TYPE TIME
            USING "duracion"::TIME
        """)

class Migration(migrations.Migration):

    dependencies = [
        ('Cartelera', '0005_pelicula'),
    ]

    operations = [
        migrations.RunPython(convert_numeric_to_time),
]