from pickle import NONE
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class DealerLoginForm(forms.Form):
    dealername = forms.CharField(max_length=120,label='Dealer Name')
    dealerpassword = forms.CharField(widget=forms.PasswordInput(),label='Password')

    def clean_dealername(self):
        dealername = self.cleaned_data.get('dealername')
        try:
            user = User.objects.get(username = dealername)
        except User.DoesNotExist:
            user = None
            raise forms.ValidationError('No User Found')
        except:
            user = None
            pass
        return dealername

    def clean_dealerpassword(self):
        dealername = self.cleaned_data.get('dealername')
        dealerpassword = self.cleaned_data.get('dealerpassword')

        try:
            user = User.objects.get(username=dealername)
        except:
            user = None
            pass

        if user is not None and not user.check_password(dealerpassword):
            raise forms.ValidationError('Incorrect Password')
        elif user is None:
            pass
        else:
            return dealerpassword
        
    def __init__(self,*args,**kwargs):
        super(DealerLoginForm, self).__init__(*args, **kwargs)
        self.fields['dealername'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Dealer Name'})
        self.fields['dealerpassword'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Password'})

class DealerRegistrationForm(forms.ModelForm):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput(),label='Confirm Password')

    class Meta:
        model = User
        help_texts = {
            'username' : None,
        }
        fields = ['username','email']

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('No Matching Passwords')
        return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_count = User.objects.filter(email=email).count()
        if email_count > 0:
            raise forms.ValidationError('E-Mail Already Registered')
        return email

    def save(self, commit=True):
        user = super(DealerRegistrationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(DealerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Username'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Email'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Password'})
        self.fields['confirm_password'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Confirm Password'})