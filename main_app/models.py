from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Skill(models.Model):
    SKILL_LEVELS = (
        (1, 'Fundamental Awareness'),
        (2, 'Novice'),
        (3, 'Intermediate'),
        (4, 'Advanced'),
        (5, 'Expert'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField(max_length=300)
    skill_level = models.IntegerField(choices=SKILL_LEVELS, default=1)

    def __str__(self):
        return f'{self.description} ({self.get_skill_level_display()})'

    def get_absolute_url(self):
        return reverse('skill_detail', args=[self.pk])