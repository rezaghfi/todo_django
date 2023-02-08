from django import forms
class UserRegisterForm(forms.Form):
  username = forms.CharField(label='نام کاربری')
  email = forms.EmailField(label='ایمیل')
  password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput())
  firstname = forms.CharField(label='نام')
  lastname = forms.CharField(label='نام خانوادگی')
class UserLoginForm(forms.Form):
  username = forms.CharField(label='نام کاربری')
  password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput())



