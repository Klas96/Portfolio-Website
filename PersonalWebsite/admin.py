from django.contrib import admin
from .models import Certificate, Testimonial, PersonalDescription, Skill, CodeProject, ArtProject, TimelineEntry

print("Registering models...")  # Debugging statement

admin.site.register(Certificate)
admin.site.register(Testimonial)
admin.site.register(PersonalDescription)
admin.site.register(Skill)
admin.site.register(CodeProject)
admin.site.register(ArtProject)
admin.site.register(TimelineEntry)

print("Models registered.")  # Debugging statement
