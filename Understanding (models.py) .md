# Understanding models.py

```python
from uuid import uuid4
from django.db import models
from helpers.misc import get_url_friendly
```
This just imports directories
```
class Body(models.Model):
    """An organization or club which may conduct events."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    str_id = models.CharField(max_length=50, editable=False, null=True)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    time_of_modification = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=50)
    canonical_name = models.CharField(max_length=50, blank=True)
    short_description = models.CharField(max_length=50, blank=True)
    description = models.TextField(blank=True)
    website_url = models.URLField(blank=True, null=True)
    image_url = models.URLField(blank=True, null=True)
    cover_url = models.URLField(blank=True, null=True)
    blog_url = models.URLField(null=True, blank=True)
   ```
"Body" containts these fields:

|  UUIDField    |   CharField   | DateTimeField |TextField|URLField|
| ------------- |:-------------:|:-------------:|:-------:|:------:|
|   id | str_id |   time_of_creation      |description|website_url|
|       | name      |  time_of_modification        |   | image_url|
|   |    canonical_name | | |cover_url|
|        |short_description|||blog_url|

    def save(self, *args, **kwargs):
        self.str_id = get_url_friendly(
            self.name if not self.canonical_name else self.canonical_name)
        super(Body, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/org/' + self.str_id

The first and last functions work together:

- **save** provides str_id to the body. It is name if name=canonical_name otherwise it is canonical_name
- **get_absolute_url** gives the url of the body using str_id, ..../**org/str_id**

Eg. Name: Tinkerers' Lab ; Canonical Name: tl ; so the url is ..../**org/tl** <br />

The second function is a standard function which gives back the name of the body <br />
