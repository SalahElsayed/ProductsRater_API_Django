
from django.contrib import admin
from django.urls.conf import path, include
from rest_framework.authtoken.views import obtain_auth_token
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Product Rater API",
      default_version='v1',
      contact=openapi.Contact(email="salahelsayed995@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('token_request/', obtain_auth_token),
    path('', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
