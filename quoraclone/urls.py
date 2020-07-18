"""quoraclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path

from django_registration.backends.one_step.views import RegistrationView

from core.views import IndexTemplateView
from users.forms import CustomUserForm

#https://django-registration.readthedocs.io/en/3.0/activation-workflow.html

urlpatterns = [

    # Admin URL
    path('admin/', admin.site.urls),

    #  Register (create new accounts) via browser (Custom version)
    path('accounts/register/',
        RegistrationView.as_view(
            form_class=CustomUserForm,
            success_url='/',
            ), name='django_registration_register'),

    # URL used by Django registration package
    path('accounts/',
        include('django_registration.backends.one_step.urls')),

    # Login URLS used by Django to login user via browser
    path('accounts/',
        include('django.contrib.auth.urls')),

    # Login via browsable API
    path('api-auth/',
        include('rest_framework.urls')),

    # Login via REST
    path('api/rest-auth.',
        include('rest_auth.urls')),

    # Register via REST
    path('api-auth/rest-auth/registration/',
        include('rest_auth.registration.urls')),

    re_path(r"^.*$", IndexTemplateView.as_view(), name='entry-point')
]
