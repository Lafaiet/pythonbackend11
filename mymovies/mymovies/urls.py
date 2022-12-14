"""mymovies URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import settings

from viewer.views import (
    hello,
    luck_number,
    favorite_pet,
    pet_names,
    home_page,
    MoviesList,
    MovieDetail,
    MovieCreate,
    MovieUpdate,
    MovieDelete,
    HomePage,
    Contact,
    SignUpView
)


urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('luck/', luck_number),
    path('pet/', favorite_pet),
    path('pet_names/<pet_type>', pet_names),
    path('movies/', MoviesList.as_view(), name='movies_list'),
    path('movies/<int:pk>', MovieDetail.as_view(), name='movie_detail'),
    path('create_movie', MovieCreate.as_view(), name='create_movie'),
    path('movies/<int:pk>/update', MovieUpdate.as_view(), name='movie_update'),
    path('movies/<int:pk>/delete', MovieDelete.as_view(), name='movie_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('contact/', Contact.as_view(), name='contact'),
    path('signup/', SignUpView.as_view(), name='signup')
]

if settings.DEBUG:

    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MERIA_ROOT

    )

