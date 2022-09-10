from django.urls import path
from .views import ActivateEmailView, ActivateSendEmailView, Authentication, BasketAllClean, BasketClean, BasketView, ChangeIMG_test, HomePageView, LoginOrRegistrationView, Logout, Registrations,ResetPassword_3_View,ResetPassword_4_View,ResetPassword_2_View,ResetPassword_1_View, charge

urlpatterns = [
    path("",HomePageView.as_view(),name='home'),
    path('login-or-register/',LoginOrRegistrationView.as_view(),name='reg'),
    path('reg/',Registrations.as_view(),name='regi'),
    path('log/',Authentication.as_view(), name='log'),
    path('logout/',Logout.as_view(),name='logout'),
    path('uasd/',ChangeIMG_test.as_view(),name='ch'),
    path('reset_password_step_1/',ResetPassword_1_View.as_view(),name='reset'),
    path('reset_password_step_2/',ResetPassword_2_View.as_view(),name='password_reset_done'),
    path('reset_password_step_3/<uidb64>/<token>/',ResetPassword_3_View.as_view(),name='password_reset_confirm'),
    path('reset_password_step_4/',ResetPassword_4_View.as_view(),name='password_reset_complete'),
    path('activate/',ActivateSendEmailView.as_view(),name='activate'),
    path('activate/<uidb64>/<token>/',ActivateEmailView.as_view(),name='activeEmail'),
    path('user-basket/',BasketView.as_view(),name='basket'),
    path('rem/<pk>',BasketClean.as_view(),name='remove'),
    path('allclean-basket/',BasketAllClean.as_view(),name='clean'),
    path('success-charge/<int:sum>/',charge,name='charge'),
]