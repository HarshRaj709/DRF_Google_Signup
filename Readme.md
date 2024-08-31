<h1> What i did to use Googl Authentication Through DRF? <h1>


First you need to create an account on google cloud platform 
    THen create a new project there.
    Then do same process we did in our django authentication project.
    copy client ID, and Secret Key.

Second you need to download some packages.
    <ul>
        <li>pip install django-allauth</li>
        <li>pip install dj-rest-auth</li>
    </ul>

Now you need to add these in your INSTALLED APP sections.

        'django.contrib.sites',
        'dj_rest_auth',
        'rest_framework.authtoken',
        'dj_rest_auth.registration',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',

After that add these Authentication backends.

        AUTHENTICATION_BACKENDS = (
            'django.contrib.auth.backends.ModelBackend',
            'allauth.account.auth_backends.AuthenticationBackend',
        )

And this Middleware in your Middleware sections

        'allauth.account.middleware.AccountMiddleware',


And then This ---

        SITE_ID = 3
        LOGIN_REDIRECT_URL = 'home'
        SOCIALACCOUNT_LOGIN_ON_GET = True


Then PRovide social Accounts settings

        SOCIALACCOUNT_PROVIDERS = {
                'google': {
                'SCOPE': ['profile','email',],
                'AUTH_PARAMS': {
                    'access_type': 'online',
                },
                'OAUTH_PKCE_ENABLED': True,  # Optionally enable PKCE for additional security
                'REDIRECT_URL': None,
            }
            # 'github': {
            #     'SCOPE': ['user', 'repo'],
            #     'VERIFIED_EMAIL': True,
            # }
            }
        
---------------------------------------------------------------------------------------------------------------

Our Settings.py File is Ready now Move to urls.py add some neccessary routes.

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

---------------------------------------------------------------------------------------------------------------

                        After all this make sure to run makemigrations and migrate.

Now open admin pannel of Django App.
    go to sites Table add your local host in both domain name and Display name.

    Now go to social apps.
        Add your Google app there.

        Provider,Name will be Google.
        Then paste your Client ID
        And then Secret Key.
        Then Choose the sites and save.


        ------------------------------------>  All SET  <----------------------------------------
