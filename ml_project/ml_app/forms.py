from django import forms

from .models import Image


class ImageForm(forms.ModelForm):
    """
    Form for uploading an image and a video.

    Meta:
    - model: Image, the model associated with the form.
    - fields: List of fields from the model to include in the form.
    - widgets: Dictionary mapping field names to widget instances for customization.

    Attributes of Meta class:
    - model = Image instance of class Image
    - fields:
        - image: FileField, for uploading an image file.
        - video: FileField, for uploading a video file.
    - widgets:
        - image: image field is required in user interface.
        - video: video field is required in user interface.
    """
    class Meta:
        model = Image
        fields = ["image", "video"]
        widgets = {
            "image": forms.FileInput(attrs={"required": "required"}),
            "video": forms.FileInput(attrs={"required": "required"}),
        }
