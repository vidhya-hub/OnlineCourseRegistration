from django import  forms
from app1.models import StudentModel

class Studentform(forms.ModelForm):
    c=(('python','python'),('django','django'),('java','java'))
    course=forms.ChoiceField(choices=c)
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        fields="__all__"
        model=StudentModel
        labels={"name":"student name","age":"student age"}
class Loginform(forms.Form):
    username=forms.CharField(label="Emailid")
    password=forms.CharField(widget=forms.PasswordInput,label="Password")
