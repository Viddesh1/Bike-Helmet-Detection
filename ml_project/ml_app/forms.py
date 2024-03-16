from django import forms
from . models import Image

# TODO: Add validations to the form data and test case for it.
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image', 'video']