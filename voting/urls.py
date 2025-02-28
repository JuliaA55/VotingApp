"""
URL configuration for voting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from voting_app import views
from django.conf.urls.static import static
from voting import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('voting_app.urls')),
    path("add_candidate/", views.add_candidate_view, name="add_candidate_view"),
    path("vote/", views.vote_view, name="vote"),
    path("get_winner/", views.get_winner_view, name="winner"),
    path("get_balance/", views.get_balance_view, name="balance"),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
