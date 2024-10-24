from django.db import models

# Create your models here.
class Certificate(models.Model):
    title = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    school = models.CharField(max_length=255)
    href = models.URLField()
    description = models.TextField()

    def save(self, *args, **kwargs):
        print(f'Saving Certificate: {self.title}')
        super().save(*args, **kwargs)

class Testimonial(models.Model):
    author = models.CharField(max_length=255)
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

class PersonalDescription(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

class Skill(models.Model):
    title = models.CharField(max_length=255)
    percentage = models.IntegerField()

class CodeProject(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='code_projects/')
    href = models.URLField()
    skills = models.ManyToManyField(Skill)

class TimelineEntry(models.Model):
    title = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    time_span = models.CharField(max_length=255)
    description_points = models.TextField()
