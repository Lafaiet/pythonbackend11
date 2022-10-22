from django import forms
from django.contrib.auth.forms import UserCreationForm
from viewer.models import Profile


class ContactForm(forms.Form):
    name = forms.CharField(max_length=50)
    email = forms.EmailField()
    gender = forms.CharField(max_length=10, required=False)
    message = forms.CharField(max_length=500, widget=forms.Textarea)


class SignUpForm(UserCreationForm):

    def save(self):
        new_user = super().save()

        email = self.cleaned_data.get("email")
        new_user.email = email
        new_user.save()

        Profile.objects.create(user=new_user)

        return new_user

    email = forms.EmailField()

