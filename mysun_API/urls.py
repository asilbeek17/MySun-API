from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
   openapi.Info(
      title="mysun API",
      default_version='v1',
      description="API for mysun template",
      terms_of_service="https://bicycle.pythonanywhere.com/",
      contact=openapi.Contact(email="asilbek1721@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('api-auth/', include('rest_framework.urls')),
]