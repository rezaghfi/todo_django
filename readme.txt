def user_register(request):
  if request.method == 'POST':
    form = UserRegistrationForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = User.objects.create_user(username=cd['username'], email=cd['email'], password=cd['password'])
      user.first_name = cd['firstName']
      user.last_name = cd['lastName']
      user.save()
      messages.success(request, 'کاربر با موفقیت وارد شد')
      return redirect('home')
  else:
    form = UserRegistrationForm()
  return render(request, 'register.html', {'form': form})

----------------------------------------
def user_login(request):
  if request.method == 'POST':
    form = UserLoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'], password=['password'])
      if user is not None:
        login(request, user)
        messages.success(request, 'کاربر با موفقیت وارد شد')
        return redirect('home')
      else:
        messages.error(request, 'کاربری یا رمز اشتباه است')
  else:
    form = UserLoginForm()
  return render(request, 'login.html', {'form': form})


------------------------------
class UserRegistrationForm(forms.Form):
  username = forms.CharField()
  firstName = forms.CharField()
  lastName = forms.CharField()
  email = forms.CharField()
  password = forms.CharField()


class UserLoginForm(forms.Form):
  username = forms.CharField()
  password = forms.CharField()