from django.contrib import admin
from .models import *


class ProblemInline(admin.StackedInline):
    model = Problem
    extra = 1


class LevelAdmin(admin.ModelAdmin):
    inlines = [ProblemInline,]


admin.site.register(Level, LevelAdmin)