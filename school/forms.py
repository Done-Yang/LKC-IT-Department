from django import forms
from school.models import CustomUser
from . import models

#for admin
class AdminSigupForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','password']

#for student related form

class StudentUserForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','password']

class StudentExtraForm(forms.ModelForm):
    class Meta:
        model=models.StudentExtra
        fields=['student_id','fee', 'sessionYear','adress', 'birthday', 'phone',]

#for teacher related form
class TeacherUserForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['first_name','last_name','username','password']

class TeacherExtraForm(forms.ModelForm):
    class Meta:
        model=models.TeacherExtra
        fields=['salary', 'phone', 'adress','birthday']

class AskDateForm(forms.Form):
    date=forms.DateField()

# session year related form
class AddSessionYear(forms.ModelForm):
    class Meta:
        model = models.SessionYear
        fields = ['sessionYear','classificate','attendance', 'fee']

#for notice related form
class NoticeForm(forms.ModelForm):
    class Meta:
        model=models.Notice
        fields='__all__'

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))
