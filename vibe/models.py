from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

# Create your models here.
class Vibe(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
  text = models.TextField(max_length=240)
  
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  
  def clean(self):
    if self.media.count() > 5:
        raise ValidationError("You can upload at most 5 media files (photos/videos).")

  def __str__(self):
    return f"Vibe by {self.user.username} - {self.text[:10]}"
  
class VibeMedia(models.Model):
  vibe = models.ForeignKey(Vibe, related_name="media", on_delete=models.CASCADE)
  file = models.FileField(
        upload_to="media/",
        validators=[FileExtensionValidator(allowed_extensions=['jpg','jpeg','png','gif','mp4','mov','avi','mkv'])]
    )# can store image or video

  def __str__(self):
    return f"Media for Vibe {self.vibe.id}"