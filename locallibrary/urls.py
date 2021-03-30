

from django.contrib import admin
from django.urls import include
from django.urls import path
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
]

# Use include() to add paths from the catalog application
urlpatterns += [
    path('catalog/', include('catalog.urls')),
]


# Use static() to add url mapping to serve static files during development (only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#Add URL maps to redirect the base URL to our application
urlpatterns += [
    path('', RedirectView.as_view(url='/catalog/', permanent=True)),
]


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]


# Another way to write the above code:
    # urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('catalog/', include('catalog.urls')),
#     path('', RedirectView.as_view(url='catalog/')),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
