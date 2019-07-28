from django.db import models
from django.urls import reverse
# Create your models here.
class Daily_words(models.Model):
    class Meta:
        ordering=['-Date_posted']
    Date_posted=models.DateField(auto_now=True)
    Word=models.CharField(max_length=20,unique=True)
    Meaning=models.CharField(max_length=100)
    Synonyms=models.CharField(max_length=80,null=True,blank=True)
    Antonyms=models.CharField(max_length=80,null=True,blank=True)
    Examples=models.TextField()
    AddedBy=models.ForeignKey('auth.User',on_delete=models.CASCADE)
    def __str__(self):
        return self.Word

    def get_absolute_url(self):
        return reverse("Detail", kwargs={"pk": self.pk})
    