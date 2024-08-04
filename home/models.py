from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

# Create your models here.
class AchievementModel(models.Model):
    title = models.CharField(max_length=255, default="")
    image = models.FileField(upload_to="images/", blank=False)

    def __str__(self) -> str:
        return super().__str__()

class HomeButtonModel(models.Model):
    button_title = models.CharField(max_length=100, blank=True)
    file = models.FileField(upload_to="pdfs/", blank=False)

    def __str__(self) -> str:
        return str(self.button_title)


class AboutMeModel(models.Model):
    content = RichTextUploadingField()

    def save(self, *args, **kwargs):
        if not self.pk and AboutMeModel.objects.exists():
            raise ValidationError('There is already an instance of SingletonModel.')
        return super(AboutMeModel, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'AboutMeModel'
        verbose_name_plural = 'AboutMeModel'

    def __str__(self):
        return "AboutMeModel"

class TechUsedTagModel(models.Model):
    tag_name = models.CharField(max_length=100, null=False, blank=False)
    icon = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return str(self.tag_name)


class ProjectModel(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    image = models.FileField(upload_to="images/", blank=True)
    content = RichTextUploadingField()
    github_link = models.URLField(null=True, blank=True, default=None)
    demo_link = models.URLField(null=True, blank=True, default=None)
    document_link = models.FileField(upload_to="pdfs/", blank=True, null=True, default=None)
    tech_used_tag = models.ManyToManyField(TechUsedTagModel)
    position = models.IntegerField(default=255)  # Add this field for custom ordering

    def __str__(self) -> str:
        return str(self.title)
