from django.urls import path, include
from allauth.socialaccount.providers.google import views as google_views
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/registration/', include('dj_rest_auth.registration.urls')),
    path('api/auth/social/', include('allauth.socialaccount.urls')),
    path('api/auth/social/login/google/', google_views.oauth2_login, name='google_login'),
    path('api/auth/social/login/google/callback/', google_views.oauth2_callback, name='google_callback'),
    # path('home/',views.home,name='home'),
    path('logout/',views.logout_user,name='logout'),

]
