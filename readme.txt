def user_login(request):
  if request.method == 'POST':
    form = UserLoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'], password=cd['password'])
      if user is not None:
        login(request, user)
        txt = 'خوش آمدید' + user.first_name
        messages.success(request, txt)
        return redirect('user')
      else:
        messages.error(request, 'نام کاربری یا رمز عبور اشتباه است')
  else:
    form = UserLoginForm()
  return render(request, 'login.html', {'form':form})

def user_logout(request):
  logout(request)
  messages.success(request, 'خارج شدید')
  return redirect('home')

def user(request):
  return render(request, 'user.html')


------------------------------
class UserLoginForm(forms.Form):
  username = forms.CharField(label='نام کاربری')
  password = forms.CharField(label='رمزعبور', widget=forms.PasswordInput())

  ----------------------------

{% extends 'base.html' %}

{% block main %}
    <h1>صفحه کاربری</h1>
    <p>{{ request.user.first_name }}</p>
    {% if request.user.is_authenticated %}
        <a href="{% url 'logout' %}">خروج</a>
    {% else %}
        <h2>ابتدا وارد شوید</h2>
    {% endif %}
{% endblock %}