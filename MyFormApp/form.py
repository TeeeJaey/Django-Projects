from django import forms
from django.core import validators

def check_for_t(value):
    if(value[0].lower() != 't'):
        raise forms.ValidationError('Name must start with a T')


def check_pswrd_match(psw,cnfpsw):
    if (psw != cnfpsw): 
        raise forms.ValidationError('Password doesnot match!')

class FormName(forms.Form):

    name = forms.CharField(validators=[check_for_t])
    email = forms.EmailField()
    password = forms.CharField( widget=forms.PasswordInput)
    cnfPassword = forms.CharField(label="Confirm Password", widget=forms.PasswordInput)
    text = forms.CharField(required=False, widget=forms.Textarea)

    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) 

    def clean(self):
        allCleanData = super().clean()
        psw = allCleanData['password']
        cnfpsw = allCleanData['cnfPassword']
        
        check_pswrd_match(psw,cnfpsw)
        



    """
    def clean_botcatcher(self):
        botcatcher = self.cleaned_data['botcatcher']

        if(len(botcatcher) > 0):
            raise forms.ValidationError("Bot found!")
    """     
