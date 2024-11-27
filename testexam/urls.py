from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    path('contact/', views.contact_page, name='contact_page'),  # Adminga yozish sahifasi
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    # link
    path('', views.HomeView, name='home'),
    path('exam/', views.ExamView, name='exam'),
    # path('result/', views.Test_result, name='test_result'),
    path('service/', views.ServiceView, name='service'),
    path('contact/', views.ContactView, name='contact'),
    path('search/', views.ask_question, name='ask_question'),
    path('about/', views.AboutView, name='about'),
    path('doctorself/', views.DoctorSelfViewList, name='doctorself'),
    path('appointment/', views.AppointmentView, name='appointment'),
    path('appointment/success/', views.Appointment_success, name='appointment_success'),

    path('inbox/', views.user_inbox, name='user_inbox'),  # Foydalanuvchi inbox sahifasi
    path('respond/<int:appointment_id>/', views.respond_to_appointment, name='respond_to_appointment'),
]


