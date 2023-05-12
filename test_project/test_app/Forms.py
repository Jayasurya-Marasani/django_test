from django import forms
 
class StudentForm(forms.Form) :
    name = forms.CharField(label='Name', max_length=40)
    roll = forms.CharField(label='Roll', help_text='AM.EN.U4AIE20001')
    year = forms.IntegerField(label='Year')
    dob = forms.DateField(label='Date of Birth', required=False)
    degree = forms.CharField(label='Degree', max_length=20) 
    branch = forms.CharField(label='Branch', max_length=50)