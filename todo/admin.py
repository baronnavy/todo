from django.contrib import admin
from .models import TodoModel ,Reservation,Reserve

# Register your models here.

admin.site.register(TodoModel)
admin.site.register(Reservation)
admin.site.register(Reserve)