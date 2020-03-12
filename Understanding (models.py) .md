# Understanding models.py

```python
from uuid import uuid4
from django.db import models
from helpers.misc import get_url_friendly
```
This just imports directories
```python
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

```python
    def save(self, *args, **kwargs):
        self.str_id = get_url_friendly(
            self.name if not self.canonical_name else self.canonical_name)
        super(Body, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/org/' + self.str_id
  
  ```

The first and last functions work together:

- **save** provides str_id to the body. It is name if name=canonical_name otherwise it is canonical_name
- **get_absolute_url** gives the url of the body using str_id, ..../**org/str_id**

Eg. Name: Tinkerers' Lab ; Canonical Name: tl ; so the url is ..../**org/tl** <br />

The *str* function is a standard function which gives back the name of the body <br />

 ```python
 class Meta:
        verbose_name = "Body"
        verbose_name_plural = "Bodies"
        ordering = ("name",)
 
 ```
When you ask the user to add a name (it is a field in class Body), it is ambiguous what you are referring to. So verbone_name is created, it will ask for a "Body" from the user instead of name (default verbose_name is set same as the field name). Similarly the plural is provided as django makes the default plural by adding 's' at the end of verbose_name.<br />
Meta can be used to add stuff to the class outside the class<br />
Not sure what ordering does exactly, maybe it orders the way fields are to be entered in by the user

 
 ```python
 class BodyChildRelation(models.Model):
    """Relates a body to one child."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    parent = models.ForeignKey(
        Body, on_delete=models.CASCADE, default=uuid4, related_name='children')
    child = models.ForeignKey(
        Body, on_delete=models.CASCADE, default=uuid4, related_name='parents')

    def __str__(self):
        return self.parent.name + " --> " + self.child.name
 
 ```
 The peculiar thing about this part is that it does not crate a child class in the usual sense. In InstiApp all sub-bodies are also declared as an instance of the class Body. This class: **BodyChildRelation** just relates the body to sub-body. As this is not a parent-child relation in the normal sense, any sort of tree structure can be made.<br />
A relation is built by creating an instance of class BodyChildRelation. This relation can be used/viewed by printing the class which calls the *str* function, the output looks like : parent_name --> child name

```python
     class Meta:
        verbose_name = "Body-Child Relation"
        verbose_name_plural = "Body-Child Relations"
        ordering = ("parent__name",)
 ```
 Same as above 
