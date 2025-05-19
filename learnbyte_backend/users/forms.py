from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True, label="Register as")

    def save(self, request):
        user = super().save(request)
        user.role = self.cleaned_data['role']
        user.save()
        return user
