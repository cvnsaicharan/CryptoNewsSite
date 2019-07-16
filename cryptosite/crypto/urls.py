from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name="signup"),
    path('prices/', views.prices, name="prices"),
    path('news/', views.news, name="news"),
    path('accounts/', include('django.contrib.auth.urls')),
]

