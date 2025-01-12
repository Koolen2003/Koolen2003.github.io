"""
URL configuration for registration project.

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
from django.urls import path , include # Django admin module
from django.urls import path       # URL routing
from register.views import submit_form,view_csv
from register.views import register_page,teachers_page # login_pageImport views from the authentication app
from django.conf import settings   # Application settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from django.conf.urls.static import static
from register.views import home_page, mark
from register.views import contact, register_teacher
from register.views import search_csv,edit_student,searchs

from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('register.urls')),
    path('home/', home_page, name='home_page'),
    path('contact/', contact, name='contact'),
    path('login/', submit_form, name='submit'),
    path('register/', register_page, name='register'),        # Login page
    path('view/', view_csv, name='view'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('teachers/', teachers_page, name='teachers'),
    path('register_teacher/', register_teacher, name='register_teacher'),
    path('mark/', mark, name='marking'),
    path('search/', search_csv, name='search_csv'),  # Ensure this line is included
    path('edit/<str:student_id>/', edit_student, name='edit_student'),
    path('searchs/', searchs, name='searchs'),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files using staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()