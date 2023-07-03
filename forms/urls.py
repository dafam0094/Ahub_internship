from django.urls import path
from . import views


urlpatterns = [
    # Other URL patterns...
    path('contact/', views.Contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
    path('registration_form/', views.registration_form, name='registration_form'),
    path('login/', views.student_login, name='student_login'),
    path('student/profile/', views.student_profile, name='student_profile'),
    path('forms/student/update/', views.student_update, name='student_update'),
    path('signout', views.signOut, name='signout')
]
