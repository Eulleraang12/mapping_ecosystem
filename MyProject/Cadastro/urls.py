# from django.contrib import admin
from django.urls import path, include
# from Cadastro.views import index
from . import views

urlpatterns = [
    
    # path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registro/', views.registro, name='add'),
    path('sobre_mapeamento/', views.sobre_mapeamento, name='sobre_mapeamento'),
    path('vertente_do_map/', views.vertente_do_map, name='vertente_do_map'),
    path('mapeamento_atual/', views.mapeamento_atual, name='mapeamento_atual'),
    path('addUsers', views.addUsers, name='addUsers'),

]