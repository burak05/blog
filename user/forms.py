from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50,label="username")
    password = forms.CharField(max_length=20,label="password",widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="username")
    password = forms.CharField(max_length=20,label="password",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="confirm password",widget=forms.PasswordInput)

def clean(self):
    username = self.cleaned_data_get("username")
    password = self.cleaned_data_get("password")
    confirm = self.cleaned_data_get("confirm")

    if password and confirm and password != confirm:
        raise forms.ValidationError("Passwords do not match!!")
    
    values = {
        "username" : username,
        "password" : password
    }
    return values