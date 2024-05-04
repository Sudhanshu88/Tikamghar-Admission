from .utils import requestInfo, responseInfo, getParams, updateTestRegistrationModel, updatePaymentDetailModel, getTestRegistrationDetails, createPDF
from .forms import TestRegistrationForm, PaymentDetailsForm, ValidateForm, ContactForm
from .PaytmChecksum import generateSignature, verifySignature, generateRandomString
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import TestRegistration
from django.conf import settings

def home(request):
    return render(request, 'home.html')

def admissionView(request):
    return render(request, 'admission.html')    

def thanksView(request):
    return render(request, 'thanks.html')  

def somethingWentWrongView(request):
    return render(request, 'somethingwentwrong.html')  

def notRegisteredView(request):
    return render(request, 'notregistered.html')  

def handler404(request, exception):
    return render(request, '404.html')  

def handler500(request):
    return render(request, '404.html')  

def contactUsView(request):
    #POST
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            return HttpResponseRedirect('/Thanks')
    #GET
    contact_form = ContactForm()
    context = {
        'contact_form' : contact_form
    }   
    return render(request, 'contact.html', context)

def entrenceTestView(request):
    #POST
    if request.method == 'POST':
        test_registration_form = TestRegistrationForm(request.POST, request.FILES)
        if test_registration_form.is_valid():
            test_registration_form.save()
            return HttpResponseRedirect('/Payment')
    #GET
    test_registration_form = TestRegistrationForm()
    context = {
        'test_registration_form': test_registration_form
    }
    return render(request, 'entrencetest.html', context)

def admitCardView(request):
    #POST
    if request.method == "POST": 
        try:
            response = createPDF(request)
            return response
        except:
            return HttpResponseRedirect('/NotRegistered')
    #GET
    make_payment_form = ValidateForm()
    context = {
        'make_payment_form': make_payment_form
    }
    return render(request, 'admitCard.html', context)

def makePaymentView(request):
    #GET
    make_payment_form = ValidateForm()
    context = {
        'make_payment_form': make_payment_form
    }
    return render(request, 'makepayment.html', context)

def payment(request):
    #POST
    if request.method == 'POST':
        make_payment_form = ValidateForm(request.POST)
        if make_payment_form.is_valid():
            isFound = TestRegistration.objects.get(DATEOFBIRTH=request.POST['DATEOFBIRTH'], PHONE=request.POST['PHONE'])
            amount = "100"
            if isFound:
                context = {
                    'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
                    'comany_name': settings.PAYTM_COMPANY_NAME,
                    'data_dict': requestInfo(request.POST['PHONE'], amount)
                }
                return render(request, 'payment.html', context)
            return HttpResponseRedirect('/NotRegistered')
        return HttpResponseRedirect('/FormNotValid')
    return HttpResponseRedirect('/Payment')


@csrf_exempt
def response(request):
    #POST
    if request.method == 'POST':
        isVerified = responseInfo(request)
        if isVerified:
            context = {
                'paytm_params':getParams(request)
            }
            updatePaymentDetailModel(request)
            updateTestRegistrationModel(request.POST['STATUS'], request.POST['ORDERID'])
            return render(request, 'response.html', context)
        else:
            return HttpResponseRedirect('/SomethingWentWrong')
    #GET
    return HttpResponseRedirect('/SomethingWentWrong')




















        # elif paytm_params['RESPCODE'] == '227':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #         # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '235':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #     # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '295':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #     # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '334':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #     # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '335':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #     # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '400':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #         return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '401':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #     # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '402':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #         return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '501':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #     # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)

        # elif paytm_params['RESPCODE'] == '810':
        #     if form.is_valid():
        #         form.save()
        #         modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
        #         modelObj.PAYMENT = request.POST['STATUS']
        #         modelObj.save()
        #     # rollback(paytm_params['ORDERID'])
        #     return render(request, 'response.html', context)




# def payment(request):
#     if request.method == 'POST':
#         test_registration_form = TestRegistrationForm(request.POST, request.FILES)
#         if test_registration_form.is_valid():
#             test_registration_form = test_registration_form.save(commit=False)
#             request.session['unsaved_model'] = serializers.serialize('xml', [test_registration_form, ])
#             data_dict = {
#                 'MID': settings.PAYTM_MERCHANT_ID,
#                 'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
#                 'WEBSITE': settings.PAYTM_WEBSITE,
#                 'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
#                 'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
#                 'MOBILE_NO': request.POST['PHONE'],
#                 'CUST_ID': generateRandomString(10),
#                 'ORDER_ID': generateRandomString(10),
#                 'TXN_AMOUNT': '100',
#             }
#             data_dict['CHECKSUMHASH'] = generateSignature(data_dict, settings.PAYTM_MERCHANT_KEY)
#             context = {
#                 'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
#                 'comany_name': settings.PAYTM_COMPANY_NAME,
#                 'data_dict': data_dict
#             }
#             return render(request, 'payment.html', context)
#         return HttpResponseRedirect('ifsorry')
#     return HttpResponseRedirect('sorry')

# @csrf_exempt
# def response(request):
#     paytm_params = dict()
#     for Key in request.POST.keys():
#         paytm_params[Key] = request.POST[Key]
#     paytmChecksum = paytm_params['CHECKSUMHASH']
#     paytm_params.pop('CHECKSUMHASH', None) 
#     isVerified = verifySignature(params=paytm_params, key=settings.PAYTM_MERCHANT_KEY,  checksum=paytmChecksum)
#     if isVerified:
#         form = PaymentForm(request.POST)
#         context = {
#             'paytm_params':paytm_params
#         }
#         if paytm_params['RESPCODE'] == '01':
#             if form.is_valid():
#                 form.save()
#                 string = request.session.get('unsaved_model')
#                 obj =serializers.deserialize('xml', string)
#                 for mymodel in obj:
#                     if mymodel == None:
#                         mymodel.save()
#                 # List = list()
#                 # for key in request.session.keys()
#                 #     List.push(key)
#                 form.save()
#                 return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '227':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '235':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '295':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '334':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '335':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '400':
#             if form.is_valid():
#                 form.save()
#                 return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '401':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '402':
#             if form.is_valid():
#                 form.save()
#                 return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '501':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)

#         elif paytm_params['RESPCODE'] == '810':
#             # rollback(paytm_params['ORDERID'])
#             return render(request, 'response.html', context)
#     else:
#         # rollback(paytm_params['ORDERID'])
#         return render(request, 'response.html', context)
#     # rollback(paytm_params['ORDERID'])
#     return render(request, 'response.html', context)


# def payment(request):
#     if request.method == 'POST':
#         form = StudentForm(request.POST)
#         if form.is_valid():
#             form = json.dumps(form.cleaned_data, default=str)
#             request.session['unsaved_form'] = form
#             data_dict = {
#                 'MID': settings.PAYTM_MERCHANT_ID,
#                 'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
#                 'WEBSITE': settings.PAYTM_WEBSITE,
#                 'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
#                 'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
#                 'MOBILE_NO': '7777777777',
#                 'EMAIL': 'dhaval.savalia6@gmail.com',
#                 'CUST_ID': '123123',
#                 'ORDER_ID':generateRandomString(20),
#                 'TXN_AMOUNT': '100',
#             } # This data should ideally come from database
#             data_dict['CHECKSUMHASH'] = generateSignature(data_dict, settings.PAYTM_MERCHANT_KEY)
#             context = {
#                 'payment_url': settings.PAYTM_PAYMENT_GATEWAY_URL,
#                 'comany_name': settings.PAYTM_COMPANY_NAME,
#                 'data_dict': data_dict
#             }
#             return render(request, 'payment.html', context)
#         return HttpResponseRedirect('ifsorry')
#     return HttpResponseRedirect('sorry')

# @csrf_exempt
# def response(request):
#     paytm_params = dict()
#     for Key in request.POST.keys():
#         paytm_params[Key] = request.POST[Key]
#     paytmChecksum = paytm_params['CHECKSUMHASH']
#     paytm_params.pop('CHECKSUMHASH', None)

#     isVerified = verifySignature(params=paytm_params, key=settings.PAYTM_MERCHANT_KEY,  checksum=paytmChecksum)
#     if isVerified:
#         context = {
#             'paytm_params':paytm_params
#         }
#         if paytm_params['RESPCODE'] == '01':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '227':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '235':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '295':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '334':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '335':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '400':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '401':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '402':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '501':
#             return render(request, 'response.html', context)
#         elif paytm_params['RESPCODE'] == '810':
#             return render(request, 'response.html', context)
#     else:
#         # check what happened; details in resp['paytm']
#         return HttpResponse("<center><h1>Transaction Failed</h1><center>", status=400)
#     return HttpResponse("<center><h1>Transaction Failed</h1><center>", status=400)

                # data_dict = {
                #     'MID': settings.PAYTM_MERCHANT_ID,
                #     'INDUSTRY_TYPE_ID': settings.PAYTM_INDUSTRY_TYPE_ID,
                #     'WEBSITE': settings.PAYTM_WEBSITE,
                #     'CHANNEL_ID': settings.PAYTM_CHANNEL_ID,
                #     'CALLBACK_URL': settings.PAYTM_CALLBACK_URL,
                #     'MOBILE_NO': request.POST['PHONE'],
                #     'CUST_ID': generateRandomString(10),
                #     'ORDER_ID': request.POST['PHONE'],
                #     'TXN_AMOUNT': '100',
                # }
                # data_dict['CHECKSUMHASH'] = generateSignature(data_dict, settings.PAYTM_MERCHANT_KEY)

                # paytm_params = dict()
    # for Key in request.POST.keys():
    #     paytm_params[Key] = request.POST[Key]
    # paytmChecksum = paytm_params['CHECKSUMHASH']
    # paytm_params.pop('CHECKSUMHASH', None) 
    # isVerified = verifySignature(params=paytm_params, key=settings.PAYTM_MERCHANT_KEY,  checksum=paytmChecksum)

    # modelObj = TestRegistration.objects.get(PHONE=request.POST['ORDERID'])
            # modelObj.PAYMENT = request.POST['STATUS']
            # modelObj.save()