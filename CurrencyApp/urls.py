from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name='index'),
    path('about/', views.about, name='about'),

    # pages
    path('login/', views.login_page, name='login'),
    path('signup/', views.signup, name='signup'),

    # auth actions
    path('loginAction/', views.loginAction, name='loginAction'),
    path('signupAction/', views.signupAction, name='signupAction'),

    # allauth
    path('accounts/', include('allauth.urls')),

    # currency pages
    path('livecurrency/', views.livecurrency, name='livecurrency'),
    path('defaultcurrency/', views.defaultcurrency, name='defaultcurrency'),
    path('coinexchange/', views.coinexchange, name='coinexchange'),

    # actions
    path('livecurrencyAction/', views.livecurrencyAction),
    path('defaultcurrencyAction/', views.defaultcurrencyAction),
    path('coinAction/', views.coinAction),

    # API
    path('currency_history/', views.currency_history),
]