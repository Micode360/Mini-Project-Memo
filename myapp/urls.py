from django.urls import path
from myapp import views

urlpatterns = [
    path('route', views.home, name='route'),
    path('message', views.message_func, name='message'),
    path('details/<int:pk>/', views.details_func, name="details")
]
