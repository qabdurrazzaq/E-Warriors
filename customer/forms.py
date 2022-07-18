from pickle import NONE
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomerLoginForm(forms.Form):
    customername = forms.CharField(max_length=120,label='Customer Name')
    customerpassword = forms.CharField(widget=forms.PasswordInput(),label='Password')

    def clean_customername(self):
        customername = self.cleaned_data.get('customername')
        try:
            user = User.objects.get(username = customername)
        except User.DoesNotExist:
            user = None
            raise forms.ValidationError('No User Found')
        except:
            user = None
            pass
        return customername

    def clean_customerpassword(self):
        customername = self.cleaned_data.get('customername')
        customerpassword = self.cleaned_data.get('customerpassword')

        try:
            user = User.objects.get(username=customername)
        except:
            user = None
            pass

        if user is not None and not user.check_password(customerpassword):
            raise forms.ValidationError('Incorrect Password')
        elif user is None:
            pass
        else:
            return customerpassword
        
    def __init__(self,*args,**kwargs):
        super(CustomerLoginForm, self).__init__(*args, **kwargs)
        self.fields['customername'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Customer Name'})
        self.fields['customerpassword'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Password'})

class CustomerRegistrationForm(forms.ModelForm):
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
        user = super(CustomerRegistrationForm,self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs):
        super(CustomerRegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Username'})
        self.fields['email'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Email'})
        self.fields['password'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Password'})
        self.fields['confirm_password'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Confirm Password'})

# class CustomerDetailsForm(forms.Form):
#     first_name = forms.CharField(max_length=120,label = "First Name")
#     last_name = forms.CharField(max_length=120,label = "Last Name")
#     middle_name = forms.CharField(max_length=120,label = "Middle Name")
#     phone_number = forms.IntegerField(label = "Phone Number")

#     def save(self, commit=True):
#         user = super(CustomerDetailsForm,self).save(commit=False)
#         if commit:
#             user.save()
#         return user

#     def __init__(self, *args, **kwargs):
#         super(CustomerDetailsForm, self).__init__(*args, **kwargs)
#         self.fields['first_name'].widget.attrs.update({'class' : 'form-control','placeholder' : 'First Name'})
#         self.fields['last_name'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Last Name'})
#         self.fields['middle_name'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Middle Name'})
#         self.fields['phone_number'].widget.attrs.update({'class' : 'form-control','placeholder' : 'Phone Number'})