from django import forms
from .models import Education, WorkExperience, Skill, Certification, Project, Award, ProfessionalMembership, Publication, Language, VolunteerExperience, Hobby,ContactInformation

class ContactInformationForm(forms.ModelForm):
    class Meta:
        model = ContactInformation
        fields = ['full_name', 'phone_number', 'email_address', 'linkedin_profile', 'professional_website']

    def __init__(self, *args, **kwargs):
        super(ContactInformationForm, self).__init__(*args, **kwargs)

        # You can add additional customization for each field here, if needed
        # For example, you can set placeholders, labels, or custom widget attributes

        self.fields['full_name'].widget.attrs.update({'placeholder': 'Enter your full name'})
        self.fields['phone_number'].widget.attrs.update({'placeholder': 'Enter your phone number'})
        self.fields['email_address'].widget.attrs.update({'placeholder': 'Enter your email address'})
        self.fields['linkedin_profile'].widget.attrs.update({'placeholder': 'Enter your LinkedIn profile (optional)'})
        self.fields['professional_website'].widget.attrs.update({'placeholder': 'Enter your professional website (optional)'})
class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = '__all__'

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = '__all__'

class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = '__all__'

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = '__all__'

class ProfessionalMembershipForm(forms.ModelForm):
    class Meta:
        model = ProfessionalMembership
        fields = '__all__'

class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = '__all__'

class VolunteerExperienceForm(forms.ModelForm):
    class Meta:
        model = VolunteerExperience
        fields = '__all__'

class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'