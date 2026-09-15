"""
URL configuration for config project.
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.urls import include, path


urlpatterns = [
    # Redirige "/" al login
    path("", lambda request: redirect("login")),

    # Admin
    path("admin/", admin.site.urls),

    # Login / Logout
    path(
        "accounts/login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path(
        "accounts/logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    # App tickets
    path("tickets/", include("tickets.urls")),
]