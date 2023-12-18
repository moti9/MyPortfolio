from django.contrib import admin
from .models import (
    Project,
    ProjectImage,
    Skill,
    Education,
    WorkExperience,
    SocialMedia,
    Certification,
    Language,
    Presentation,
    Blog,
    Interest,
    Profile,
    ContactMessage,
    FamiliarTech,
    LibFramework,
    ToolPlatform,
    SubscribeEmail,
)

admin.site.site_title = "Moti Kumar Yadav | Portfolio"
admin.site.index_title = "Moti Kumar Yadav - Admin Panel"
admin.site.site_header = "Moti Kumar Yadav"
# Register your models here.

admin.site.register(Project)
admin.site.register(ProjectImage)
admin.site.register(Skill)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(SocialMedia)
admin.site.register(Certification)
admin.site.register(Language)
admin.site.register(Presentation)
admin.site.register(Blog)
admin.site.register(Interest)
admin.site.register(Profile)
admin.site.register(ContactMessage)
admin.site.register(FamiliarTech)
admin.site.register(ToolPlatform)
admin.site.register(LibFramework)
admin.site.register(SubscribeEmail)
