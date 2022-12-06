from django.contrib import admin
import images.models as models
from django.utils.html import format_html
from polymorphic.admin import PolymorphicInlineSupportMixin




@admin.register(models.Image)
class ImageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):


    def images(self, objs):
        print(objs)
        html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        return format_html(''.join(html.format(url=objs.image.url)))


    list_display = [field.name for field in models.Image._meta.fields]
    list_filter = [field.name for field in models.Image._meta.fields]
    images.short_description = 'images'

    list_display.append("images")
    readonly_fields = ('images',)