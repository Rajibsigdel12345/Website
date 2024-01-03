from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    accountType = forms.CharField(label="Account Type", widget=forms.RadioSelect(
        choices=(("GUEST", "GUEST"), ("RECEPTIONIST", "RECEPTIONIST"), ("HOUSEKEEPING", "HOUSEKEEPING"),)))

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "accountType"]

        def save(self, commit=True):
            user = super(NewUserForm, self).save(commit=False)
            user.email = self.cleaned_data['email']
            if commit:
                user.save()
            return user
