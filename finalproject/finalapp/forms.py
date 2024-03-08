from django import forms
from . models import Mypc

class MypcForm(forms.ModelForm):
    class Meta:
        model=Mypc
        fields=['name','desc','img']
