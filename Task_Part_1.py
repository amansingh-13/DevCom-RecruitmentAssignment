from uuid import uuid4
from django.db import models

class User(models.Model):
    """A user of Book-ed"""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=50)
    roll_no = models.IntegerField(unique=True)
    short_description = models.CharField(max_length=50, blank=True)
    
