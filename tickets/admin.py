from django.contrib import admin

from .models import Comentario, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "titulo",
        "categoria",
        "prioridad",
        "estado",
        "created_at",
        "updated_at",
    )
    list_filter = ("prioridad", "estado", "categoria")
    search_fields = ("titulo", "descripcion")


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "ticket",
        "titulo",
        "fecha_registro",
    )
    search_fields = ("titulo", "descripcion")