from django.urls import path
from bangalore.views import *
app_name='something'

urlpatterns = [
    path('microsoft/',microsoft,name='microsoft.html'),
    path('apple/',apple,name='apple.html'),
]
