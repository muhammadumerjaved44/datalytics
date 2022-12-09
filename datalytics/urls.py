from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view


schema_view =  swagger_get_schema_view(
    openapi.Info(
        title="My POD API",
        default_version="0.0.0",
        description="myPod API "
    ),
    public=True
)


# customizing admin panel
admin.site.site_header = "Datalytics Admin Portal"
admin.site.site_title = "Datalytics Admin Portal"
admin.site.index_title = "Welcome to Datalytics  Portal"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("websites.urls")),
    path("", include("courses.urls")),
    path("", include("events.urls")),
    path("", include("clients.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
