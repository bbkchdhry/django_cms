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
    path('sweetalert/', views.sweet_alert_page.as_view(), name="sweet_alert_page"),
    path('alertify/', views.alertify.as_view(), name="alertify_page"),
    path('idletimer/', views.idle_timer_page.as_view(), name="idle_timer_page"),
    path('sessiontimeout/', views.session_timeout_page.as_view(), name="session_timeout_page"),
    path('treeview/', views.tree_view_page.as_view(), name="tree_view_page"),
    path('nestable/', views.nestable_list_page.as_view(), name="nestable_list_page"),
    path('clipbord/', views.clipboard_page.as_view(), name="clipboard_page"),
    path('buttons/', views.button_page.as_view(), name="button_page"),
    path('widgetlist/', views.widget_list_page.as_view(), name="widget_list_page"),
    path('formcontrol/', views.form_control_page.as_view(), name="form_control_page"),
    path('formswitch/', views.form_switch_page.as_view(), name="form_switch_page"),
    path('formcheckboxradio/', views.form_checkbox_radio_page.as_view(), name="form_checkbox_radio_page"),
    path('formadvanced/', views.form_advanced_page.as_view(), name="form_advanced_page"),
    path('formlayout/', views.form_layout_page.as_view(), name="form_layout_page"),
    path('inputgroup/', views.form_input_group_page.as_view(), name="form_input_group_page"),
    path('formmask/', views.form_mask_page.as_view(), name="form_mask_page"),
    path('formvaidation/', views.form_validation_page.as_view(), name="form_validation_page"),
    path('texteditor/', views.text_editor_page.as_view(), name="text_editor_page"),
    path('formdropzone/', views.form_dropzone_page.as_view(), name="form_dropzone_page"),
    path('imagecropping/', views.image_cropping_page.as_view(), name="image_cropping_page"),
    path('autocomplete/', views.autocomplete_page.as_view(), name="auto_complete_page"),
    path('formwizard/', views.form_wizard_page.as_view(), name="form_wizard_page"),
    path('datatables', views.datatables_page.as_view(), name="datatables_page"),
    path('chartjs/',views.chart_js_page.as_view(), name="chart_js_page"),
    path('googlemap/', views.google_map_page.as_view(), name="google_map_page"),
    path('calendar/', views.calendar_page.as_view(), name="calendar_page"),
    path('faq/', views.faq_page.as_view(), name="faq_page"),
    path('login_v2/', views.login_v2_page.as_view(), name="login_v2_page"),
    path('login_v3/', views.login_v3_page.as_view(), name="login_v3_page"),
    path('login_v4/', views.login_v4_page.as_view(), name="login_v4_page"),
    path('forgot_password/', views.forgot_password_page.as_view(), name="forgot_password_page"),
    path('error404/', views.error_404_page.as_view(), name="error_404_page"),
    path('error403/', views.error_403_page.as_view(), name="error_403_page"),
    path('error500/', views.error_500_page.as_view(), name="error_500_page"),
    path('maintenance/', views.maintenance_page.as_view(), name="maintenance_page"),
    path('profile/', login_view.profile, name="profile"),
    path('dashboard/users/', include('apps.account.urls')),
    path('dashboard/roles/', include('apps.roles.urls')),
    path('logout/', login_view.logout.as_view(), name="logout")
]
