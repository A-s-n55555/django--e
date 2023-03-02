from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError("name must start with z")

class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_z,])
    email =forms.EmailField()
    verify_email = forms.EmailField(label='enter again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField( required=False,
                                widget =forms.HiddenInput,
                                validators=[validators.MaxLengthValidator(0)]              )
    # we have another django built in bot capture 
    # this is bot validator by user 
    # def clean_botcatcher(self):
    #     botcatcher =self.cleaned_data['botcatcher']
    #     if len(botcatcher)>0:
    #         raise forms.ValidationError("gotcha bot")
    #         return botcatcher