from django.contrib import admin


from .models import Wave

@admin.register(Wave)
class WaveAdmin(admin.ModelAdmin):
    pass

    