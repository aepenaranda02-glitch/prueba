from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login en la raíz: http://127.0.0.1:8000/
    path(
        '',
        auth_views.LoginView.as_view(template_name='registration/login.html'),
        name='login',
    ),

    # Logout
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),

    # App tickets
    path('tickets/', include('tickets.urls')),
]