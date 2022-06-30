from django import forms
from .models import tituloElectronico
from cloudinary.forms import CloudinaryJsFileField

# class FormularioCertificado(forms.Form):

#     plan_estudios = forms.IntegerField(required=True, min_value=1900, max_value=3000)
#     periodo_escolar_init = forms.CharField(required=True, max_length=10)
#     periodo_escolar_end = forms.CharField(required=True, max_length=10)
#     check = forms.BooleanField(required=True)

class fileUploadForm(forms.ModelForm):
    class Meta:
        model = tituloElectronico
        fields = '__all__'