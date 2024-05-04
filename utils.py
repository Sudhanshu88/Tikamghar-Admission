from .models import TestRegistration, PaymentDetails
from .PaytmChecksum import generateRandomString, generateSignature, verifySignature
from django.conf import settings
from reportlab.pdfgen import canvas  
from reportlab.lib.utils import ImageReader
from .forms import ValidateForm
from django.shortcuts import HttpResponse

def requestInfo(phone, amount):
    data_dict = {
        'MID': settings.PAYTM_MERCHANT_ID,
        'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
        'WEBSITE': settings.PAYTM_WEBSITE,
        'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
        'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
        'MOBILE_NO': phone,
        'CUST_ID': generateRandomString(10),
        'ORDER_ID': phone,
        'TXN_AMOUNT': amount,
    }
    data_dict['CHECKSUMHASH'] = generateSignature(data_dict, settings.PAYTM_MERCHANT_KEY)
    return data_dict

def getParams(request):
    paytm_params = dict()
    for Key in request.POST.keys():
        paytm_params[Key] = request.POST[Key]
    return paytm_params

def responseInfo(request):
    paytm_params = getParams(request)
    paytmChecksum = paytm_params['CHECKSUMHASH']
    paytm_params.pop('CHECKSUMHASH', None) 
    isVerified = verifySignature(params=paytm_params, key=settings.PAYTM_MERCHANT_KEY,  checksum=paytmChecksum)
    return isVerified

def updateTestRegistrationModel(status, orderId):
    modelObj = TestRegistration.objects.get(PHONE=orderId)
    modelObj.PAYMENT = status
    modelObj.save()

def updatePaymentDetailModel(request):
    mymodel = PaymentDetails(
        GATEWAYNAME=request.POST['GATEWAYNAME'],
        RESPMSG=request.POST['RESPMSG'],
        BANKNAME=request.POST['BANKNAME'],
        PAYMENTMODE=request.POST['PAYMENTMODE'],
        RESPCODE=request.POST['RESPCODE'],
        TXNID=request.POST['TXNID'],
        TXNAMOUNT=request.POST['TXNAMOUNT'],
        ORDERID=request.POST['ORDERID'],
        STATUS=request.POST['STATUS'],
        BANKTXNID=request.POST['BANKTXNID'],
        TXNDATE=request.POST['TXNDATE'],
    )
    mymodel.save()

def getTestRegistrationDetails(request):
    Data = TestRegistration.objects.get(DATEOFBIRTH=request.POST['DATEOFBIRTH'], PHONE=request.POST['PHONE'])
    return Data

def createPDF(request):
    make_payment_form = ValidateForm(request.POST)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="MyAdmitCard.pdf"' 
    data = getTestRegistrationDetails(request)
    p = canvas.Canvas(response)
    image = ImageReader(data.IMAGE)
    background = ImageReader('Static\\assets\\img\\background.png')
    
    name = 'Name: ' + data.FIRSTNAME + ' ' + data.MIDDLENAME + ' ' + data.LASTNAME
    father = "Father's Name: " + data.FATHERFIRSTNAME
    phone = 'Phone: ' + data.PHONE
    dateofbirth = 'Date of birth: ' + data.DATEOFBIRTH.strftime('%m/%d/%Y')
    classofadmission = 'Class of admission: ' + data.CLASSOFADMISSION
    payment = 'Fee: ' + 'Submitted' if data.PAYMENT == "TXN_SUCCESS" else 'Pending'
    p.setFont("Times-Roman", 12)
    p.drawImage(background, 0,650-90, mask='auto', width=600, height=240)
    p.drawBoundary(0,45,667-50,135,135)
    p.drawImage(image, 50,672-50, mask='auto', width=125, height=125)
    p.drawBoundary(0,10,625-50,575,212)
    p.drawString(200, 790-50, name)
    p.drawString(200, 770-50, father)
    p.drawString(200, 750-50, dateofbirth)
    p.drawString(200, 730-50, classofadmission)
    p.drawString(200, 710-50, phone)
    p.drawString(200, 690-50, payment)
    
    p.showPage()  
    p.save() 
    return response