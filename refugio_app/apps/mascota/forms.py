from django import forms

from apps.mascota.models import Mascota


class MascotaForm(forms.ModelForm):
    class Meta:
        model = Mascota
        fields = [
            'nombre',
            'genero',
            'edad',
            'fecha_rescate',
            'persona',
            'vacuna',
        ]
        labels = {
            'nombre': 'Nombre',
            'genero': 'Genero',
            'edad': 'Edad',
            'fecha_rescate': 'Fecha de Rescate',
            'persona': 'Persona',
            'vacuna': 'Vacunas Aplicadas',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'edad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_rescate': forms.DateInput(attrs={'class': 'form-control',}),
            'persona': forms.Select(attrs={'class': 'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }
