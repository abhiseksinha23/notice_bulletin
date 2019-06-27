from django.db import models
from django.urls import reverse
from django.utils import timezone
# Create your models here.


class Notices(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_info(self):
        return self.info.filter(approved_info=True)

    def get_absolute_url(self):
        return reverse("notices_detail",kwargs={'pk':self.pk})


    def __str__(self):
        return self.title



class addinfo(models.Model):
    notice = models.ForeignKey('notice.Notices', related_name='info',on_delete=models.CASCADE)
    author = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_info= models.BooleanField(default=False)

    def approve(self):
        self.approved_info = True
        self.save()

    def get_absolute_url(self):
        return reverse("notice_list")

    def __str__(self):
        return self.text

class queries(models.Model):
    author = models.CharField(max_length=250)
    regno = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.PositiveIntegerField()
    subject = models.CharField(max_length=500)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse("thanks")

    def __str__(self):
        return self.subject
