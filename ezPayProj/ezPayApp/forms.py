from django import forms
from django.forms import ModelForm,PasswordInput, HiddenInput, Form, Textarea
from ezPayApp.models import *

class TransferForm(ModelForm):
    class Meta:
        model=Transfer