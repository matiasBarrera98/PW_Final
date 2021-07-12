from django.forms import ModelForm
from .models import Mascota

class Agregamascota(ModelForm):
    class Meta:
        model = Mascota
        fields = ['idMascota', 'nombre', 'telefonoDuenio', 'idAnimal']