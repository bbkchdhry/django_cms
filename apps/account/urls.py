from django.urls import path
from .views import user_page, user_view, user_view_detail


urlpatterns = [
    path('', user_page.as_view(), name="users_page"),
    path('list/', user_view.as_view(), name="list_users"),
    path('create/', user_view.as_view(), name="create_users"),
    path('edit/<int:id>', user_view_detail.as_view(), name="edit_user"),
    path('delete/<int:id>', user_view_detail.as_view(), name="delete_user"),

]