from django.contrib import admin
from .models import Poll
from .models import Option

admin.site.register(Poll)
admin.site.register(Option)