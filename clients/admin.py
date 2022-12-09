from django.contrib import admin
import clients.models as models
from django.utils.html import format_html
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

@admin.register(models.ClientsImage)
class ClientsImageAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.ClientsImage._meta.fields]
    list_filter = list_display

@admin.register(models.Clients)
class ClientsAdmin(admin.ModelAdmin):

    def images(self, objs):
        html = '<a href="{url}" target="_blank"><img src="{url}" style="width: auto;height: 50px;" /></a>'
        return format_html(''.join(html.format(url=objs.client_image.image.url)))

    images.short_description = 'images'


    list_display = [field.name for field in models.Clients._meta.fields]
    list_filter = [field.name for field in models.Clients._meta.fields]
    list_display.append("images")


