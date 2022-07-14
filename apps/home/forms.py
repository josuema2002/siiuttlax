from django import forms
from .models import electronicDegree, degreeCertificate
from cloudinary.forms import CloudinaryJsFileField

class certificadoTitulacionForm(forms.ModelForm):
    class Meta:
        model = degreeCertificate
        fields = '__all__'
        
class fileUploadForm(forms.ModelForm):
    class Meta:
        model = electronicDegree
        fields = '__all__'