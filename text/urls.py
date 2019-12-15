from django.urls import path
from .views import image_view, success, show_extract_text

urlpatterns = [
    path('', image_view, name='image_upload'),
    path('success', success, name='success'),
    path('text', show_extract_text, name='text')
]
