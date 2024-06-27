import os
import sys
from django.core.wsgi import get_wsgi_application


# Ajusta esta ruta según la estructura de tu proyecto
current_path = os.path.abspath(os.path.dirname(__file__))
current_path = current_path[:current_path.find(os.path.dirname(__file__))]
sys.path.append(current_path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "cert3.settings")
application = get_wsgi_application()


import os
import sys
from django.core.wsgi import get_wsgi_application
from PIL import Image
from django.core.files import File
from backend.models import Pokemon




def add_image_manually(pokemon_name, image_path):
    try:
        # Buscar el Pokémon por nombre
        pokemon = Pokemon.objects.get(name=pokemon_name)
        
        # Obtener la ruta absoluta del archivo
        image_path = os.path.abspath(image_path)
        
        # Abrir la imagen desde el archivo
        with open(image_path, 'rb') as f:
            image_data = f.read()  # Leer los datos del archivo
            
            # Utilizar File para guardar la imagen en el campo ImageField
            pokemon.image.save(os.path.basename(image_path), File(f))
            pokemon.save()
            
            print(f"Imagen añadida correctamente para {pokemon_name}")
    except Pokemon.DoesNotExist:
        print(f"No se encontró ningún Pokémon con el nombre {pokemon_name}")
    except Exception as e:
        print(f"Error al añadir la imagen para {pokemon_name}: {str(e)}")

# Ejemplo de uso
if __name__ == "__main__":
    pokemon_name = 'Squirtle'  # Nombre del Pokémon al que deseas añadir la imagen
    image_path = 'media/images/007.png'  # Ruta de la imagen que deseas añadir
    add_image_manually(pokemon_name, image_path)