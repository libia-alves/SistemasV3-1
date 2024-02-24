from django.views.generic import TemplateView



class PaginaInicial(TemplateView):
    template_name="paginas/index.html"
    

class SobreView(TemplateView):
    template_name="paginas/sobre.html"
    

class produtosView(TemplateView):
    template_name="paginas/produtos.html"
    
    
class empresasView(TemplateView):
    template_name="paginas/empresa.html"
    
    
    