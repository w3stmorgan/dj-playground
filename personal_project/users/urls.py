from django.urls import path

from personal_project.users.views import (
    logout_modal,
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("logout_modal/", view=logout_modal, name="logout_modal"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
