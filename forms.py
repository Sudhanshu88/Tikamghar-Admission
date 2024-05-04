from django import forms
from django.forms import ModelForm
from .models import TestRegistration, PaymentDetails, Contact

class ValidateForm(forms.Form):
    DATEOFBIRTH = forms.DateField(label='Date of birth', widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    PHONE = forms.IntegerField(label='Phone', widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'7777777777', 'type':'tel'}))

class TestRegistrationForm(ModelForm):
    class Meta:
        model = TestRegistration
        fields = ['FIRSTNAME', 'MIDDLENAME', 'LASTNAME', 'FATHERFIRSTNAME', 'DATEOFBIRTH', 'PHONE', 'CLASSOFADMISSION', 'MARKSHEET', 'IMAGE']
        labels = {
            'FIRSTNAME':'First Name',
            'MIDDLENAME':'Middle Name',
            'LASTNAME':'Last Name',
            'FATHERFIRSTNAME':'Father\'s First Name',
            'DATEOFBIRTH':'Date of birth',
            'PHONE':'Phone',
            'CLASSOFADMISSION':'Class of admission',
            'MARKSHEET':'Marksheet',
            'IMAGE':'Image'
        }
        widgets={
            'FIRSTNAME': forms.TextInput(attrs={'class': 'form-control','placeholder': 'First Name'}),
            'MIDDLENAME': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Middle Name'}),
            'LASTNAME': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Last Name'}),
            'FATHERFIRSTNAME': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Father\'s First Name'}),
            'DATEOFBIRTH': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'PHONE': forms.TextInput(attrs={'class':'form-control', 'placeholder':'7777777777', 'type':'tel'}),
            'CLASSOFADMISSION': forms.Select(attrs={'class':'form-control'}),
            'MARKSHEET': forms.FileInput(attrs={'class':'form-control'}),
            'IMAGE': forms.FileInput(attrs={'class':'form-control'}),
        }
    # FIRSTNAME = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
    # MIDDLENAME = forms.CharField(max_length=50, required=False , widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Middle Name'}))
    # LASTNAME = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
    # DATEOFBIRTH = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control'}))
    # PHONE = forms.IntegerField(max_value=999999999, widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'7777777777'}))
    # CLASSOFADMISSION = forms.CharField(max_length=4, widget=forms.Select(choices=admission_class, attrs={'class':'form-control'}))
    # MARKSHEET = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))
    # IMAGE = forms.FileField(widget=forms.FileInput(attrs={'class':'form-control'}))

class PaymentDetailsForm(ModelForm):
    class Meta:
        model = PaymentDetails
        fields = ['GATEWAYNAME', 'RESPMSG', 'BANKNAME', 'PAYMENTMODE', 'RESPCODE', 'TXNID', 'TXNAMOUNT', 'ORDERID', 'STATUS', 'BANKTXNID', 'TXNDATE']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['NAME', 'EMAIL', 'PHONE', 'SUBJECT', 'MESSAGE']
        widgets={
            'NAME': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name'}),
            'EMAIL': forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Email', 'type': 'email'}),
            'PHONE': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone', 'type':'tel'}),
            'SUBJECT': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Subject'}),
            'MESSAGE': forms.Textarea(attrs={'class':'form-control', 'type':'textarea','placeholder': 'Message . . .'}),
        }