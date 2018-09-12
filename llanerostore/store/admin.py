from django.contrib import admin
from .models import Item, Foto
# Register your models here.
class fotosInline(admin.TabularInline):
    model = Foto
    extra = 4

class ItemAdmin(admin.ModelAdmin):
    inlines = [fotosInline]
admin.site.register(Item, ItemAdmin)
