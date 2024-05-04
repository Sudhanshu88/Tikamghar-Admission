from django.contrib import admin
from .models import TestRegistration, PaymentDetails, Contact

# Register your models here.
class TestRegistrationAdmin(admin.ModelAdmin):
    list_display = ('FIRSTNAME', 'MIDDLENAME', 'LASTNAME', 'FATHERFIRSTNAME', 'DATEOFBIRTH', 'PHONE', 'CLASSOFADMISSION', 'MARKSHEET', 'IMAGE', 'PAYMENT', 'RESULT')

admin.site.register(TestRegistration, TestRegistrationAdmin)

class PaymentDetailsAdmin(admin.ModelAdmin):
    list_display = ('GATEWAYNAME', 'RESPMSG', 'BANKNAME', 'PAYMENTMODE', 'RESPCODE', 'TXNID', 'TXNAMOUNT', 'ORDERID', 'STATUS', 'BANKTXNID', 'TXNDATE')

admin.site.register(PaymentDetails, PaymentDetailsAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('NAME', 'EMAIL', 'PHONE', 'SUBJECT', 'MESSAGE')

admin.site.register(Contact, ContactAdmin)