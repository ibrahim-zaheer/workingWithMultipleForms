from django.contrib import admin
from .models import Skill,Award,Certification,ContactInformation,Education,Hobby,Language,ProfessionalMembership,Project,Publication,VolunteerExperience,WorkExperience
# Register your models here.

class EducationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Education._meta.fields]

class ContantInformationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ContactInformation._meta.fields]    

admin.site.register(ContactInformation,ContantInformationAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(WorkExperience)
admin.site.register(Skill)
admin.site.register(Certification)
admin.site.register(Project)
admin.site.register(Award)
admin.site.register(ProfessionalMembership)
admin.site.register(Publication)
admin.site.register(Language)
admin.site.register(VolunteerExperience)
admin.site.register(Hobby)