from django.db import models

# Music will be used to store all information regarding the "Music" section of Vermanubis portfolio.
class About(models.Model):
    about = models.CharField(max_length=10000)
    last_updated = models.DateTimeField(auto_now_add=True)
