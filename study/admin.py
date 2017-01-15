from django.contrib import admin
from study.models import Study

# Register your models here.
class StudyAdmin(admin.ModelAdmin):
    list_display = ('id','class_name', 'class_content', 'target_user','tag')
admin.site.register(Study, StudyAdmin)