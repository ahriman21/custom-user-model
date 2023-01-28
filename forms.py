from django import forms
from .models import User
from django.core.exceptions import ValidationError
#

class UserSignUpForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['full_name','email','password','confirm_password']
        widgets = {
            'password' : forms.PasswordInput()
        }


    def clean_email(self):
        user_email = self.cleaned_data.get('email')
        email_exist = User.objects.filter(email=user_email).exists()
        if email_exist:
            raise ValidationError('ایمیل وارد شده تکراری است . لطفاایمیل دیگری وارد کنید.')
        return user_email

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise ValidationError('گذرواژه باید باهم دیگر مطاقبت داشته باشند.')
        return confirm_password

    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 4:
            raise ValidationError('گذرواژه دست کم باید 4 کاراکتر باشد.')
        return password

      
      
class UserSignInForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())
    
        
