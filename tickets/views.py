from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .models import Comentario, Ticket

def login_view(request):
    if request.user.is_authenticated:
        return redirect("lista_tickets")

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        user = authenticate(
            request,
            username=username,
            password=password,
        )

        if user is not None:
            login(request, user)
            return redirect("lista_tickets")

        messages.error(
            request,
            "Usuario o contraseña incorrectos.",
        )

    return render(request, "tickets/login.html")


def logout_view(request):
    logout(request)
    return redirect("login")


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


def crear_ticket(request):
    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()
        categoria = request.POST.get("categoria", "").strip()
        prioridad = request.POST.get("prioridad", "")

        if not titulo or not descripcion or not categoria or not prioridad:
            messages.error(
                request,
                "Todos los campos obligatorios deben estar completos.",
            )
            return render(
                request,
                "tickets/crear.html",
                {
                    "prioridades": Ticket.Prioridad.choices,
                    "datos": request.POST,
                },
            )

        Ticket.objects.create(
            titulo=titulo,
            descripcion=descripcion,
            categoria=categoria,
            prioridad=prioridad,
            estado=Ticket.Estado.ABIERTO,
        )

        messages.success(request, "Ticket creado correctamente.")
        return redirect("lista_tickets")

    return render(
        request,
        "tickets/crear.html",
        {
            "prioridades": Ticket.Prioridad.choices,
        },
    )


def detalle_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    comentarios = ticket.comentarios.all().order_by("-fecha_registro")

    return render(
        request,
        "tickets/detalle.html",
        {
            "ticket": ticket,
            "comentarios": comentarios,
            "estados": Ticket.Estado.choices,
            "prioridades": Ticket.Prioridad.choices,
        },
    )


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


def agregar_comentario(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)

    if request.method == "POST":
        titulo = request.POST.get("titulo", "").strip()
        descripcion = request.POST.get("descripcion", "").strip()

        if not titulo or not descripcion:
            messages.error(
                request,
                "El título y la descripción del comentario son obligatorios.",
            )
            return redirect("detalle_ticket", ticket_id=ticket.id)

        Comentario.objects.create(
            ticket=ticket,
            titulo=titulo,
            descripcion=descripcion,
        )

        messages.success(request, "Comentario agregado correctamente.")

    return redirect("detalle_ticket", ticket_id=ticket.id)