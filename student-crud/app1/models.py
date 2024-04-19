from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    mobile_number = models.PositiveIntegerField()

    class Meta:
        app_label = 'app1'
        db_table = "student"