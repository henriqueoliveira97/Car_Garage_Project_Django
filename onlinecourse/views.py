from django.shortcuts import render
from django.http import HttpResponseRedirect
# <HINT> Import any new Models here
from .models import Mecanico, Cliente, Vendedor, Viatura, Reparacao, Peca, PecaReparacao, Administrativo
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.contrib.auth import login, logout, authenticate
import logging
# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.


def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'onlinecourse/user_registration_bootstrap.html', context)
    elif request.method == 'POST':
        # Check if user exists
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            User.objects.get(username=username)
            user_exist = True
        except:
            logger.error("New user")
        if not user_exist:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request, user)
            return redirect("onlinecourse:cliente", pk=user.id)
        else:
            context['message'] = "User already exists."
            return render(request, 'onlinecourse/user_registration_bootstrap.html', context)


def login_request(request):
    context = {}
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['psw']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            #Cliente
            if hasattr(user, 'cliente'):
                return redirect('onlinecourse:cliente', pk=user.cliente.id)

            # Mecânico
            if hasattr(user, 'mecanico'):
                return redirect('onlinecourse:mecanico', pk=user.mecanico.id)

            # Admin 
            if user.is_staff or user.is_superuser:
                return redirect('onlinecourse:administrative', pk=user.id)

            return redirect('onlinecourse:index')
        else:
            context['message'] = "Invalid username or password."
            return render(request, 'onlinecourse/user_login_bootstrap.html', context)
    else:
        return render(request, 'onlinecourse/user_login_bootstrap.html', context)


def logout_request(request):
    logout(request)
    return redirect('onlinecourse:index')

def editar_reparacao(request, reparacao_id):
    reparacao= get_object_or_404(Reparacao, id= reparacao_id)

    # Só permite que o mecânico responsável edite
    if reparacao.mecanico.user != request.user:
        return HttpResponseForbidden("Não tem permissão para editar esta reparação.")

    if request.method == "POST":
        reparacao.descricao = request.POST.get("descricao")
        reparacao.status = request.POST.get("status")
        reparacao.custo_total = request.POST.get("custo_total")
        reparacao.save()
        return redirect('onlinecourse:mecanico', pk=reparacao.mecanico.id)
    return redirect('onlinecourse:mecanico', pk=reparacao.mecanico.id)

def adicionar_reparacao(request, viatura_id):
    viatura = get_object_or_404(Viatura, id=viatura_id)
    mecanico = viatura.mecanico  

    if request.method == "POST":
        descricao = request.POST.get("descricao")
        status = request.POST.get("status")
        custo_total = request.POST.get("custo_total") or 0

        
        reparacao = Reparacao.objects.create(
            descricao=descricao,
            status=status,
            custo_total=custo_total,
            mecanico=mecanico,
            viatura=viatura
        )
        return redirect('onlinecourse:mecanico', pk=mecanico.id)
    
    return redirect('onlinecourse:mecanico', pk=mecanico.id)

class ClientView(generic.ListView):
    template_name = 'onlinecourse/client_details_bootstrap.html'
    context_object_name = 'viaturas'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            cliente = Cliente.objects.filter(user=user).first()
            if cliente:
                return Viatura.objects.filter(cliente=cliente).prefetch_related('reparacoes')
        return Viatura.objects.none()

class MecanincalView(generic.ListView):
    template_name= 'onlinecourse/mecanic_details_bootstrap.html'
    context_object_name= 'viaturas'

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            mecanico = Mecanico.objects.filter(user= user).first()
            if mecanico:
                return Viatura.objects.filter(mecanico=mecanico)
        return Viatura.objects.none()
    
class AdministrativeView(generic.ListView):
    template_name= 'onlinecourse/admin_details_bootstrap.html'
    context_object_name = 'administrative'




class InitialView(TemplateView):
    template_name = 'onlinecourse/initial_page_bootstrap.html'