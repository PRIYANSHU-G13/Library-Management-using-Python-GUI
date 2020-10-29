from django import forms
from .models import Student,Course
import datetime
from datetime import datetime, time


class StudentForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput,required=True)
    DOB = forms.DateField(localize=True,widget=forms.DateInput(format = '%d-%m-%y',attrs={'type': 'date'}),help_text="Date of birth")
    class Meta:
        model=Student
        fields="__all__"
        labels={
            "regno":"Registration Number",
            'fullname':"Full Name",
            'username':"Username Name",
            'mobile':"Mobile number",
            'DOB':"Date of birth", 
        }

    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['course'].empty_label="Select the course"
        # self.fields["password"].required = False
        # self.fields["DOB"].required = False

        # instance = getattr(self, 'instance', None)
        # if instance and instance.pk:
        #     self.fields['password'].widget.attrs['readonly'] = True
        #     self.fields['DOB'].widget.attrs['readonly'] = True
        
        



     

