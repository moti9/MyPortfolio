from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse
from .models import (
    Profile,
    Education,
    WorkExperience,
    Project,
    ProjectImage,
    Certification,
    Language,
    SocialMedia,
    Presentation,
    Blog,
    Interest,
    Skill,
    LibFramework,
    ToolPlatform,
    FamiliarTech,
    SubscribeEmail,
)
from .forms import ContactForm, SubsribeForm


# Create your views here.


def home(request):
    # Retrieve data from various models
    user_profile = Profile.objects.first()  # Assuming you have a single user profile
    education_data = Education.objects.all().order_by("-graduation_date")
    work_experience_data = WorkExperience.objects.all()
    projects_data = Project.objects.all()
    certifications_data = Certification.objects.all()
    languages_data = Language.objects.all()
    social_media_data = SocialMedia.objects.all()
    presentations_data = Presentation.objects.all()
    blogs_data = Blog.objects.all()
    interests_data = Interest.objects.all()
    skills = Skill.objects.all()
    libframework = LibFramework.objects.all()
    toolPlatform = ToolPlatform.objects.all()
    familiartech = FamiliarTech.objects.all()

    # Render the template with the retrieved data
    return render(
        request,
        "index.html",
        {
            "profile": user_profile,
            "educations": education_data,
            "experiences": work_experience_data,
            "projects": projects_data,
            "certifications": certifications_data,
            "languages": languages_data,
            "social_media": social_media_data,
            "presentations": presentations_data,
            "blogs": blogs_data,
            "interests": interests_data,
            "skills": skills,
            "libframework": libframework,
            "toolPlatform": toolPlatform,
            "familiartech": familiartech,
        },
    )


def project_detail(request, pk):
    try:
        project = get_object_or_404(Project, pk=pk)
        images = ProjectImage.objects.filter(project=project)  # Retrieve project images
    except Project.DoesNotExist:
        messages.error(
            request,
            "Project does not exist.",
            extra_tags="alert alert-danger alert-dismissible fade show",
        )
        return redirect("home")  # Return an appropriate template

    return render(
        request, "project_detail.html", {"project": project, "images": images}
    )


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here, like sending an email notification.
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    return redirect("portfolio:home")


def subscribe(request):
    if request.method == "POST":
        form = SubsribeForm(request.POST)
        if form.is_valid():
            form.save()
            # You can add additional logic here, like sending an email notification.
            return JsonResponse({"success": True})
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    return redirect("portfolio:home")


# def contact(request):
#     if request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # You can add additional logic here, like sending an email notification.
#             return redirect("success_message")  # Redirect to a success page
#     else:
#         form = ContactForm()

#     return render(request, "index.html", {"form": form})
