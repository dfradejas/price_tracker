from django import forms

class AddItemForm(forms.Form):
    url = forms.CharField(label='URL: ', max_length=250)