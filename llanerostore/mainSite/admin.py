from django.contrib import admin
from .models import Question, Choice
# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['questionText']}),
        ('Informacion del clima', {'fields':['pub_date'], 'classes':['collapse']})
    ]
    inlines = [ChoiceInline]

admin.site.register(Question,QuestionAdmin)