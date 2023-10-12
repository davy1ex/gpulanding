from django import forms


class MyForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=100)
    email = forms.EmailField(label='Адрес электронной почты')
    comment = forms.CharField(label='Примечание', max_length=100)
    

