from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Topics(models.Model):
    """A topic the user is learning about."""
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length = 200)
    date = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        """return the string representation of the model"""
        return self.text

class Entry(models.Model):
    """Something specific learned about a topic"""
    topic = models.ForeignKey(Topics, on_delete = models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        """Manage extra information in entry model"""
        verbose_name_plural = "Entries"

    def __str__(self):
        """return the string representation of the model"""
        # TIY-18.2
        if len(self.text) < 50:
            return f"{self.text[:50]}"
        return f"{self.text[:50]}..."