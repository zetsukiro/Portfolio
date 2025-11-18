from django.contrib import admin
from .models import (
    ProgrammingSkill,
    ToolTechnology,
    SpecialInterest,
    ContactInfo,
    WorkExperience
)

admin.site.register(ProgrammingSkill)
admin.site.register(ToolTechnology)
admin.site.register(SpecialInterest)
admin.site.register(ContactInfo)
admin.site.register(WorkExperience)
