"""
Middleware que obliga a iniciar sesión para /tickets/*.
"""
from django.conf import settings
from django.shortcuts import redirect


class LoginRequiredMiddleware:
    """
    Redirige a LOGIN_URL si el usuario no está autenticado y la ruta
    empieza por /tickets/.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ruta_protegida = request.path.startswith("/tickets/")
        usuario_no_logueado = not request.user.is_authenticated
        ruta_excluida = (
            request.path.startswith("/accounts/")
            or request.path.startswith("/admin/")
            or request.path.startswith(settings.STATIC_URL)
        )

        if ruta_protegida and usuario_no_logueado and not ruta_excluida:
            return redirect(f"{settings.LOGIN_URL}?next={request.path}")

        return self.get_response(request)