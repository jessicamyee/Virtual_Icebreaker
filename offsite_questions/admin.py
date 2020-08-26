from django.contrib import admin
from .models import Entry, Team
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from offsite_questions.models import Entry, Team



# Register your models here.

# admin.site.register(Entry)

class EntryResource(resources.ModelResource):
    class Meta:
        model = Entry


class EntryAdmin(ImportExportModelAdmin):
    resource_class = EntryResource

admin.site.register(Entry, EntryAdmin)   


class Team(resources.ModelResource):
    class Meta:
        model = Team
    