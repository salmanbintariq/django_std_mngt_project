from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('home/', views.home_view, name='home'),
    path('logout/', views.logout_view, name='logout'),
    path('all_student/',views.all_student_view, name='allStudent'),
    path('edit_student/<int:id>', views.edit_view, name='edit_student'),
    path('delete_student/<int:id>', views.delete_view, name='delete_student'),
]
