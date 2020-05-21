"""rest URL Configuration

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
from django.urls import path, include

urlpatterns = [
    path('api/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('api/user/', include('users.urls')),
    path('api/energytransfers/', include('energytransfers.urls')),
    path('api/invoice/', include('contract.urls')),
    path('api/pay/', include('payments.urls')),
    path('api/bancks/', include('bancks.urls')),
    path('api/commercial/', include('commercial.urls')),
    path('api/reports/', include('reports.urls'))
]
