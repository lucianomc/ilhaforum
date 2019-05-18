from django.contrib.auth.models import User
from django.db import models
from .base_model import BaseModel


class Forum(BaseModel):
    description = models.CharField(max_length=255)