from django.shortcuts import render
from .forms import MyForm


def index(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']

            with open('contacts.txt', 'a') as file:
                file.write(f'{name}, {email}, {comment}\n')

            return render(request, 'main/index.html', {'form': form})
    else:
        form = MyForm()

    return render(request, 'main/index.html', {'form': form})

def create_form(request):
    if request.method == 'POST':
        form = MyForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            name = form.cleaned_data['name']
            comment = form.cleaned_data['comment']

            with open('contacts.txt', 'a') as file:
                file.write(f'{name}, {email}, {comment}\n')

            return redirect('success_url')  # замените 'success_url' на URL-адрес страницы успешной отправки
    else:
        form = MyForm()

    return render(request, 'lending/index.html', {'form': form})

