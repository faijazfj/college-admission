from django import forms
from .models import *

class Addform(forms.ModelForm):
    class Meta:
        model = Details
        fields = "__all__"


