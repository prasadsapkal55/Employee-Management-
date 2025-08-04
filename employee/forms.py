from django import forms
from employee.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"
        widgets = {
            'eid': forms.TextInput(attrs={
                'class': 'form-control input-with-icon',
                'placeholder': 'Enter Employee ID',
                'required': True
            }),
            'ename': forms.TextInput(attrs={
                'class': 'form-control input-with-icon',
                'placeholder': 'Enter Full Name',
                'required': True
            }),
            'eemail': forms.EmailInput(attrs={
                'class': 'form-control input-with-icon',
                'placeholder': 'Enter Email Address',
                'required': True
            }),
            'econtact': forms.TextInput(attrs={
                'class': 'form-control input-with-icon',
                'placeholder': 'Enter Contact Number',
                'required': True
            }),
        }
        labels = {
            'eid': 'Employee ID',
            'ename': 'Employee Name',
            'eemail': 'Email Address',
            'econtact': 'Contact Number',
        }