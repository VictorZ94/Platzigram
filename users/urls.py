"""Users URLS"""
from django.urls import path

from users import views
from django.views.generic import TemplateView


urlpatterns = [

    # Posts
    path(
        route='profile/<str:username>',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # Management
    path(
        route='users/login/', 
        view=views.login_view,
        name='login'
    ),
    path(
        route='users/logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='users/signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='users/me/profile/', 
        view=views.update_profile,
        name='update'
    )
]
