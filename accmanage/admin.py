from django.contrib import admin
from .models import Accinfo


class AccinfoAdmin(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(Accinfo, AccinfoAdmin)
