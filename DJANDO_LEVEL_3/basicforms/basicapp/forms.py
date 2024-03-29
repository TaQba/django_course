from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower() != 'z':
        raise forms.ValidationError('Name needs to start with Z!')

class FormName(forms.Form):
    # name = forms.CharField(validators=[check_for_z])
    name = forms.CharField()
    email = forms.EmailField(validators=[validators.EmailValidator()])
    varify_email = forms.EmailField(label='Enter your email again:')
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Got error')
    #     return botcatcher


    def clean(self):
        all_clean_data = super().clean()
        email = all_clean_data['email']
        vmail = all_clean_data['varify_email']

        if email != vmail:
            raise forms.ValidationError("Make sure it match")