from django.contrib import admin
from polls.models import MyQuestion,MyChoice
# Register your models here.

class ChoiceInlines(admin.TabularInline):
    model=MyChoice
    extra=3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[(None,{'fields':['question_text']}),]
    inlines=[ChoiceInlines]

admin.site.register(MyQuestion,QuestionAdmin)

# admin.site.register(MyQuestion)
# admin.site.register(MyChoice)
