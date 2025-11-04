from django.urls import path
from .views import home_view, upload_image_view
from django.views.generic import TemplateView

urlpatterns = [
    path('', home_view, name='home'),
    path('upload/', upload_image_view, name='upload_image'),
    path('upload/success/', TemplateView.as_view(template_name='upload_success.html'), name='upload_success'),
]