from django.forms import *
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
    #puedo hacer lo que hice en la vista, aqui tambien en la funcion save()
    def save(self,commit=True):
        data = {}
        form = super() #obtengo el formulario
        try:
            if form.is_valid():
                form.save()
            else:
                #si hay errores, creo la clave error
                data['error']=form.errors
        except Exception as e:
            #por si pasa algun otro error
            data['errors']=str(e)
        return data
    
    def clean(self):
        cleaned = super().clean() #retorna el formulario con los datos y asi podemos hacer verificaciones
        #if len(cleaned['name']) <= 50: #en el cleaned en forma de diccionario
            #raise forms.ValidationError('Validation xxx') #aqui le mando un error que no tiene nada que ver con mis componentes y lo hago con la palabra reservada raise que es para generar ua excepcion manualmente
        
            # y con la funcion add_error agrego el error a ese componente que estoy verificando, el primer parametro es el componente o input y el segundo el mensaje
            #self.add_error('name','Le faltan caracteres')
            #eso se agrega en el form.errors que verifico en el html y recorro

        return cleaned
