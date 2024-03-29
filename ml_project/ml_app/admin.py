from django.contrib import admin
from django.utils.html import format_html

from .models import Image, PredImage

# Register your models here.


class ImageAdmin(admin.ModelAdmin):
    list_display = ("id", "image", "video")

    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" height="50" />', obj.image.url)
        else:
            return "No Image"

    display_image.short_description = "Image"

    def display_video(self, obj):
        if obj.video:
            return format_html(
                '<video width="50" height="50" controls><source src="{}" type="video/mp4"></video>',
                obj.video.url,
            )
        else:
            return "No Video"

    display_video.short_description = "Video"


admin.site.register(Image, ImageAdmin)


class PredImageAdmin(admin.ModelAdmin):
    list_display = ("pred_image_id", "pred_image", "pred_video")

    def display_image(self, obj):
        if obj.pred_image:
            return format_html('<img src="{}" height="50" />', obj.pred_image.url)
        else:
            return "No predicted Image"

    display_image.short_description = "Predicted Image"

    def display_video(self, obj):
        if obj.pred_video:
            return format_html(
                '<video width="50" height="50" controls><source src="{}" type="video/mp4"></video>',
                obj.pred_video.url,
            )
        else:
            return "No predicted Video"

    display_video.short_description = "Predicted Video"


admin.site.register(PredImage, PredImageAdmin)
