from django.forms import ModelForm, TextInput, Textarea
from .models import *

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #recorro self ya que ahi estan mis componentes
        # for form in self.visible_fields():
        #     #asi le modifico la clase y pues de esa misma forma los demas atributos
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
            #asi puedo modificar varios atributos
            # form.field.widget.attrs.update({'class':'clase','id':'valor','otro-atributo':'valor'})
            #atributos del label
            # form.label_attrs={'class':'clase','for':'id-o-valor'}
        #ya fuera del for, busco mi atributo name y le activo el autofocus con True ya que es un atributo booleano
        # self.fields['name'].widget.attrs['autofocus']=True
    class Meta:
        model = Category
        fields = '__all__'
        #puedo excluir los campos
        #exclude =['atributo']
        labels = {
            #aqui puedo modificar el label que se mostara en el input
            'name': 'Nombre',
            'desc':'Descripción'
        }
        #con este atributo puedo personalizar/modificar mis componentes
        widgets = {
            'name':TextInput( #le digo que va a seguir siendo un input
            #aqui le pongo los atributos que quiera agregarle
            attrs={
            'placeholder':'Ingrese un nombre',
            }
            ),
            'desc':Textarea( #le digo que va a seguir siendo un input
            #aqui le pongo los atributos que quiera agregarle
            attrs={
            'placeholder':'Ingrese una descripción',
            'rows':'3',
            'cols':'3'
            }
            )
        }