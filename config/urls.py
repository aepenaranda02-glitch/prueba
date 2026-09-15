from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # LOGIN en la raíz: http://127.0.0.1:8000/  y  https://tickets-8r4x.onrender.com/
    path(
        '',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),

    # LOGOUT
    path(
        'accounts/logout/',
        auth_views.LogoutView.as_view(next_page='login'),
        name='logout',
    ),

    # App tickets
    path('tickets/', include('tickets.urls')),
]