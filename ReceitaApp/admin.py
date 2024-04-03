from django.contrib import admin

from ReceitaApp.models import Categoria, Receita

# Register your models here.
class ReceitaAppAdmin(admin.ModelAdmin):
    list_display = ['nome', 'ingredientes', 'preparo', 'dificuldade']
    list_display_links = ['nome']

class CategoriaAdmin(admin.ModelAdmin):
    #colunas exibidas
    list_display = ['nome']
    #colunas com link para editar
    list_display_links = ['nome']
    #colunas para filtro
    list_filter = ['nome']
    



admin.site.register(Receita, ReceitaAppAdmin)
admin.site.register(Categoria,CategoriaAdmin)
