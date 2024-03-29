from django import forms

from .models import Image


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image", "video"]
        widgets = {
            "image": forms.FileInput(attrs={"required": "required"}),
            "video": forms.FileInput(attrs={"required": "required"}),
        }
