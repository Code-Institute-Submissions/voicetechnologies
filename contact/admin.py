from django.contrib import admin
from .models import Contact

# Register your models here.
admin.site.register(Contact)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'date',)
    search_fields = ('name', 'email',)
    date_hierarchy = 'date'
