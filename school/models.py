from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    USER = (
        ('1', "HOD"),
        ('2', "STAFF"),
        ('3', "TEACHER"),
        ('4', "STUDENT")
    )
    user_type = models.CharField(max_length=100, choices=USER, default='1')
    picture = models.ImageField(upload_to="admin", null=True, blank=True)

    REQUIRED_FIELDS = ['first_name', 'last_name']

class SessionYear(models.Model):
    id = models.AutoField(primary_key=True)
    sessionYear = models.CharField(max_length=40)
    classificate = models.CharField(max_length=100)
    attendance = models.CharField(max_length=100)
    fee = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.sessionYear

class TeacherExtra(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    salary = models.PositiveIntegerField()
    phone = models.IntegerField()
    adress = models.CharField(max_length=200)
    birthday = models.DateField()
    joindate=models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return self.user.first_name
    @property
    def get_id(self):
        return self.user.id
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name

class StudentExtra(models.Model):
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=30)
    phone = models.IntegerField()
    adress = models.CharField(max_length=200)
    birthday = models.DateField()
    fee=models.PositiveIntegerField()
    sessionYear = models.ForeignKey(SessionYear, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name

position = (('accounting','accounting'),
           ('manager','manager'))

class StaffExtra(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone = models.IntegerField(null=True)
    adress = models.CharField(max_length=200)
    birthday = models.DateField()
    position = models.CharField(max_length=50, choices=position)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name+ " " + self.user.last_name

class Notice(models.Model):
    date=models.DateField(auto_now=True)
    by=models.CharField(max_length=20,null=True,default='school')
    message=models.CharField(max_length=500)
