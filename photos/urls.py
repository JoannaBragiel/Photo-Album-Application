from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('photo/<str:pk>/', views.viewPhoto, name='view_photo'),
    path('delete/<str:pk>/', views.delete_photo, name='delete_photo'),
    path('add/', views.addPhoto, name='add_photo'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
