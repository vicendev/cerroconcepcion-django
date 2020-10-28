from django import forms
from .models import Business, Structure, EstateImages, Estate
from phonenumber_field.formfields import PhoneNumberField

from django.contrib.auth.models import User


#class CoverImageWidget(forms.widgets.Widget):
#    def render(self, name, value, attrs=None):
#        html = Template("""<img src="$link"/>""")
#        return mark_safe(html.substitute(link=value))

class EstateForm(forms.ModelForm):

    title = forms.CharField(label='Título', required=True, widget=forms.TextInput(
        attrs={'class':'form-control', 'placeholder':'Escribe un título'}
    ), min_length=10, max_length=100)
    content = forms.CharField(label='Contenido', required=True, widget=forms.Textarea(
        attrs={'class':'form-control', 'placeholder':'Escribe tu contenido'}
    ), min_length=10, max_length=1000)
    price = forms.IntegerField(label='Precio', required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Escribe un precio'}
    ))
    room = forms.IntegerField(label='Habitaciones', required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Habitaciones', 'size':'30'}
    ))
    bathroom = forms.IntegerField(label="Baños", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Baños', 'size':'10'}
    ))
    area = forms.IntegerField(label="Area", required=True, widget=forms.NumberInput(
        attrs={'class':'form-control', 'placeholder':'Superficie', 'size':'20'}
    ))
    phone_number = PhoneNumberField(label="Número Teléfono", required=False, widget=forms.TextInput(
        attrs={'placeholder':'Número de Teléfono'}
    ))
    business = forms.ModelChoiceField(queryset=Business.objects.all() , label="Negocio", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Negocio'}
    ))
    structure = forms.ModelChoiceField(queryset=Structure.objects.all(), label="Estructura", required=True, widget=forms.Select(
        attrs={'class':'form-control', 'placeholder':'Estructura'}
    ))
    image_cover = forms.ImageField(label='Foto Portada', required=False)

    class Meta:
        model = Estate
        fields = ['title','content','price','room','bathroom','area','phone_number','business','structure','image_cover']

class ImageForm(forms.ModelForm):
    file = forms.ImageField(label='', required=False, widget=forms.FileInput({'multiple':True}))
    
    class Meta:
        model = EstateImages
        fields = ('file',)