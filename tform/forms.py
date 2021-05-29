from django import forms

from .models import TForm

class InputFormRevamped(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = TForm
        fields = '__all__'



