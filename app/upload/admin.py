from django.contrib import admin
from .models import RegisterSeat


# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('token', 'assign_seat')
    list_filter = ('token', 'assign_seat')
    search_fields = ('token', 'assign_seat')
    ordering = ('token',)


admin.register(RegisterSeat, RegisterAdmin)
