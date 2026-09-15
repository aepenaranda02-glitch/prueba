from functools import wraps

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from .models import Comentario, Ticket


def agente_required(view_func):
    """Solo usuarios del grupo 'Agente' o superusuarios."""
    @wraps(view_func)
    @login_required
    def _wrapped(request, *args, **kwargs):
        es_agente = request.user.groups.filter(name="Agente").exists()
        if not (es_agente or request.user.is_superuser):
            raise PermissionDenied("Solo los agentes pueden realizar esta acción.")
        return view_func(request, *args, **kwargs)
    return _wrapped


@login_required
def lista_tickets(request):
    tickets = Ticket.objects.all().order_by("-created_at")

    estado = request.GET.get("estado", "")
    prioridad = request.GET.get("prioridad", "")

    if estado:
        tickets = tickets.filter(estado=estado)

    if prioridad:
        tickets = tickets.filter(prioridad=prioridad)

    context = {
        "tickets": tickets,
        "estado_actual": estado,
        "prioridad_actual": prioridad,
        "estados": Ticket.Estado.choices,
        "prioridades": Ticket.Prioridad.choices,
    }

    return render(request, "tickets/lista.html", context)


@login_required
def crear_ticket(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        prioridad = request.POST.get("prioridad", "")

        if not titulo or not descripcion or not categoria or not prioridad:
            messages.error(request, "Todos los campos obligatorios deben estar completos.")
            return render(request, "tickets/crear.html", {
                "prioridades": Ticket.Prioridad.choices,
                "datos": request.POST,
            })

        Ticket.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            categoria=categoria,
            prioridad=prioridad,
            estado=Ticket.Estado.ABIERTO,
        )
        messages.success(request, "Ticket creado correctamente.")
        return redirect("lista_tickets")

    return render(request, "tickets/crear.html", {
        "prioridades": Ticket.Prioridad.choices,
    })


@login_required
def detalle_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    comentarios = ticket.comentarios.all().order_by("-fecha_registro")
    return render(request, "tickets/detalle.html", {
        "ticket": ticket,
        "comentarios": comentarios,
        "estados": Ticket.Estado.choices,
        "prioridades": Ticket.Prioridad.choices,
    })


@agente_required
def actualizar_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method != "POST":
        return redirect("detalle_ticket", ticket_id=ticket.id)

    estado = request.POST.get("estado")
    prioridad = request.POST.get("prioridad")

    if estado in dict(Ticket.Estado.choices):
        ticket.estado = estado

    if prioridad in dict(Ticket.Prioridad.choices):
        ticket.prioridad = prioridad

    ticket.save()
    messages.success(request, "Ticket actualizado correctamente.")
    return redirect("detalle_ticket", ticket_id=ticket.id)


@login_required
def agregar_comentario(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()

        if not titulo or not descripcion:
            messages.error(request, "El título y la descripción del comentario son obligatorios.")
            return redirect("detalle_ticket", ticket_id=ticket.id)

        Comentario.objects.create(
            ticket=ticket,
            titulo=titulo,
            descripcion=descripcion,
        )
        messages.success(request, "Comentario agregado correctamente.")

    return redirect("detalle_ticket", ticket_id=ticket.id)