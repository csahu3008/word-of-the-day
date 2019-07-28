from django.contrib import admin
from .models import Daily_words
# Register your models here.
class WordAdmin(admin.ModelAdmin):
    pass
    list_display = ('Word', 'Date_posted')
    list_filter = ['Date_posted']
    
admin.site.register(Daily_words,WordAdmin)
