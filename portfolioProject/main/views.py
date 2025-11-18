from django.shortcuts import render, redirect
from .models import (
    ProgrammingSkill,
    ToolTechnology,
    SpecialInterest,
    ContactInfo,
    WorkExperience,
)
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages


def home(request):
    context = {
        'prog_skills': ProgrammingSkill.objects.all(),
        'tools': ToolTechnology.objects.all(),
        'special_interests': SpecialInterest.objects.all(),
    }
    return render(request, 'home.html', context)


def work(request):
    experiences = WorkExperience.objects.all()
    return render(request, 'work.html', {'experiences': experiences})


def contact(request):
    contact_info = ContactInfo.objects.first()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        body = f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"

        try:
            send_mail(
                f"Portfolio Contact - {name}",
                body,
                settings.DEFAULT_FROM_EMAIL,
                ['floppy941998@gmail.com'],
                fail_silently=False,
            )
            messages.success(request, "Message sent successfully!")
        except:
            messages.error(request, "Error sending message.")

    return render(request, 'contact.html', {'contact': contact_info})


def add_skill(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            ProgrammingSkill.objects.create(name=name)
        return redirect('home')
    return render(request, 'add_skill.html')


def add_tool(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            ToolTechnology.objects.create(name=name)
        return redirect('home')
    return render(request, 'add_tool.html')


def add_interest(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:
            SpecialInterest.objects.create(name=name)
        return redirect('home')
    return render(request, 'add_interest.html')


def delete_skill(request, id):
    ProgrammingSkill.objects.filter(id=id).delete()
    return redirect('home')


def delete_tool(request, id):
    ToolTechnology.objects.filter(id=id).delete()
    return redirect('home')


def delete_interest(request, id):
    SpecialInterest.objects.filter(id=id).delete()
    return redirect('home')


def add_experience(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        company = request.POST.get('company') or ''
        role = request.POST.get('role')
        purpose = request.POST.get('purpose')
        duration = request.POST.get('duration')
        description = request.POST.get('description')

        if title and role and purpose and duration and description:
            WorkExperience.objects.create(
                title=title,
                company=company,
                role=role,
                purpose=purpose,
                duration=duration,
                description=description,
            )
        return redirect('work')

    return render(request, 'add_experience.html')


def delete_experience(request, id):
    WorkExperience.objects.filter(id=id).delete()
    return redirect('work')
