from django.db import models


class Study(models.Model):

    TAG_CHOICES = (
        ('program','Program'),
        ('base_subject','Base_Subject'),
        ('sport','Sport')
    )

    """クラス"""
    class_name = models.CharField(max_length=100)
    class_content = models.CharField(max_length=1000)
    target_user = models.CharField(max_length=400)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES)

    def __str__(self):
        return self.class_name



