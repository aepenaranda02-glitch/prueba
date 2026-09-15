from django.contrib.auth.models import Group, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Crea los grupos y usuarios por defecto para la demo."

    def handle(self, *args, **options):
        agente_group, _ = Group.objects.get_or_create(name="Agente")
        solicitante_group, _ = Group.objects.get_or_create(name="Solicitante")

        if not User.objects.filter(username="agente").exists():
            agente = User.objects.create_user(
                username="agente",
                password="agente123",
                is_staff=True,
            )
            agente.groups.add(agente_group)
            self.stdout.write(self.style.SUCCESS("Usuario 'agente' creado."))
        else:
            # Reset password por si las dudas
            agente = User.objects.get(username="agente")
            agente.set_password("agente123")
            agente.save()
            self.stdout.write("Usuario 'agente' actualizado.")

        if not User.objects.filter(username="solicitante").exists():
            solicitante = User.objects.create_user(
                username="solicitante",
                password="solicitante123",
            )
            solicitante.groups.add(solicitante_group)
            self.stdout.write(self.style.SUCCESS("Usuario 'solicitante' creado."))
        else:
            solicitante = User.objects.get(username="solicitante")
            solicitante.set_password("solicitante123")
            solicitante.save()
            self.stdout.write("Usuario 'solicitante' actualizado.")

        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin123",
            )
            self.stdout.write(self.style.SUCCESS("Superusuario 'admin' creado."))
        else:
            admin = User.objects.get(username="admin")
            admin.set_password("admin123")
            admin.save()
            self.stdout.write("Superusuario 'admin' actualizado.")

        self.stdout.write(self.style.SUCCESS("Usuarios y grupos listos."))