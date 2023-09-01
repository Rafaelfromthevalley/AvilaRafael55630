from django import forms
from .models import CuidadorMascotas, DuenoMascota, Mascota

class CuidadorForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    correo_electronico = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    biografia = forms.CharField(widget=forms.Textarea)
    entrenamiento_cuidado_perros = forms.BooleanField(required=False)

    class Meta:
        model = CuidadorMascotas
        fields = '__all__'

class DuenoForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    correo_electronico = forms.EmailField()
    telefono = forms.CharField(max_length=20)
    direccion = forms.CharField(max_length=200)

    class Meta:
        model = DuenoMascota
        fields = '__all__'

class MascotaForm(forms.ModelForm):
    nombre = forms.CharField(max_length=100)
    dueno = forms.ModelChoiceField(queryset=DuenoMascota.objects.all())
    tipo = forms.ChoiceField(choices=[('canino', 'Canino'), ('felino', 'Felino')])
    raza = forms.CharField(max_length=50)
    edad = forms.IntegerField()

    class Meta:
        model = Mascota
        fields = '__all__'
