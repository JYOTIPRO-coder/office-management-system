from django import forms
from .models import Employee
#here i m creating form....!
class Addrecordform(forms.ModelForm):
    
    class Meta:
        model =Employee
        fields = ("first_name","last_name","dept","salery","bonus","role","phone","hire_date")

class updaterecordform(forms.ModelForm):
    
    class Meta:
        model =Employee
        fields = ("first_name","last_name","dept","salery","bonus","role","phone","hire_date")
