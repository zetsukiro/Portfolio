from django.db import models

class ProgrammingSkill(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ToolTechnology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SpecialInterest(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class WorkExperience(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255, blank=True, null=True)
    role = models.CharField(max_length=255)
    purpose = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        if self.company:
            return f"{self.title} - {self.role} @ {self.company}"
        return f"{self.title} - {self.role}"


class ContactInfo(models.Model):
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.email
