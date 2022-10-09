from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    gender = forms.CharField(max_length=10, required=False)
    message = forms.CharField(max_length=500, widget=forms.Textarea)