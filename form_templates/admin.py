from django.contrib import admin
from form_templates.models import FormTemplate, NumberField, StringField, ListField

#class ChoiceInline(admin.StackedInline):
#   model = Choice
#   extra = 3
#
#class PollAdmin(admin.ModelAdmin):
#    fieldsets = [
#        (None,               {'fields': ['question']}),
#        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
#    ]
#    inlines = [ChoiceInline]
#    list_display = ('question', 'pub_date', 'was_published_recently')
#    list_filter = ['pub_date']
#    
class NumberInline(admin.StackedInline):
    model = NumberField
    extra = 3
    
class StringInline(admin.StackedInline):
    model = StringField
    extra = 3
    
class ListInline(admin.StackedInline):
    model = ListField
    extra = 3
    
class TemplateAdmin(admin.ModelAdmin):
    inlines = [NumberInline, StringInline, ListInline]
    list_display = ['name']
    
admin.site.register(FormTemplate, TemplateAdmin)