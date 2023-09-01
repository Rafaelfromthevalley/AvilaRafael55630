from .models import CuidadorMascotas

def buscar_cuidador_por_nombre(nombre):
    """
    Busca cuidadores de mascotas por nombre.
    
    Args:
        nombre (str): El nombre del cuidador a buscar.

    Returns:
        QuerySet: Un conjunto de consultas que coincide con el nombre proporcionado.
    """
    return CuidadorMascotas.objects.filter(nombre__icontains=nombre)
