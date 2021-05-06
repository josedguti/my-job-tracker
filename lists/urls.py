from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('create/', views.CreateList.as_view(), name='create'),
    # path('<int:pk>/update/', views.UpdateList.as_view(), name='update'),
    # path('<int:pk>/delete/', views.DeleteList.as_view(), name='delete'),
]