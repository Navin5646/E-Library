from .models import Book
from django import forms
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'author',
            'price',
            'publish_date',
        ]

"""from django.contrib.auth import(
        authenticate,
        get_user_model,
        login,
        logout
    )
user=get_user_model()
class BookForm(Forms.ModelForm):
    name=forms.CharField(max_length=10, help_text= "write your full name")

   
class UserRegistrationForm(Forms.ModelForm):
    email=forms.EmailField(Label='Email Address')
    email2=forms.EmailField(Label='Confirm Email')
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=[
            'username',
            'email',
            'email2',
            'password',
        ]
        def clean_email2(self):
            email=self.cleaned_data.get('email')
            email2=self.cleaned_data.get('email2')
            if email !=email2:
                raise forms.ValidateionError("email must match")
            emial_qs=User.objects.filter(email=email)
            if email_qs.exist():
                raise forms.ValidateionError("email is already registerd")
            return email
class UserLoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.passwordInput)
    def clean(self, *args, **kwargs):
        username=self.cleaned_date.get('username')
        password=self.cleaned_date.get('paswword')
        if username and password:
            user=authenticate(username=username,password=password)
            if not user:
                raise forms.ValidateionError("the user is not exist")
            if not user.check_password(password):
                raise forms.ValidateionError("invalid password")
                if not user.is_active:
                    raise forms.ValidateionError("the user is no longer active")
            return super(UserLoginForm,self).clean(*args, **kwargs)
"""








