from django import forms


class TodoCreateForm(forms.Form):
  title = forms.CharField(max_length=10, label='عنوان کار')
  body = forms.CharField(label='محتوای کار')
  created = forms.DateTimeField(label='تاریخ ایجاد')
