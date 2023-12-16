from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django import forms
from allauth.account.forms import (
    SignupForm,
    LoginForm,
)

def validate_username_length(value):
    if len(value) < 3:
        raise ValidationError('Username must be at least 3 characters long')


class CustomSignupForm(SignupForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #classにbootstrapのform-controlを指定したい場合
        if 'username' in self.fields:
            self.fields['username'].widget.attrs['class'] = 'form-control'
            self.fields['email'].widget.attrs['class'] = 'form-control'
            self.fields['password1'].widget.attrs['class'] = 'form-control'
            self.fields['password2'].widget.attrs['class'] = 'form-control'
            #placeholderを設定したい場合
            self.fields['username'].widget.attrs['placeholder'] = 'Please enter between 3 and 10 characters.'
            self.fields['email'].widget.attrs['placeholder'] = '+@st.kyoto-u.ac.jp'
            self.fields['password1'].widget.attrs['placeholder'] = 'Password'
            self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
            #labelを設定したい場合
            self.fields['username'].label = 'Username (Be careful, Username cannot be changed!):'
            self.fields['email'].label = 'KUMOI adress:'
            self.fields['password1'].label = 'Password:'
            self.fields['password2'].label = 'Confirm Password:'
            self.fields['username'].validators.append(validate_username_length)
            self.fields['username'].max_length = 10
            
            self.fields['email'].validators.append(
                RegexValidator(
                    regex=r'.+@st\.kyoto-u\.ac\.jp$',
                    message='Enter a valid email address ending with @st.kyoto-u.ac.jp',
                )
            )
    #class Meta(UserCreationForm.Meta):
    #    model = CustomUser
    #    fields = ('username', 'email', 'password')


class CustomLoginForm(LoginForm):
    success_url = '/'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #classにbootstrapのform-controlを指定したい場合
        self.fields['login'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        #placeholderを設定したい場合
        self.fields['login'].widget.attrs['placeholder'] = 'Email'
        self.fields['password'].widget.attrs['placeholder'] = 'Password'
        #labelを設定したい場合
        self.fields['login'].label = 'Email:'
        self.fields['password'].label = 'Password:'
        
    