from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class Preference_Tag(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Agenda_Tag(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Recruitment_Tag(models.Model):
    name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Preference(models.Model):
    title = models.CharField(max_length=50, unique=True)
    body = models.CharField(max_length=200,blank=True)
    name = models.CharField(max_length=20,blank=True)
    create_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Preference_Tag, blank=True)
    
    def __str__(self):
        return self.title
    
class Agenda(models.Model):
    title = models.CharField(max_length=50,unique=True)
    body = models.CharField(max_length=200)
    name = models.CharField(max_length=20,blank=True)
    create_date = models.DateField(auto_now=True)
    tags = models.ManyToManyField(Agenda_Tag, blank=True)
    
    def __str__(self):
        return self.title
    
class Recruitment(models.Model):
    title = models.CharField(max_length=50,unique=True)
    body = models.CharField(max_length=200)
    adress = models.CharField(max_length=20,blank=False,default='adress')
    create_date = models.DateField( auto_now=True)
    tags = models.ManyToManyField(Recruitment_Tag, blank=True)
    author = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.title
    
    
class Preference_GroupMessage(models.Model):
    title = models.ForeignKey(Preference,null=False,db_column='title', to_field='title', on_delete=models.CASCADE, default='title')
    username = models.CharField(max_length=100,default='usernname')
    message = models.TextField(max_length=200,  null =True, default='default_message')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}: {self.message}"
    
class Agenda_GroupMessage(models.Model):
    title = models.ForeignKey(Agenda,null=False,db_column='title', to_field='title', on_delete=models.CASCADE, default='title')
    username = models.CharField(max_length=100,default='usernname')
    message = models.TextField(max_length=200,  null =True, default='default_message')
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username}: {self.message}"
    
    
class Preference_people(models.Model):
    title = models.ForeignKey(Preference,null=False,db_column='title',to_field='title', on_delete=models.CASCADE, default='title')
    username = models.CharField(max_length=100,default='usernname')
    
class Agenda_people(models.Model):
    title = models.ForeignKey(Agenda,null=False,db_column='title', to_field='title', on_delete=models.CASCADE, default='title')
    username = models.CharField(max_length=100,default='usernname')
class Recruitment_people(models.Model):
    title = models.ForeignKey(Recruitment,null=False,db_column='title', to_field='title', on_delete=models.CASCADE, default='title')
    username = models.CharField(max_length=100,default='usernname')
    

    
