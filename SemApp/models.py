from django.db import models

# Create your models here.
class  SemMarks(models.Model):
        Regno=models.CharField(max_length=6)
        Maths=models.IntegerField()
        Physics=models.IntegerField()
        Chemistry=models.IntegerField()

        def __str__(self):
             return self.Regno
              


