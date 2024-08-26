from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from votacao.models import Perfil

class Command(BaseCommand):
    help = 'Cria perfis para usuários existentes que não têm um perfil associado.'

    def handle(self, *args, **kwargs):
        users_without_profile = User.objects.filter(perfil__isnull=True)
        for user in users_without_profile:
            Perfil.objects.create(user=user, perfil='fiscal')  # Ou 'admin', conforme necessário
            self.stdout.write(self.style.SUCCESS(f'Perfil criado para {user.username}'))
