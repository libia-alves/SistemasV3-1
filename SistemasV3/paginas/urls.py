from django.urls import path

from .views import PaginaInicial, SobreView,produtosView, empresasView

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('sobre/',SobreView.as_view(),name='sobre'),
    path('produtos/',produtosView.as_view(),name='produtos'),
    path('empresa/',empresasView.as_view(),name='empresa'),

    
]
