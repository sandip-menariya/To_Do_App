from .models import Task 
from django import forms

class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=["title","description","status"]
        widgets={
            "title" : forms.TextInput(attrs={"class":"form-control"}),
            "description" : forms.Textarea(attrs={"class":"form-control", "rows":3}),
            "status" : forms.Select(attrs={"class":"form-control"}),
        }

