from django.urls import path
from wordcount import views

app_name = 'wordcount'

urlpatterns = [
    path('', views.word_count, name='word_count'),
]
