from django.urls import path
from dogs.views import index, DogListView, CategoryListView, DogCreateView, DogUpdateView, DogDeleteView

from dogs.apps import DogsConfig

app_name = DogsConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('<int:pk>/dogs/', DogListView.as_view(), name='category'),
    path('dogs/create/', DogCreateView.as_view(), name='dog_create'),
    path('dogs/update/<int:pk>/', DogUpdateView.as_view(), name='dog_update'),
    path('dogs/delete/<int:pk>/', DogDeleteView.as_view(), name='dog_delete'),
]