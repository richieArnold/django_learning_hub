from django.db import models

# Create your models here.
# create a model for courses which creates a table in the database with the following fields: title, description, price, image, created_at

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    thumbnail = models.ImageField(upload_to="course_thumbnails/", null=True, blank=True)

    def __str__(self):
        return self.title