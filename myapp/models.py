from django.db import models
from django.contrib.auth.models import User

def alumni_profile_upload_path(instance, filename):
    return f'profile_pics/{instance.id}/{filename}'

def post_image_upload_path(instance, filename):
    return f'post_images/{instance.user.id}/{filename}'

class Alumni(models.Model):
    name = models.CharField(max_length=100, verbose_name="Full Name")
    batch = models.IntegerField(verbose_name="Batch Year")
    department = models.CharField(max_length=100, verbose_name="Department")
    skills = models.TextField(verbose_name="Skills & Expertise")
    experience = models.TextField(verbose_name="Work Experience")
    linkedin_url = models.URLField(blank=True, null=True, verbose_name="LinkedIn Profile")
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub Profile")
    profile_picture = models.ImageField(upload_to=alumni_profile_upload_path, blank=True, null=True, verbose_name="Profile Picture")

    class Meta:
        verbose_name = "Alumni"
        verbose_name_plural = "Alumni"
        ordering = ["name"]  # Sort alumni alphabetically

    def __str__(self):
        return f"{self.name} ({self.batch}, {self.department})"


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    content = models.TextField(verbose_name="Post Content")
    image = models.ImageField(upload_to=post_image_upload_path, blank=True, null=True, verbose_name="Post Image")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ['-created_at']  # Show newest posts first

    def __str__(self):
        return f"Post by {self.user.username} on {self.created_at.strftime('%Y-%m-%d %H:%M')}"
