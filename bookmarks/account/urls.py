from django.urls import path,include
from django.contrib.auth import views as auth_views
from .import views

app_name='account'
urlpatterns = [
    #path('login/',views.user_login,name='login'),
    path('edit/',views.edit,name='edit'),
    path('register/',views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(),name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('',views.dashboard,name='dashboard')
#password urls
,path('password-change/',auth_views.PasswordChangeView.as_view(),name='password_change')
,path('password-change/done',auth_views.PasswordChangeDoneView.as_view(),name='password_change_done')
#resst password urls
,
path('password-reset/', auth_views.PasswordResetView.as_view(
    email_template_name='registration/password_reset_email.html',
     subject_template_name='registration/password_reset_subject.txt'
), name='password_reset'),
path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
path('password-reset/confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
path('password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
path('', include('django.contrib.auth.urls')),
]
