from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import ContactInformation,Education,Hobby
from .forms import ContactInformationForm,EducationForm,HobbyForm
from django.http import HttpResponse
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'home.html')

def basicDataCollector(request):
    if request.method == 'POST':
        form = ContactInformationForm(request.POST)
        if form.is_valid():
            # Use form's cleaned_data to create a ContactInformation instance
            contact = ContactInformation(
                full_name=form.cleaned_data['full_name'],
                phone_number=form.cleaned_data['phone_number'],
                email_address=form.cleaned_data['email_address'],
                linkedin_profile=form.cleaned_data['linkedin_profile'],
                professional_website=form.cleaned_data['professional_website']
            )
            contact.save()
            return render(request, 'thanks.html',{'context':contact})

    else:
        form = ContactInformationForm()

    return render(request, 'contactinformation.html', {'form': form})

# def create_education(request):
#     if request.method == 'POST':
#         form = EducationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return render(request,'thanks.html',{'form':form})  # Redirect to a success page or another view
#     else:
#         form = EducationForm()

#     return render(request, 'create_education.html', {'form': form})


# To create a form for entering Education data where the associated ContactInformation object
#  is already determined by the URL 
# parameter (pk), you can pre-populate the form with the associated contact information. 
def education_form_creation(request, pk):
    # Retrieve the ContactInformation instance using its primary key
    contact_instance = get_object_or_404(ContactInformation, pk=pk)

    if request.method == 'POST':
        # Pre-populate the form with the associated contact information
        form = EducationForm(request.POST, initial={'contact_information': contact_instance.id})
        hobbyForm = HobbyForm(request.POST,initial={'contact_information': contact_instance.id})
        context = {
        'form': form,
        'hobbyForm':hobbyForm,
        'contact_information': contact_instance,
    }
        
        if form.is_valid() and hobbyForm.is_valid():
            form.save()
            hobbyForm.save()
            return render(request, 'thanks.html', context)
    else:
        # Initialize the form with the associated contact information
        form = EducationForm(initial={'contact_information': contact_instance.id})
        hobbyForm = HobbyForm(initial={'contact_information': contact_instance.id})

    context = {
        'form': form,
        'hobbyForm':hobbyForm,
        'contact_information': contact_instance,
    }

    return render(request, 'create_education.html', context)