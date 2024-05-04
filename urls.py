from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('Home', views.home, name='Home'),
    path('EntrenceTest', views.entrenceTestView, name='EntrenceTest'),
    path('payment', views.payment, name='Payment'),
    path('response', views.response, name='Response'),
    path('Payment', views.makePaymentView, name='MakePayment'),
    path('AdmitCard', views.admitCardView, name='AdmitCard'),
    path('ContactUs', views.contactUsView, name='ContactUs'),
    path('Admission', views.admissionView, name='Admission'),
    path('Thanks', views.thanksView, name='Thanks'),
    path('SomethingWentWrong', views.somethingWentWrongView, name='SomethingWentWrong'),
    path('NotRegistered', views.notRegisteredView, name='NotRegistered'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

