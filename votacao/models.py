# from django.db import models
# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import User
# from django.db import models


# class Perfil(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     perfil = models.CharField(max_length=10, choices=[('admin', 'Administrador'), ('fiscal', 'Fiscal')])

#     def __str__(self):
#         return f'{self.user.username} - {self.perfil}'
    
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Perfil.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.perfil.save()

# class Secao(models.Model):
#     local = models.CharField(max_length=200)
#     numero = models.IntegerField(unique=True)

#     def __str__(self):
#         return f"Seção {self.numero} - {self.local}"


# class Cargo(models.Model):
#     cargo = models.CharField(max_length=50)

#     def __str__(self):
#         return self.cargo


# class Usuario(models.Model):
    
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
#     secao = models.ForeignKey('Secao', on_delete=models.CASCADE)
#     perfil = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('fiscal', 'Fiscal')])
#     nome = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user.username

# class Candidato(models.Model):
#     nome = models.CharField(max_length=100)
#     numero = models.IntegerField(unique=True)
#     foto = models.ImageField(upload_to='fotos_candidatos/')
#     partido = models.CharField(max_length=50)
#     cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.nome} ({self.partido})"


# class Apurado(models.Model):
#     secao = models.ForeignKey('Secao', on_delete=models.CASCADE)
#     candidato = models.ForeignKey('Candidato', on_delete=models.CASCADE)
#     cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
#     votos_validos = models.IntegerField()
#     votos_branco = models.IntegerField()
#     votos_nulos = models.IntegerField()
#     foto = models.ImageField(upload_to='fotos_apuracao/', blank=True, null=True)  # Adicionando o campo de foto, se necessário

#     def __str__(self):
#         return f"Seção {self.secao.numero} - {self.candidato.nome} ({self.cargo.cargo})"



# ________________2ª alteração____________________________________________________

# from django.db import models
# from django.contrib.auth.models import User

# class Secao(models.Model):
#     local = models.CharField(max_length=200)
#     numero = models.IntegerField(unique=True)

#     def __str__(self):
#         return f"Seção {self.numero} - {self.local}"

# class Usuario(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
#     secao = models.ForeignKey('Secao', on_delete=models.CASCADE)
#     nome = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user.username

# class Cargo(models.Model):
#     cargo = models.CharField(max_length=50)

#     def __str__(self):
#         return self.cargo

# class Candidato(models.Model):
#     nome = models.CharField(max_length=100)
#     numero = models.IntegerField(unique=True)
#     foto = models.ImageField(upload_to='fotos_candidatos/')
#     partido = models.CharField(max_length=50)
#     cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.nome} ({self.partido})"

# class Apurado(models.Model):
#     secao = models.ForeignKey('Secao', on_delete=models.CASCADE)
#     candidato = models.ForeignKey('Candidato', on_delete=models.CASCADE)
#     cargo = models.ForeignKey('Cargo', on_delete=models.CASCADE)
#     votos_validos = models.IntegerField()
#     votos_branco = models.IntegerField()
#     votos_nulos = models.IntegerField()
#     foto = models.ImageField(upload_to='fotos_apuracao/', blank=True, null=True)

#     def __str__(self):
#         return f"Seção {self.secao.numero} - {self.candidato.nome} ({self.cargo.cargo})"

# class Perfil(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     perfil = models.CharField(max_length=10, choices=[('admin', 'Administrador'), ('fiscal', 'Fiscal')])

#     def __str__(self):
#         return f'{self.user.username} - {self.perfil}'

# ------------------------------3ª Alteração

# from django.db import models
# from django.contrib.auth.models import User
# from django.db.models.signals import post_save, post_delete
# from django.dispatch import receiver

# class Secao(models.Model):
#     local = models.CharField(max_length=200)
#     numero = models.IntegerField(unique=True)

#     def __str__(self):
#         return f"Seção {self.numero} - {self.local}"

# class Cargo(models.Model):
#     cargo = models.CharField(max_length=50)

#     def __str__(self):
#         return self.cargo

# class Usuario(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
#     secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
#     perfil = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('fiscal', 'Fiscal')])

#     def __str__(self):
#         return self.user.username

# @receiver(post_delete, sender=Usuario)
# def delete_user(sender, instance, **kwargs):
#     if instance.user:
#         instance.user.delete()

# class Candidato(models.Model):
#     nome = models.CharField(max_length=100)
#     numero = models.IntegerField(unique=True)
#     foto = models.ImageField(upload_to='fotos_candidatos/')
#     partido = models.CharField(max_length=50)
#     cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.nome} ({self.partido})"

# class Apurado(models.Model):
#     secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
#     candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
#     cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
#     votos_validos = models.IntegerField()
#     votos_branco = models.IntegerField()
#     votos_nulos = models.IntegerField()
#     foto = models.ImageField(upload_to='fotos_apuracao/', blank=True, null=True)

#     def __str__(self):
#         return f"Seção {self.secao.numero} - {self.candidato.nome} ({self.cargo.cargo})"

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Secao(models.Model):
    local = models.CharField(max_length=200)
    numero = models.IntegerField(unique=True)

    def __str__(self):
        return f"Seção {self.numero} - {self.local}"

class Cargo(models.Model):
    cargo = models.CharField(max_length=50)

    def __str__(self):
        return self.cargo

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

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    perfil = models.CharField(max_length=20, choices=[('admin', 'Admin'), ('fiscal', 'Fiscal')])
    nome = models.CharField(max_length=255)
    def __str__(self):
        return self.user.username

@receiver(post_delete, sender=Usuario)
def delete_user(sender, instance, **kwargs):
    if instance.user:
        instance.user.delete()

class Candidato(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField(unique=True)
    foto = models.ImageField(upload_to='fotos_candidatos/')
    partido = models.CharField(max_length=50)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} ({self.partido})"

class Apurado(models.Model):
    secao = models.ForeignKey(Secao, on_delete=models.CASCADE)
    candidato = models.ForeignKey(Candidato, on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    votos_validos = models.IntegerField()
    votos_branco = models.IntegerField()
    votos_nulos = models.IntegerField()
    foto = models.ImageField(upload_to='fotos_apuracao/', blank=True, null=True)

    def __str__(self):
        return f"Seção {self.secao.numero} - {self.candidato.nome} ({self.cargo.cargo})"
