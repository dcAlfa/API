
from django.contrib import admin
from django.urls import path

from Music.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', QoshiqchilarAPIView.as_view(), name="qoshiqchilar"),
    path('qoshiqchi/<int:pk>/', QoshiqchiAPIView.as_view(), name="qoshiqchi"),
    path('qoshiq/', QoshiqAPIView.as_view(), name="qoshiq"),
    path('albom/', AlbomlarAPIView.as_view(), name="albomlar"),
    path('albom/<int:pk>/', AlbomAPIView.as_view(), name="albom"),


]
