from django.contrib import admin
from users.models import User
# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['role', 'name', 'phone_number']
    search_fields = ['role', 'name', 'phone_number', 'passport_seria']
    list_filter = ['role']

admin.site.register(User, UserAdmin)