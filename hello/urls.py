
from django.urls import path
from hello import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
]