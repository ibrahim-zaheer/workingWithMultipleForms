from django.db import models

class ContactInformation(models.Model):
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    linkedin_profile = models.URLField(blank=True)
    professional_website = models.URLField(blank=True)

class Education(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    institution_name = models.CharField(max_length=255)
    degree_earned = models.CharField(max_length=255)
    major = models.CharField(max_length=255)
    graduation_date = models.DateField()
    honors_or_awards = models.CharField(max_length=255, blank=True)

class WorkExperience(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField()
    achievements = models.TextField(blank=True)

class Skill(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=255)

class Certification(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    certification_name = models.CharField(max_length=255)

class Project(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=255)
    description = models.TextField()
    role = models.CharField(max_length=255)
    outcomes = models.TextField(blank=True)

class Award(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    award_name = models.CharField(max_length=255)

class ProfessionalMembership(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    membership_name = models.CharField(max_length=255)

class Publication(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    publication_title = models.CharField(max_length=255)
    details = models.TextField()

class Language(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    language_name = models.CharField(max_length=255)
    proficiency = models.CharField(max_length=255)

class VolunteerExperience(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    organization_name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    description = models.TextField()

class Hobby(models.Model):
    contact_information = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    hobby_name = models.CharField(max_length=255)
