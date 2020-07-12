from django.contrib import admin
from .models import Entry
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from offsite_questions.models import Entry



# Register your models here.

# admin.site.register(Entry)

class EntryResource(resources.ModelResource):
    class Meta:
        model = Entry


class EntryAdmin(ImportExportModelAdmin):
    resource_class = EntryResource

admin.site.register(Entry, EntryAdmin)            