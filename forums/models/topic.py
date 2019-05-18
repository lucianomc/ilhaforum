from django.db import models
from .base_model import BaseModel

class Topic(BaseModel):
    name = models.CharField(max_length=100)
    forum = models.ForeignKey('Forum', on_delete=models.CASCADE)
