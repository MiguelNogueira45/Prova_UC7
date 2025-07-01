from django.urls import path
from . import views



urlpatterns = [

    path("", views.filmes_principal, name="principal_filmes"),
    path('filme/<int:id>/excluir/', views.excluir_filme, name='excluir_filme'),

]