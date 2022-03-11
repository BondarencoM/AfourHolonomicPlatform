from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('arbitraryMove', views.arbitraryMove, name='index', ),
    path('presetMove', views.presetMove, name='index', ),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    