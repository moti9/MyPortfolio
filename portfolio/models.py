from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Project(models.Model):
    project_name = models.CharField(max_length=100, default="")
    project_type = models.CharField(max_length=100, default="")
    techstack = RichTextField(max_length=500, default="")
    pages = RichTextField(max_length=500, default="")
    tags = RichTextField(max_length=500, default="")
    description = RichTextField(default="")
    moreabout = RichTextField(default="")
    url = models.URLField(default="")
    github_repo = models.URLField(default="")
    project_date = models.DateField()

    def __str__(self):
        return self.project_name


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.FileField(upload_to="projects/", default=None)

    def __str__(self):
        return f"{self.project}--{self.image.name}"


class Skill(models.Model):
    name = models.CharField(max_length=100, default="")
    proficiency = models.FloatField(default=100)
    image = models.FileField(default=None, upload_to="skill/")

    def __str__(self):
        return self.name


class Education(models.Model):
    institution = models.CharField(max_length=200, default="")
    degree = models.CharField(max_length=100, default="")
    major = models.CharField(max_length=100, default="")
    aggregate = models.CharField(max_length=20, default="")
    graduation_date = models.DateField(default=None)
    image = models.FileField(default=None, upload_to="education/")

    def __str__(self):
        return f"{self.degree} in {self.major}"


class WorkExperience(models.Model):
    job_title = models.CharField(max_length=100, default="")
    company = models.CharField(max_length=200, default="")
    start_date = models.DateField(default=None)
    end_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=200, default="")
    job_description = models.TextField(default=None)
    image = models.FileField(upload_to="work/", default=None)

    def __str__(self):
        return self.job_title


class SocialMedia(models.Model):
    platform = models.CharField(max_length=20, default="")
    url = models.URLField(default=None)
    image = models.FileField(upload_to="social/", default=None)

    def __str__(self):
        return f"{self.platform}-{self.url}"


class Certification(models.Model):
    name = models.CharField(max_length=200, default="")
    issuing_organization = models.CharField(max_length=200, default="")
    issue_date = models.DateField()
    expiration_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    certificate = models.FileField(upload_to="certificates/", default=None)
    image = models.FileField(upload_to="certificate/", default=None)

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(max_length=100, default="")
    image = models.FileField(upload_to="languages/", default=None)

    def __str__(self):
        return self.name


class LibFramework(models.Model):
    name = models.CharField(max_length=100, default="")
    image = models.FileField(upload_to="frameworks/", default=None)

    def __str__(self):
        return self.name


class FamiliarTech(models.Model):
    name = models.CharField(max_length=100, default="")
    image = models.FileField(upload_to="familiar/", default=None)

    def __str__(self):
        return self.name


class ToolPlatform(models.Model):
    name = models.CharField(max_length=100, default="")
    image = models.FileField(upload_to="tools/", default=None)

    def __str__(self):
        return self.name


class Presentation(models.Model):
    title = models.CharField(max_length=200, default="")
    date = models.DateField(default=None)
    description = models.TextField(default=None)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=200, default="")
    url = models.URLField(default=None)
    image = models.FileField(default=None, upload_to="blog/")

    def __str__(self):
        return self.title


class Interest(models.Model):
    name = models.CharField(max_length=100, default="")
    description = models.TextField(default=None)
    image = models.FileField(default=None, upload_to="interest/")

    def __str__(self):
        return self.name


class Profile(models.Model):
    # Basic Information
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    profile_picture = models.FileField(
        upload_to="profile_pictures/", blank=True, null=True
    )
    title = models.CharField(max_length=100, default="")

    # Contact Information
    email = models.EmailField(default="")
    phone = models.CharField(max_length=20, default="(+91) 906-XXXX-100")
    curr_location = models.CharField(max_length=200, default="")
    location = models.CharField(max_length=200, default="")

    # About Me
    about = RichTextField()

    # Relationships
    skills = models.ManyToManyField(Skill, blank=True)
    education = models.ManyToManyField(Education, blank=True)
    work_experience = models.ManyToManyField(WorkExperience, blank=True)
    projects = models.ManyToManyField(Project, blank=True)
    languages = models.ManyToManyField(Language, blank=True)
    social_media = models.ManyToManyField(SocialMedia, blank=True)
    presentations = models.ManyToManyField(Presentation, blank=True)
    blogs = models.ManyToManyField(Blog, blank=True)
    interests = models.ManyToManyField(Interest, blank=True)
    certifications = models.ManyToManyField(Certification, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    reviewed = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class SubscribeEmail(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    stamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


# class Profile(models.Model):
#     # Basic Information
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     profile_picture = models.FileField(
#         upload_to="profile_pictures/", blank=True, null=True
#     )
#     title = models.CharField(max_length=100, default="")

#     # Contact Information
#     email = models.EmailField(default="")
#     phone = models.CharField(max_length=20, default="(+91) 906-XXXX-100")
#     curr_location = models.CharField(max_length=200, default="")
#     location = models.CharField(max_length=200, default="")

#     # About Me
#     about = models.TextField(default=None)

# class Profile(models.Model):
#     name = models.CharField(max_length=100, default="")
#     title = models.CharField(max_length=100, default="")
#     email = models.EmailField(default="")
#     phone = models.CharField(max_length=20, default="(+91) 906-XXXX-100")
#     curr_location = models.CharField(max_length=200, default="")
#     location = models.CharField(max_length=200, default="")
#     about = models.TextField(default=None)
#     github = models.URLField(blank=True, null=True)
#     linkedin = models.URLField(blank=True, null=True)
#     twitter = models.URLField(blank=True, null=True)
#     instagram = models.URLField(blank=True, null=True)

#     def __str__(self):
#         return self.name
