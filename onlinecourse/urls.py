from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # route is a string contains a URL pattern
    # view refers to the view function
    # name the URL
    path(route='', view=views.InitialView.as_view(), name='index'),
    path('registration/', views.registration_request, name='registration'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('client/<int:pk>/', views.ClientView.as_view(), name='cliente'),
    path('mechanic/<int:pk>/', views.MecanincalView.as_view(), name='mecanico'),
    path('admin/<int:pk>/', views.AdministrativeView.as_view(), name='admin'),
    path('reparacao/editar/<int:reparacao_id>/', views.editar_reparacao, name='editar_reparacao'),
    path('reparacao/adicionar/<int:viatura_id>/', views.adicionar_reparacao, name='adicionar_reparacao'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
