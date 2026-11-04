from django.contrib import admin
from .models import To_Do_List


@admin.register(To_Do_List)
class ToDoListAdmin(admin.ModelAdmin):

    list_display = ('title', 'created', 'done')

    list_filter = ('done', 'created')

    search_fields = ('title', 'description')
