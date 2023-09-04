from django import forms
from .models import CuidadorMascotas, DuenoMascota, Mascota
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation

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


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=30, required=True, help_text="Introduce tu primer nombre.")
    last_name = forms.CharField(max_length=30, required=True, help_text="Introduce tu apellido.")

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')

        # Por ejemplo, asegurarse de que la contraseña tenga al menos 8 caracteres
        if len(password1) < 8:
            raise forms.ValidationError("La contraseña debe tener al menos 8 caracteres.")

        # Aplica las validaciones estándar de Django
        try:
            password_validation.validate_password(password1, self.instance)
        except forms.ValidationError as error:
            self.add_error('password1', error)

        return password1

class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email de Usuario")
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirmar Contraseña", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Nombre/s", max_length=50, required=False)   
    last_name = forms.CharField(label="Apellido/s", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']