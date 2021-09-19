from django.urls import path
from .views import Home_view,model_form_upload,show_upload_view

urlpatterns=[
    path('home/',Home_view,name='home'),
    path('model_form_upload/',model_form_upload,name='model_form_upload'),
    path('show_upload/',show_upload_view,name='show_upload'),

]