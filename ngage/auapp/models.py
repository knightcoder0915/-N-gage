from django.db import models

class DeleteModel(models.Model):
    deleted_Employee = models.CharField(max_length=50)
    deleting_HR = models.CharField(max_length=50)
	

    def __str__(self):
	    return self.deleting_HR

class EventsModel(models.Model):
    ename = models.CharField(max_length=50)
    image_url = models.CharField(max_length=400)
    description = models.CharField(max_length=250)
    date_of_event = models.DateField()


    def __str__(self):
	    return self.ename