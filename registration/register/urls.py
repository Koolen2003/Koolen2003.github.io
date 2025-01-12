from django.urls import path
from . import views
from django.urls import path


urlpatterns = [
    path('', views.submit_form, name='login'),
    path('home/', views.home_page, name='home_page'),
    path('contact/',views.contact, name='contact'),
    path('login/', views.submit_form, name='login'),
    path('logout/', views.log_in_out, name='logout'),
    path('register/', views.register_page, name='register_page'),
    path('view/', views.view_csv, name='view_csv'),
    path('teachers/', views.teachers_page, name='teachers_page'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('mark/', views.mark, name='marking'),
    path('studentmark/', views.studentmark, name='studentmark'),
    path('search/', views.search_csv, name='search'),
    path('searchs/', views.searchs, name='searchs'),
    path('edit/<str:student_id>/', views.edit_student, name='edit_student'),
]   