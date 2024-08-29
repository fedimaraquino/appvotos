from django import forms
from .models import Secao, Usuario, Candidato, Cargo, Apurado
from django import forms
from django.contrib.auth.models import User
from .models import Usuario, Perfil

class SecaoForm(forms.ModelForm):
    class Meta:
        model = Secao
        fields = ['local', 'numero']




# class UsuarioForm(forms.ModelForm):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
#     secao = forms.ModelChoiceField(queryset=Secao.objects.all())
#     perfil = forms.ChoiceField(choices=[('admin', 'Admin'), ('fiscal', 'Fiscal')])

#     class Meta:
#         model = Usuario
#         fields = ['nome', 'secao', 'perfil']

#     def save(self, commit=True):
#         # Cria um novo usuário
#         user = User.objects.create_user(
#             username=self.cleaned_data['username'],
#             password=self.cleaned_data['password']
#         )

#         # Cria o perfil associado ao usuário
#         usuario = super().save(commit=False)
#         usuario.user = user

#         if commit:
#             usuario.save()
#         return usuario

class UsuarioForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    perfil = forms.ChoiceField(choices=[('admin', 'Administrador'), ('fiscal', 'Fiscal')])

    class Meta:
        model = Usuario
        fields = ['nome', 'secao','perfil']

    def save(self, commit=True):
        usuario = super(UsuarioForm, self).save(commit=False)
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        
        usuario.user = user
        if commit:
            usuario.save()
            # Atualiza ou cria o perfil
            perfil, created = Perfil.objects.get_or_create(user=user)
            perfil.perfil = self.cleaned_data['perfil']
            perfil.save()
        return usuario
class CandidatoForm(forms.ModelForm):
    class Meta:
        model = Candidato
        fields = ['nome', 'numero', 'foto', 'partido', 'cargo']

class CargoForm(forms.ModelForm):
    class Meta:
        model = Cargo
        fields = ['cargo']

class ApuradoForm(forms.ModelForm):
    class Meta:
        model = Apurado
        fields = ['secao', 'candidato', 'cargo', 'votos_validos', 'votos_branco', 'votos_nulos', 'foto']
