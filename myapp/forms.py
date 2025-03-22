from django import forms
from django.core.validators import MaxLengthValidator
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Share your thoughts...',
                'rows': 3,
                'maxlength': '500'  # Frontend validation
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'accept': 'image/*'  # Allow only images
            })
        }
        validators = {
            'content': [MaxLengthValidator(500)]  # Enforce 500-char limit in the backend
        }

    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > 500:
            raise forms.ValidationError("Post content must be 500 characters or less.")
        return content

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            max_size = 5 * 1024 * 1024  # 5MB limit
            if image.size > max_size:
                raise forms.ValidationError("Image size must be less than 5MB.")
        return image
