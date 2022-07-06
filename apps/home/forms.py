from django import forms
from .models import tituloElectronico, certificadoTitulacion
from cloudinary.forms import CloudinaryJsFileField

class certificadoTitulacionForm(forms.ModelForm):
    class Meta:
        model = certificadoTitulacion
        fields = '__all__'
        
class fileUploadForm(forms.ModelForm):
    class Meta:
        model = tituloElectronico
        fields = '__all__'