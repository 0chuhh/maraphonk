from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import MyLoginView, CustomLoginView, SignUp

urlpatterns = [
    path('login/', CustomLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("registration/<str:role>/", SignUp.as_view(), name="registration"),
]