# forms.py
from django import forms

class MyForm(forms.Form):
  
    name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100, required=False)
    student_id = forms.CharField(max_length=100, required=False)
    cohort = forms.CharField(max_length=100, required=False)
    username = forms.CharField(max_length=100, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    
    USER_TYPE_CHOICES = [
        ('student', 'Student'),
        ('teacher', 'Teacher'),
    ]
    user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)

class TeacherRegistrationForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

class studentmakeform(forms.Form):
    name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=100)
    cohort = forms.CharField(max_length=100)
    Computer_Arquitecture= forms.DecimalField(max_digits=100, decimal_places=2)
    Networking= forms.DecimalField(max_digits=100, decimal_places=2)
    R_Programming= forms.DecimalField(max_digits=100, decimal_places=2)


# forms.py

from django import forms

class EditStudentForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100)
    student_id = forms.CharField(label='Student ID', max_length=100, disabled=False)  # Make ID uneditable
    cohort = forms.CharField(label='Cohort', max_length=100)
    Computer_Arquitecture = forms.DecimalField(label='Computer Architecture', max_digits=100, decimal_places=2)
    Networking = forms.DecimalField(label='Networking', max_digits=100, decimal_places=2)
    R_Programming = forms.DecimalField(label='R Programming', max_digits=100, decimal_places=2)

   

