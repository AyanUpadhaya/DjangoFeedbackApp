from django.db import models

class Feedback(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField()
	feedback = models.TextField()

	date_added = models.DateTimeField(auto_now_add =True)

	class Meta:
		ordering = ['-date_added']
