from django import forms
from home.models import Todo


class TodoCreateForm(forms.Form):
  title = forms.CharField(max_length=10, label='عنوان کار', min_length=2)
  body = forms.CharField(label='محتوای کار')
  created = forms.DateTimeField(label='تاریخ ایجاد')

class TodoUpdateForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ('title', 'body', 'created')
    labels={
      'title': 'عنوان کار',
      'body': 'محتوای کار',
      'created': 'تاریخ ایجاد'
    }
