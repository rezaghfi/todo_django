--------------------- forms.py
class TodoUpdateForm(forms.ModelForm):
  class Meta:
    model = Todo
    fields = ('title', 'body', 'created')

-------------------- update.html
{% extends 'base.html' %}

{% block main %}
    <form action="" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <input type="submit" value="بروزرسانی شد">
    </form>
{% endblock %}

---------------------- views.py


def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    if request.method == 'POST':
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'این کار با موفقیت بروزرسانی شد')
            return redirect('detail', todo_id)
    else:
        form = TodoUpdateForm(instance=todo)
    return render(request, 'update.html', {'form': form})