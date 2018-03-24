from django import forms
from django.forms import ModelForm,PasswordInput, HiddenInput, Form, Textarea
from ezPayApp.models import *

class TransferForm(ModelForm):
    class Meta:
        model=Transfer
        fields = ['originMoneyMovementAccountReferenceId','destinationMoneyMovementAccountReferenceId','transferAmount','transferAmount','currencyCode','transferDate','memo','transferType','frequency']
        labels = {
            'originMoneyMovementAccountReferenceId': 'Reference ID for source of funds',
            'destinationMoneyMovementAccountReferenceId':'Reference ID for destination of funds',
            'transferAmount':'transfer Amount',
            'currencyCode':'Currency Code',
            'transferDate':'Transfer Date (in YYYY-MM-DD format)',
            'memo':'Memo',
            'transferType':'Transfer Type',
            'frequency':'Frequency'
        }
