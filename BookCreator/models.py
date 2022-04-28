from djongo import models

# Create your models here.
class Page(models.Model):
  id = models.CharField(max_length=100, primary_key=True)
  subtitle = models.CharField(max_length=100)
  content = models.CharField(max_length=100)
class BookCreator(models.Model):
   #TODO from oscar: add UnitName field
  id = models.CharField(max_length=100, primary_key=True)
  name = models.CharField(max_length=100)
  type = models.CharField(max_length=100)
  teacherId = models.CharField(max_length=100)
  grade = models.IntegerField()
  contents = models.ArrayField(model_container=Page, )


 


