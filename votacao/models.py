from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perfil = models.CharField(max_length=10, choices=[('admin', 'Administrador'), ('fiscal', 'Fiscal')])

    def __str__(self):
        return f'{self.user.username} - {self.perfil}'
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.perfil.save()

class Secao(models.Model):
    local = models.CharField(max_length=200)
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return f"Seção {self.numero} - {self.local}"





class Cargo(models.Model):
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.cargo

# class Usuario(models.Model):
#     nome = models.CharField(max_length=100)
#     secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
#     perfil = models.CharField(max_length=50)  # ex: 'fiscal', 'admin', etc.

#     def __str__(self):
#         return self.nome

class Usuario(models.Model):
    ADMINISTRADOR = 'admin'
    FISCAL = 'fiscal'

    PERFIL_CHOICES = [
        (ADMINISTRADOR, 'Administrador'),
        (FISCAL, 'Fiscal'),
    ]

    nome = models.CharField(max_length=100)
    secao = models.ForeignKey('Secao', on_delete=models.CASCADE)
    perfil = models.CharField(max_length=10, choices=PERFIL_CHOICES)

    def __str__(self):
        return self.nome

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(unique=True)
    foto = models.ImageField(upload_to='fotos_candidatos/')
    partido = models.CharField(max_length=50)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.partido})"


class Apurado(models.Model):
    secao = models.ForeignKey('Secao', on_delete=models.CASCADE)
    candidato = models.ForeignKey('Candidato', on_delete=models.CASCADE)
    cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
    votos_validos = models.IntegerField()
    votos_branco = models.IntegerField()
    votos_nulos = models.IntegerField()
    foto = models.ImageField(upload_to='fotos_apuracao/', blank=True, null=True)  # Adicionando o campo de foto, se necessário

    def __str__(self):
        return f"Seção {self.secao.numero} - {self.candidato.nome} ({self.cargo.cargo})"


