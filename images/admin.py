from django.contrib import admin
import images.models as models
from polymorphic.admin import PolymorphicInlineSupportMixin




@admin.register(models.Image)
class ImageAdmin(PolymorphicInlineSupportMixin, admin.ModelAdmin):
    list_display = [field.name for field in models.Image._meta.fields]
    list_filter = list_display