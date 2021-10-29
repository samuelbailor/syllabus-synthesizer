from django.urls import path

from . import views

app_name = 'faculty_profile'
urlpatterns = [
    # profile index (placeholder, should be deleted in the future)
    path('', views.index, name='index'),
    path('edit/', views.edit, name='edit'),
    path('add/', views.add, name='add')

    # will the login app and corresponding session database provide a faculty's profile_id?
    # path('<int:profile_id>', views.index, name='index'),
    # path('<int:profile_id>/edit/', views.edit, name='edit')
]
