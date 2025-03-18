from django.contrib import admin
from .models import Poll
from .models import Option

# admin.site.register(Poll)
# admin.site.register(Option)

class OptionInline(admin.TabularInline):  # Use TabularInline for a table-like display
    model = Option
    extra = 0  # Number of empty fields to display for new related objects

@admin.register(Poll)
class PollAdmin(admin.ModelAdmin):
    inlines = [OptionInline]  # Attach the inline model to the Poll admin