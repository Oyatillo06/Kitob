from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Student, Ustoz
from .models import Fan
from .models import Record,Muallif,Kitob

@admin.register(Kitob)
class KitobAdmin(ModelAdmin):
    search_fields = ["id",'nom']
    list_filter = ['tur']
    list_display = ['nom', 'sahifa', 'tur']
    ordering = ['sahifa']
@admin.register(Muallif)
class MuallifAdmin(ModelAdmin):
    search_fields = ["id",'ism']
    list_filter = ['jinsi']
    ordering = ['yosh']
@admin.register(Record)
class RecordAdmin(ModelAdmin):


   list_display = ['muallif','kitob']
   autocomplete_fields = ['muallif','kitob']





admin.site.register(Student)
admin.site.register(Ustoz)
admin.site.register(Fan)




