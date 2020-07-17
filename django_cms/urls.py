"""django_cms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url, include
from apps.login import views as login_view
from apps.account import views

urlpatterns = [
    path('', include('apps.login.urls')),
    path('dashboard/', login_view.login_validate.as_view(), name="dashboard"),
    path('dashboard_7/', views.dashboard_page_7.as_view(), name="dashboard_7"),
    path('panel/', views.panel_page.as_view(), name="panel_page"),
    path('tabs/', views.tabs_line_pill_page.as_view(), name="tabs_page"),
    path('alerts/', views.alert_page.as_view(), name="alert_page"),
    path('tooltips/', views.tooltip_page.as_view(), name="tooltip_page"),
    path('badges/', views.badges_page.as_view(), name="badges_page"),
    path('lists/', views.list_page.as_view(), name="list_page"),
    path('toastr/', views.toastr_page.as_view(), name="toastr_page"),
    path('profile/', login_view.profile, name="profile"),
    path('dashboard/users/', include('apps.account.urls')),
    path('dashboard/roles/', include('apps.roles.urls')),
    path('logout/', login_view.logout.as_view(), name="logout")
]
