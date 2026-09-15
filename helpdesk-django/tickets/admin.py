from django.contrib import admin

from .models import Comentario, Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "categoria", "prioridad", "estado", "created_at")
    list_filter = ("estado", "prioridad", "categoria")
    search_fields = ("titulo", "descripcion", "categoria")
    ordering = ("-created_at",)
    readonly_fields = ("created_at", "updated_at")


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id", "titulo", "ticket", "fecha_registro")
    list_filter = ("fecha_registro",)
    search_fields = ("titulo", "descripcion")
    ordering = ("-fecha_registro",)