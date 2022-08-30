from django import forms

from .models import Enviar_Email_to

class Envio_de_Email (forms.ModelForm):
    class Meta:
        model = Enviar_Email_to
        fields = ["asunto","email","mensaje"]