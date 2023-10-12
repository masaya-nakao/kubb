from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from .models import CustomUser
from django.core.exceptions import ValidationError
from django import forms

class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password')


class LoginForm(AuthenticationForm):
    class Meta:
        username = forms.CharField(label="ユーザー名", min_length=3, max_length=30)
        email = forms.EmailField(label="メールアドレス")
        password = forms.CharField(label="パスワード", widget=forms.PasswordInput)
        
        def validate_email_endswith_st_kyoto(self):
            email = self.cleaned_data.get('email')
            if not email.endswith('@st.kyoto-u.ac.jp'):
                raise ValidationError("メールアドレスは '@st.kyoto-u.ac.jp' で終わる必要があります。")