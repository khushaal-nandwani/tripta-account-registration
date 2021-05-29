from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import TForm
from .forms import InputFormRevamped


class CustomFormAdmin(TForm):
    add_form = InputFormRevamped
    model = TForm

admin.site.register(CustomFormAdmin)
admin.site.register(TForm)

