from django.db import models

# Create your models here.
class TestRegistration(models.Model):
    class1 = '1st'
    class2 = '2nd'
    class3 = '3rd'
    class4 = '4th'
    class5 = '5th'
    class6 = '6th'
    class7 = '7th'
    class8 = '8th'
    class9 = '9th'
    class10 = '10th'
    class11 = '11th'
    class12 = '12th'   

    admission_class = [
        (class1, '1st'),
        (class2, '2nd'),
        (class3, '3rd'),
        (class4, '4th'),
        (class5, '5th'),
        (class6, '6th'),
        (class7, '7th'),
        (class8, '8th'),
        (class9, '9th'),
        (class10, '10th'),
        (class11, '11th'),
        (class12, '12th'), 
    ]

    indexes = [
        models.Index(fields=['date_of_birth', 'phone',]),
    ]

    FIRSTNAME = models.CharField(max_length=50)
    MIDDLENAME = models.CharField(max_length=50, blank=True)
    LASTNAME = models.CharField(max_length=50)
    FATHERFIRSTNAME = models.CharField(max_length=50)
    DATEOFBIRTH = models.DateField()
    PHONE = models.CharField(unique=True, max_length=10)
    CLASSOFADMISSION = models.CharField(max_length=4, choices=admission_class)
    MARKSHEET = models.FileField(upload_to='Marksheets/')
    IMAGE = models.FileField(upload_to='Image/')
    UPLOADEDAT = models.DateTimeField(auto_now_add=True)
    PAYMENT = models.CharField(max_length=50, default="Null", blank=True)
    RESULT = models.CharField(max_length=50, default="Null", blank=True)


class PaymentDetails(models.Model):
    GATEWAYNAME = models.CharField(max_length=100)
    RESPMSG = models.CharField(max_length=100)
    BANKNAME = models.CharField(max_length=100)
    PAYMENTMODE = models.CharField(max_length=100)
    RESPCODE = models.CharField(max_length=100)
    TXNID = models.CharField(max_length=100)
    TXNAMOUNT = models.CharField(max_length=100)
    ORDERID = models.CharField(max_length=100)
    STATUS = models.CharField(max_length=100)
    BANKTXNID = models.CharField(max_length=100)
    TXNDATE = models.CharField(max_length=100)

class Contact(models.Model):
    NAME = models.CharField(max_length=50)
    EMAIL = models.EmailField()
    PHONE = models.CharField(max_length=10)
    SUBJECT = models.CharField(max_length=50)
    MESSAGE = models.TextField(max_length=500)
