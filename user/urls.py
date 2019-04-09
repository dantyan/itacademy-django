from django.urls import path, re_path

from user.views import LoginView, SignUpConfirmView, SignupDoneView, SignupView, home, logout

app_name = 'user'
urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view(), name='user-login'),
    path('logout/', logout, name='logout'),

    path('signup/', SignupView.as_view(), name='signup'),
    path('signup/done/', SignupDoneView.as_view(), name='signup-done'),
    re_path(
        r'^signup/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        SignUpConfirmView.as_view(),
        name='signup-confirm',
    ),

    path('profile/<int:pk>', home, name="profile")

]
