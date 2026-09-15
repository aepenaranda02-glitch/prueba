from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_tickets, name="lista_tickets"),
    path("crear/", views.crear_ticket, name="crear_ticket"),
    path("<int:ticket_id>/", views.detalle_ticket, name="detalle_ticket"),
    path(
        "<int:ticket_id>/actualizar/",
        views.actualizar_ticket,
        name="actualizar_ticket",
    ),
    path(
        "<int:ticket_id>/comentario/",
        views.agregar_comentario,
        name="agregar_comentario",
    ),
]